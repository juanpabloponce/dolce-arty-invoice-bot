# ☁️ Desplegar Bot en Railway (SIN instalar nada)

## 🎯 Lo que necesitas:
- ✅ Una cuenta de GitHub (gratis)
- ✅ Una cuenta de Railway (gratis)
- ✅ 10 minutos de tu tiempo

## 📝 Paso a Paso (MUY FÁCIL)

### 1️⃣ Crear cuenta en GitHub (si no tienes)

1. Ve a: https://github.com/signup
2. Crea tu cuenta (email, contraseña, etc.)
3. Verifica tu email
4. ¡Listo!

---

### 2️⃣ Subir el código a GitHub

**Opción A - Interfaz Web (Más fácil):**

1. Ve a: https://github.com/new
2. Repository name: `dolce-arty-bot`
3. Hazlo **Private** ✅ (importante para tu seguridad)
4. Click "Create repository"
5. En la página siguiente, click en **"uploading an existing file"**
6. **Arrastra y suelta** todos los archivos de la carpeta `whatsapp-bot/`
7. También arrastra la carpeta completa `dolce-arty-invoices/`
8. Click "Commit changes"

**Opción B - Con GitHub Desktop (También fácil):**

1. Descarga GitHub Desktop: https://desktop.github.com/
2. Instala y conecta con tu cuenta
3. File → Add Local Repository
4. Selecciona la carpeta con los archivos
5. Publish repository

---

### 3️⃣ Crear cuenta en Railway

1. Ve a: https://railway.app/
2. Click **"Login"**
3. Selecciona **"Login with GitHub"**
4. Autoriza Railway
5. ¡Listo!

---

### 4️⃣ Desplegar el Bot

1. En Railway, click **"New Project"**
2. Selecciona **"Deploy from GitHub repo"**
3. Si es primera vez, click **"Configure GitHub App"**
4. Selecciona tu repositorio: `dolce-arty-bot`
5. Click **"Deploy Now"**

⏳ Railway instalará todo automáticamente (2-3 minutos)

---

### 5️⃣ Ver los logs y escanear QR

1. En Railway, click en tu proyecto
2. Ve a la pestaña **"Deployments"**
3. Click en el deployment activo
4. Ve a **"View Logs"**
5. Verás el código QR en los logs:

```
🚀 Iniciando bot de WhatsApp...
📱 Escanea este código QR:

[QR CODE aquí]
```

6. **Escanea el QR** con WhatsApp:
   - Abre WhatsApp
   - Menú → Dispositivos vinculados
   - Vincular un dispositivo
   - Escanea el QR

7. Verás:
```
✅ Conectado a WhatsApp!
🤖 Bot activo
```

---

### 6️⃣ ¡Probar el Bot!

Envíate un WhatsApp:
```
Maria Lopez, 2 horas
```

El bot responderá en 5 segundos con el PDF! 🎉

---

## 💰 ¿Cuánto cuesta?

### Railway - Plan Gratuito:
- ✅ **$5 USD de crédito GRATIS cada mes**
- ✅ Tu bot consume ~$1-2 USD/mes
- ✅ **Prácticamente GRATIS** para tu uso

Si se te acaba el crédito gratuito:
- Plan Hobby: $5 USD/mes (suficiente)

---

## 🔄 Actualizar el bot

Si necesitas cambiar algo:

1. Edita los archivos en GitHub (botón "Edit")
2. Commit changes
3. Railway **re-despliega automáticamente**
4. ¡Listo!

---

## 📊 Monitorear

En Railway puedes ver:
- ✅ Logs en tiempo real
- ✅ Cuánta memoria usa
- ✅ Si hay errores
- ✅ Cuánto crédito te queda

---

## 🔧 Solución de Problemas

### El QR no aparece en los logs
1. Espera 2-3 minutos después del deploy
2. Refresca la página de logs
3. Si nada, ve a Settings → Restart

### "Build failed"
1. Verifica que subiste TODOS los archivos
2. Incluyendo la carpeta `dolce-arty-invoices/`
3. Y todos los archivos: bot.js, package.json, etc.

### El bot no responde
1. Ve a los Logs
2. Busca el mensaje "✅ Conectado a WhatsApp"
3. Si no está, re-escanea el QR

---

## 🎯 Ventajas de Railway

✅ **Corre 24/7** - No necesitas tener tu computadora prendida
✅ **Gratis** - $5 USD/mes de crédito gratuito
✅ **Fácil** - Solo drag & drop
✅ **Logs** - Puedes ver todo lo que pasa
✅ **Automático** - Se reinicia si hay algún problema

---

## 📱 Flujo Final

```
Tú subes código a GitHub (1 vez)
   ↓
Railway lo despliega (automático)
   ↓
Escaneas QR con WhatsApp (1 vez)
   ↓
Bot corre 24/7 en la nube
   ↓
Envías mensaje por WhatsApp
   ↓
Bot responde con PDF
   ↓
¡Magia! ✨
```

---

## 🆘 ¿Necesitas ayuda?

Contáctame con:
1. Screenshot del error
2. Los últimos logs de Railway
3. En qué paso te quedaste

---

## 🎉 ¡Listo!

Una vez configurado, solo:
1. Envías mensaje por WhatsApp
2. Recibes PDF
3. ¡Así de simple!

No necesitas tocar nada más. El bot corre solo en la nube. 🚀
