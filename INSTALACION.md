# 🚀 Guía de Instalación - Bot WhatsApp Dolce Arty

## ⚡ Instalación Rápida (5 minutos)

### Paso 1: Descargar archivos

Ya tienes el archivo: `dolce-arty-whatsapp-bot.tar.gz`

### Paso 2: Descomprimir

**En Windows:**
- Descarga e instala 7-Zip: https://www.7-zip.org/
- Click derecho en el archivo → 7-Zip → Extract Here

**En Mac/Linux:**
```bash
tar -xzf dolce-arty-whatsapp-bot.tar.gz
cd whatsapp-bot
```

### Paso 3: Instalar Node.js

**Windows/Mac:**
1. Ve a: https://nodejs.org/
2. Descarga la versión LTS (recomendada)
3. Instala normalmente (siguiente, siguiente, siguiente)
4. Reinicia tu computadora

**Verificar instalación:**
```bash
node --version
# Debe mostrar algo como: v20.x.x
```

### Paso 4: Instalar dependencias

Abre la terminal/CMD en la carpeta `whatsapp-bot`:

```bash
npm install
```

⏳ Esto tomará 1-2 minutos. Verás muchos mensajes, es normal.

### Paso 5: Instalar Python y reportlab

**Ya tienes Python instalado?** Verifica:
```bash
python3 --version
# o en Windows:
python --version
```

**Si NO tienes Python:**
- Windows: https://www.python.org/downloads/
- Mac: Ya viene instalado
- Linux: `sudo apt install python3 python3-pip`

**Instalar reportlab:**
```bash
pip install reportlab
# o en algunos sistemas:
pip3 install reportlab
```

### Paso 6: Iniciar el bot 🎉

```bash
node bot.js
```

Verás algo así:
```
🚀 Iniciando bot de WhatsApp Dolce Arty...

📱 Escanea este código QR con WhatsApp:

[QR CODE aparece aquí]
```

### Paso 7: Escanear QR Code

1. Abre WhatsApp en tu teléfono
2. Ve a: **Menú (⋮) → Dispositivos vinculados**
3. Toca **"Vincular un dispositivo"**
4. Escanea el QR que aparece en tu terminal

✅ Cuando veas:
```
✅ Conectado a WhatsApp!
🤖 Bot de facturas Dolce Arty activo
```

¡Ya está funcionando!

---

## 💬 Cómo usar el bot

### Envíate un mensaje de WhatsApp (o pídele a alguien que te escriba):

```
Maria Lopez, 2 horas
```

### El bot responderá:

```
⏳ Generando factura para Maria Lopez...

✅ Factura #140

👤 Cliente: Maria Lopez
⏱️ Servicio: 2 hrs. Class, 1 person
💵 Total: 700.00 DHS

[Adjunta el PDF]
```

### Otros formatos válidos:

```
factura Ana Garcia, 1 hora
invoice John Smith, 3 hours
Pedro Martinez, 1.5 hrs
```

### Ver ayuda:

```
help
```

---

## 🔧 Solución de Problemas

### Error: "Cannot find module"
```bash
cd whatsapp-bot
npm install
```

### Error: "python3 not found"
En Windows, usa:
```bash
python bot.js
# en lugar de
python3 bot.js
```

### El QR code expiró
Simplemente presiona `Ctrl+C` para detener el bot y vuelve a ejecutar:
```bash
node bot.js
```

### "Session logged out"
Borra la carpeta de sesión y reconecta:
```bash
rm -rf auth_info_baileys
node bot.js
```

### El bot no responde a mis mensajes
1. Verifica que el bot esté corriendo (no debe haber errores en la terminal)
2. Asegúrate de que escaneaste el QR correctamente
3. Prueba enviando "help"

---

## 🎯 Mantener el bot corriendo 24/7

### Opción 1: Dejar la terminal abierta
- Simplemente no cierres la ventana de terminal/CMD
- Funciona mientras tu computadora esté encendida

### Opción 2: PM2 (Recomendado para servidores)
```bash
npm install -g pm2
pm2 start bot.js --name dolce-bot
pm2 logs dolce-bot  # Ver logs
pm2 stop dolce-bot  # Detener
pm2 restart dolce-bot  # Reiniciar
```

---

## 📋 Checklist de instalación

- [ ] Node.js instalado (`node --version` funciona)
- [ ] Python instalado (`python3 --version` funciona)
- [ ] Reportlab instalado (`pip list | grep reportlab`)
- [ ] Dependencias npm instaladas (`npm install` completado)
- [ ] Bot iniciado (`node bot.js` sin errores)
- [ ] QR escaneado con WhatsApp
- [ ] Bot respondió "Conectado a WhatsApp!"
- [ ] Probaste enviando un mensaje de prueba

---

## 💡 Tips

1. **Primer mensaje de prueba:** Envíate "help" para verificar que funciona
2. **Número de factura:** El bot comienza en 137, edita `bot.js` línea 10 para cambiar
3. **Backup:** Guarda la carpeta `auth_info_baileys` para no tener que re-escanear el QR
4. **Múltiples usuarios:** Cualquier persona que te escriba puede generar facturas

---

## 🆘 ¿Necesitas ayuda?

Si algo no funciona, envíame:
1. El mensaje de error completo
2. Tu sistema operativo (Windows/Mac/Linux)
3. La versión de Node.js (`node --version`)

---

## 🎨 ¡Disfruta tu bot!

Ahora puedes generar facturas profesionales desde WhatsApp en segundos.
