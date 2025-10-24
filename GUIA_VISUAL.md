# 🎯 Guía VISUAL - Paso a Paso (Con Capturas)

## 📦 Lo que vas a hacer:

1. Descargar ZIP
2. Subir a GitHub (drag & drop)
3. Conectar con Railway
4. Escanear QR
5. ¡Bot funcionando!

---

## PASO 1: Descargar archivos ✅

Ya tienes el archivo: `dolce-arty-bot-github.zip`

---

## PASO 2: Crear cuenta GitHub

### 2.1 Ir a GitHub
```
🌐 https://github.com/signup
```

### 2.2 Llenar formulario
```
📧 Email: tu-email@gmail.com
🔒 Password: (tu contraseña segura)
👤 Username: dolcearty (o el que quieras)
```

### 2.3 Verificar email
```
📨 Revisa tu email
✅ Click en el link de verificación
```

---

## PASO 3: Subir código a GitHub

### 3.1 Crear nuevo repositorio

```
🌐 Ve a: https://github.com/new

📝 Llena:
   Repository name: dolce-arty-bot
   Description: Bot de WhatsApp para facturas
   🔒 Selecciona: Private (IMPORTANTE!)
   
🆗 Click: "Create repository"
```

### 3.2 Subir archivos (Drag & Drop)

En la página que aparece:

```
📝 Verás un texto que dice:
   "...or upload an existing file"
   
👆 Click en "uploading an existing file"

📂 Se abre una página para subir archivos

🗜️  Descomprime el ZIP: dolce-arty-bot-github.zip
    Verás una carpeta: dolce-arty-bot/
    
🎯 ARRASTRA toda la carpeta a GitHub
    O click en "choose your files"
    
⏳ Espera que suban todos (1-2 minutos)

✍️  En el campo "Commit changes":
    Escribe: "Initial commit"
    
✅ Click: "Commit changes"
```

---

## PASO 4: Crear cuenta Railway

### 4.1 Ir a Railway
```
🌐 https://railway.app/
```

### 4.2 Login con GitHub
```
👆 Click: "Login"
👆 Click: "Login with GitHub"
🔐 Autoriza Railway (click "Authorize")
```

---

## PASO 5: Desplegar Bot en Railway

### 5.1 Nuevo Proyecto
```
👆 Click: "+ New Project"
👆 Click: "Deploy from GitHub repo"
```

### 5.2 Primera vez - Configurar GitHub
```
Si es primera vez, verás:
   "Configure GitHub App"
   
👆 Click: "Configure GitHub App"
👆 Selecciona: "Only select repositories"
👆 Busca y selecciona: "dolce-arty-bot"
✅ Click: "Install & Authorize"
```

### 5.3 Seleccionar Repositorio
```
👆 Click en: "dolce-arty-bot"
⏳ Railway empezará a instalar todo (2-3 minutos)

Verás pantalla con:
   "Deploying..."
   "Installing dependencies..."
   "Building..."
```

---

## PASO 6: Ver logs y escanear QR

### 6.1 Esperar deployment
```
⏳ Espera a que diga: "Success"
   (2-3 minutos)
```

### 6.2 Abrir logs
```
👆 Click en tu proyecto (dolce-arty-bot)
👆 Click en "Deployments" (en el menú lateral)
👆 Click en el deployment verde (el activo)
👆 Click en "View Logs" (arriba a la derecha)
```

### 6.3 Encontrar el QR Code
```
📜 Baja en los logs hasta ver:

   🚀 Iniciando bot de WhatsApp...
   📱 Escanea este código QR:
   
   ████████████████████████████
   ██  ▄▄▄  ██▀▄ ▀▀██  ▄▄▄  ██
   ██ █   █ ██▀▄▀ ▄██ █   █ ██
   ██ ▀▄▄▄▀ ██▀▄▀ ▀██ ▀▄▄▄▀ ██
   ████████████████████████████
```

---

## PASO 7: Escanear QR con WhatsApp

### 7.1 Abrir WhatsApp en tu teléfono
```
📱 Abre WhatsApp en tu celular
```

### 7.2 Ir a Dispositivos Vinculados
```
⋮ Toca el menú (3 puntitos arriba a la derecha)
👆 Toca: "Dispositivos vinculados"
```

### 7.3 Vincular dispositivo
```
👆 Toca: "Vincular un dispositivo"
📸 Apunta tu cámara al QR en Railway
✨ ¡Listo! Se vinculará automáticamente
```

### 7.4 Confirmar conexión
```
📜 En los logs de Railway verás:

   ✅ Conectado a WhatsApp!
   🤖 Bot de facturas Dolce Arty activo
   
   📝 Comandos disponibles:
      - "factura [Nombre], [horas] horas"
```

---

## PASO 8: ¡PROBAR EL BOT! 🎉

### 8.1 Enviar mensaje de prueba
```
📱 En WhatsApp, envíate un mensaje a ti mismo:

   "Test Client, 1 hora"
```

### 8.2 Recibir factura
```
⏳ En 5 segundos recibirás:

   ⏳ Generando factura para Test Client...
   
   ✅ Factura #136
   
   👤 Cliente: Test Client
   ⏱️  Servicio: 1 hr. Class, 1 person
   💵 Total: 350.00 DHS
   
   📄 Invoice_136_TestClient.pdf
   [Click para descargar]
```

---

## ✅ CHECKLIST COMPLETO

- [ ] Cuenta GitHub creada
- [ ] Repositorio "dolce-arty-bot" creado (PRIVATE)
- [ ] Archivos subidos a GitHub
- [ ] Cuenta Railway creada
- [ ] GitHub conectado con Railway
- [ ] Proyecto desplegado en Railway
- [ ] Logs abiertos en Railway
- [ ] QR code visible en logs
- [ ] QR escaneado con WhatsApp
- [ ] Mensaje "Conectado a WhatsApp!" en logs
- [ ] Mensaje de prueba enviado
- [ ] PDF recibido ✨

---

## 🎯 URLs Importantes

```
GitHub: https://github.com/
Railway: https://railway.app/
Tus repositorios: https://github.com?tab=repositories
Tus proyectos Railway: https://railway.app/dashboard
```

---

## 🆘 Si algo falla

### QR no aparece
```
1. Espera 3 minutos desde el deploy
2. Refresca la página de logs
3. Si nada, click en "Restart" en Railway
```

### Build failed
```
1. Verifica que subiste TODOS los archivos
2. Incluyendo carpeta "dolce-arty-invoices"
3. Si falta algo, sube los archivos faltantes
```

### Bot no responde
```
1. Ve a logs de Railway
2. Busca errores en rojo
3. Verifica que diga "Conectado a WhatsApp"
4. Re-escanea el QR si es necesario
```

---

## 💡 TIPS

✅ **Repositorio PRIVATE** - Muy importante para seguridad
✅ **Guarda el link de Railway** - Para ver logs cuando quieras
✅ **Screenshot del QR** - Por si se desconecta
✅ **Prueba primero** - Envía mensaje de prueba antes de usar con clientes

---

## 🎉 ¡FELICIDADES!

Tu bot está corriendo 24/7 en la nube.

Ahora solo:
1. Envías mensaje por WhatsApp
2. Recibes PDF
3. ¡Así de simple! ✨

---

**¿Necesitas ayuda? Contáctame con:**
- Screenshot del paso donde te quedaste
- El error que ves (si hay)
- Los logs de Railway
