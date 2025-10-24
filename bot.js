const { default: makeWASocket, DisconnectReason, useMultiFileAuthState } = require('@whiskeysockets/baileys');
const { Boom } = require('@hapi/boom');
const P = require('pino');
const qrcode = require('qrcode-terminal');
const { exec } = require('child_process');
const fs = require('fs');
const path = require('path');

// Invoice counter - load from file if exists
let invoiceCounter = 137; // Start from your last invoice number
const COUNTER_FILE = './invoice_counter.txt';

if (fs.existsSync(COUNTER_FILE)) {
    invoiceCounter = parseInt(fs.readFileSync(COUNTER_FILE, 'utf8'));
}

function saveCounter() {
    fs.writeFileSync(COUNTER_FILE, invoiceCounter.toString());
}

// Parse invoice request from message
function parseInvoiceRequest(message) {
    // Examples:
    // "factura Maria Lopez, 2 horas"
    // "invoice John Doe, 1.5 hours"
    // "Maria, 3hrs"
    
    const text = message.toLowerCase().trim();
    
    // Extract name and hours
    const patterns = [
        /(?:factura|invoice)?\s*(?:para\s+)?([^,]+),\s*(\d+\.?\d*)\s*(?:horas?|hrs?|hours?)/i,
        /([^,]+),\s*(\d+\.?\d*)\s*(?:horas?|hrs?|hours?)/i,
    ];
    
    for (const pattern of patterns) {
        const match = text.match(pattern);
        if (match) {
            const name = match[1].trim();
            const hours = parseFloat(match[2]);
            return { name, hours };
        }
    }
    
    return null;
}

// Generate invoice using Python script
function generateInvoice(clientName, hours, invoiceNumber) {
    return new Promise((resolve, reject) => {
        const amount = Math.round(hours * 350); // 350 DHS per hour
        const outputPath = `/tmp/invoice_${clientName.replace(/\s+/g, '')}_${invoiceNumber}.pdf`;
        const description = `${hours} hr${hours !== 1 ? 's' : ''}. Class, 1 person.`;
        
        // Get the correct paths for cloud or local
        const projectRoot = process.env.RAILWAY_STATIC_URL ? '/app' : '/home/claude';
        const invoiceGenPath = `${projectRoot}/dolce-arty-invoices`;
        
        // Call Python invoice generator with current date
        const pythonScript = `
import sys
sys.path.insert(0, '${invoiceGenPath}')
from invoice_generator import create_invoice

create_invoice(
    output_path="${outputPath}",
    client_name="${clientName}",
    invoice_number="${invoiceNumber}",
    description="${description}",
    amount="${amount}"
)
`;
        
        const tempScript = `/tmp/generate_invoice_${Date.now()}.py`;
        fs.writeFileSync(tempScript, pythonScript);
        
        exec(`python3 ${tempScript}`, (error, stdout, stderr) => {
            fs.unlinkSync(tempScript); // Clean up temp script
            
            if (error) {
                console.error('Error generating invoice:', error);
                console.error('stderr:', stderr);
                reject(error);
                return;
            }
            
            resolve({
                path: outputPath,
                amount: amount,
                hours: hours,
                invoiceNumber: invoiceNumber
            });
        });
    });
}

async function connectToWhatsApp() {
    const { state, saveCreds } = await useMultiFileAuthState('auth_info_baileys');
    
    const sock = makeWASocket({
        auth: state,
        printQRInTerminal: true,
        logger: P({ level: 'silent' })
    });
    
    sock.ev.on('creds.update', saveCreds);
    
    sock.ev.on('connection.update', (update) => {
        const { connection, lastDisconnect, qr } = update;
        
        if (qr) {
            console.log('\n📱 Escanea este código QR con WhatsApp:\n');
            qrcode.generate(qr, { small: true });
        }
        
        if (connection === 'close') {
            const shouldReconnect = (lastDisconnect?.error instanceof Boom)?.output?.statusCode !== DisconnectReason.loggedOut;
            console.log('Conexión cerrada. Reconectando:', shouldReconnect);
            
            if (shouldReconnect) {
                connectToWhatsApp();
            }
        } else if (connection === 'open') {
            console.log('✅ Conectado a WhatsApp!');
            console.log('🤖 Bot de facturas Dolce Arty activo');
            console.log('\n📝 Comandos disponibles:');
            console.log('  - "factura [Nombre], [horas] horas"');
            console.log('  - "help" - Ver ayuda\n');
        }
    });
    
    sock.ev.on('messages.upsert', async ({ messages }) => {
        const msg = messages[0];
        
        if (!msg.message || msg.key.fromMe) return;
        
        const messageText = msg.message.conversation || msg.message.extendedTextMessage?.text || '';
        const from = msg.key.remoteJid;
        
        console.log(`\n💬 Mensaje de ${from}: ${messageText}`);
        
        // Help command
        if (messageText.toLowerCase().includes('help') || messageText.toLowerCase().includes('ayuda')) {
            await sock.sendMessage(from, {
                text: `🎨 *Dolce Arty - Bot de Facturas*

📝 Para generar una factura, envía:
*factura [Nombre], [horas] horas*

Ejemplos:
• factura Maria Lopez, 2 horas
• invoice John Smith, 1.5 hours
• Ana Garcia, 3 hrs

💰 Tarifa: 350 DHS/hora

El número de factura se asigna automáticamente.
Recibirás el PDF en segundos! ✅`
            });
            return;
        }
        
        // Try to parse as invoice request
        const invoiceData = parseInvoiceRequest(messageText);
        
        if (invoiceData) {
            try {
                await sock.sendMessage(from, { 
                    text: `⏳ Generando factura para ${invoiceData.name}...` 
                });
                
                // Generate invoice
                const currentInvoiceNumber = invoiceCounter;
                invoiceCounter++;
                saveCounter();
                
                const invoice = await generateInvoice(
                    invoiceData.name, 
                    invoiceData.hours, 
                    currentInvoiceNumber
                );
                
                // Send PDF
                const pdfBuffer = fs.readFileSync(invoice.path);
                
                await sock.sendMessage(from, {
                    document: pdfBuffer,
                    mimetype: 'application/pdf',
                    fileName: `Invoice_${currentInvoiceNumber}_${invoiceData.name.replace(/\s+/g, '')}.pdf`,
                    caption: `✅ *Factura #${currentInvoiceNumber}*

👤 Cliente: ${invoiceData.name}
⏱️ Servicio: ${invoiceData.hours} hr${invoiceData.hours !== 1 ? 's' : ''}. Class, 1 person
💵 Total: ${invoice.amount}.00 DHS

_Dolce Arty - Art Academy_`
                });
                
                // Clean up temp file
                fs.unlinkSync(invoice.path);
                
                console.log(`✅ Factura #${currentInvoiceNumber} enviada`);
                
            } catch (error) {
                console.error('Error:', error);
                await sock.sendMessage(from, { 
                    text: `❌ Error generando la factura. Por favor intenta de nuevo o contacta soporte.` 
                });
            }
        } else {
            // Unknown command
            await sock.sendMessage(from, {
                text: `❓ No entendí el comando.

Envía *"help"* para ver cómo crear facturas.`
            });
        }
    });
    
    return sock;
}

// Start the bot
console.log('🚀 Iniciando bot de WhatsApp Dolce Arty...\n');
connectToWhatsApp();

// Handle process termination
process.on('SIGINT', () => {
    console.log('\n\n👋 Bot detenido. Adiós!');
    process.exit(0);
});
