# 🎨 Dolce Arty WhatsApp Invoice Bot

Bot de WhatsApp para generar facturas automáticamente para Dolce Arty.

## 📋 Características

- ✅ Genera facturas en PDF automáticamente
- ✅ Usa tu WhatsApp personal (sin costos adicionales)
- ✅ Numeración automática de facturas
- ✅ Cálculo automático de precios (350 DHS/hora)
- ✅ Responde en segundos
- ✅ Formato profesional con tu branding

## 🚀 Instalación

### Requisitos previos

1. **Node.js** (v16 o superior)
2. **Python 3** con reportlab
3. **Tu teléfono con WhatsApp**

### Paso 1: Instalar dependencias

```bash
cd /home/claude/whatsapp-bot
npm install
```

### Paso 2: Instalar Python dependencies

```bash
pip install reportlab --break-system-packages
```

### Paso 3: Copiar assets de facturas

```bash
# Los assets ya están en /home/claude/dolce-arty-invoices/assets/
# No necesitas hacer nada más
```

## ▶️ Cómo usar

### Iniciar el bot

```bash
cd /home/claude/whatsapp-bot
node bot.js
```

### Primera vez - Escanear código QR

1. Ejecuta `node bot.js`
2. Verás un código QR en la terminal
3. Abre WhatsApp en tu teléfono
4. Ve a: **Configuración > Dispositivos vinculados**
5. Toca **"Vincular un dispositivo"**
6. Escanea el código QR

✅ ¡Listo! Tu WhatsApp está conectado.

### Enviar comandos por WhatsApp

Una vez conectado, envía mensajes a tu propio número (o pídele a alguien que te escriba):

**Generar factura:**
```
factura Maria Lopez, 2 horas
```

**Otros formatos válidos:**
```
invoice John Smith, 1.5 hours
Ana Garcia, 3 hrs
factura para Pedro, 1 hora
```

**Ver ayuda:**
```
help
```

## 💬 Ejemplos de uso

### Ejemplo 1: Factura simple
**Tú escribes:**
```
factura Alina, 1 hora
```

**Bot responde:**
```
⏳ Generando factura para Alina...

✅ Factura #138
👤 Cliente: Alina
⏱️ Servicio: 1 hr. Class, 1 person
💵 Total: 350.00 DHS

[Adjunta PDF]
```

### Ejemplo 2: Clase de 3 horas
**Tú escribes:**
```
invoice Homer Smith, 3 hours
```

**Bot responde:**
```
✅ Factura #139
👤 Cliente: Homer Smith
⏱️ Servicio: 3 hrs. Class, 1 person
💵 Total: 1050.00 DHS

[Adjunta PDF]
```

## ⚙️ Configuración

### Cambiar el número de factura inicial

Edita `bot.js` línea 10:

```javascript
let invoiceCounter = 137; // Cambia este número
```

### Cambiar la tarifa por hora

Edita `bot.js` línea 47:

```javascript
const amount = hours * 350; // Cambia 350 por tu tarifa
```

### Cambiar información de pago

Edita `/home/claude/dolce-arty-invoices/invoice_generator.py` con tus datos bancarios.

## 📱 Mantener el bot corriendo 24/7

### Opción 1: PM2 (Recomendado)

```bash
# Instalar PM2
npm install -g pm2

# Iniciar bot con PM2
cd /home/claude/whatsapp-bot
pm2 start bot.js --name dolce-arty-bot

# Ver logs
pm2 logs dolce-arty-bot

# Detener
pm2 stop dolce-arty-bot

# Reiniciar
pm2 restart dolce-arty-bot

# Auto-inicio al reiniciar servidor
pm2 startup
pm2 save
```

### Opción 2: Screen (Alternativa simple)

```bash
# Crear sesión
screen -S dolce-bot

# Iniciar bot
cd /home/claude/whatsapp-bot
node bot.js

# Desconectar (deja corriendo): Ctrl+A, luego D
# Reconectar: screen -r dolce-bot
```

## 🔧 Solución de problemas

### "Error: Cannot find module"
```bash
cd /home/claude/whatsapp-bot
npm install
```

### "QR code expired"
Vuelve a ejecutar `node bot.js` y escanea el nuevo QR rápidamente.

### "Session logged out"
Borra la carpeta `auth_info_baileys` y vuelve a escanear el QR:
```bash
rm -rf auth_info_baileys
node bot.js
```

### El bot no responde
1. Verifica que el bot esté corriendo: `ps aux | grep node`
2. Revisa los logs si usas PM2: `pm2 logs dolce-arty-bot`
3. Reinicia el bot

## 📊 Archivos del sistema

```
/home/claude/
├── whatsapp-bot/
│   ├── bot.js              # Bot principal
│   ├── package.json        # Dependencias
│   ├── invoice_counter.txt # Contador de facturas
│   └── auth_info_baileys/  # Sesión de WhatsApp (generada automáticamente)
│
└── dolce-arty-invoices/
    ├── invoice_generator.py  # Generador de PDF
    └── assets/
        ├── dolce_arty_logo.png
        ├── instagram_logo.png
        └── fondo_patron.png
```

## 🎯 Próximos pasos

Una vez funcionando, puedes:
- ✅ Añadir más comandos (consultar facturas, reportes, etc.)
- ✅ Integrar con base de datos para guardar historial
- ✅ Añadir recordatorios de pago automáticos
- ✅ Exportar reportes mensuales
- ✅ Múltiples usuarios/empleados

## ⚠️ Importante

- **No compartas el QR code** - cualquiera con acceso puede controlar tu WhatsApp
- **Mantén actualizado** el contador de facturas
- **Haz backup** de la carpeta `auth_info_baileys` para no perder la sesión
- **WhatsApp puede banear** si detecta uso automatizado excesivo (aunque es raro)

## 📞 Soporte

Si tienes problemas, revisa:
1. Los logs del bot
2. Que Python y Node.js estén instalados
3. Que los assets estén en la ruta correcta
4. Tu conexión a internet

## 🎨 Creado para Dolce Arty

_Bot desarrollado por Claude para automatizar la generación de facturas de Dolce Arty Art Academy._
