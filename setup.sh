#!/bin/bash

echo "🎨 Instalando Bot de Facturas Dolce Arty..."
echo ""

# Check Node.js
if ! command -v node &> /dev/null; then
    echo "❌ Node.js no está instalado"
    echo "Instálalo desde: https://nodejs.org/"
    exit 1
fi

echo "✅ Node.js encontrado: $(node --version)"

# Check Python
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 no está instalado"
    exit 1
fi

echo "✅ Python 3 encontrado: $(python3 --version)"

# Install Node dependencies
cd /home/claude/whatsapp-bot
echo ""
echo "📦 Instalando dependencias de Node.js..."
npm install

# Check Python reportlab
echo ""
echo "📦 Verificando reportlab..."
python3 -c "import reportlab" 2>/dev/null
if [ $? -ne 0 ]; then
    echo "⚠️  Instalando reportlab..."
    pip install reportlab --break-system-packages
fi

echo ""
echo "✅ ¡Instalación completa!"
echo ""
echo "🚀 Para iniciar el bot:"
echo "   cd /home/claude/whatsapp-bot"
echo "   node bot.js"
echo ""
echo "📱 Luego escanea el código QR con WhatsApp"
echo ""
