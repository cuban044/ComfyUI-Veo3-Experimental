# Guía de Despliegue - ComfyUI Veo 3 Experimental

## Preparación para el Despliegue Web

### 1. Actualización del Proyecto ✅

El proyecto ha sido actualizado exitosamente de Veo 2 a Veo 3:

- **API actualizada**: `veo-3.0-generate-001`
- **Nodos renombrados**: Todos los nodos ahora usan el prefijo "Veo3"
- **Dependencias actualizadas**: google-genai >= 0.3.0
- **Workflow actualizado**: Nuevo archivo `Veo3_ComfyUI.json`

### 2. Archivos Creados para el Despliegue

- `package.json`: Configuración del proyecto para npm/yarn
- `deploy_config.json`: Configuración específica para despliegue
- `DEPLOYMENT.md`: Esta guía de despliegue

### 3. Opciones de Despliegue Web

#### Opción A: GitHub Pages (Recomendado)

1. **Crear repositorio en GitHub**:
   ```bash
   git init
   git add .
   git commit -m "Initial commit: ComfyUI Veo 3 Experimental"
   git branch -M main
   git remote add origin https://github.com/yourusername/ComfyUI-Veo3-Experimental.git
   git push -u origin main
   ```

2. **Configurar GitHub Pages**:
   - Ve a Settings > Pages
   - Source: Deploy from a branch
   - Branch: main
   - Folder: / (root)

3. **Crear archivo index.html**:
   ```html
   <!DOCTYPE html>
   <html>
   <head>
       <title>ComfyUI Veo 3 Experimental</title>
       <meta charset="utf-8">
       <meta name="viewport" content="width=device-width, initial-scale=1">
       <style>
           body { font-family: Arial, sans-serif; margin: 40px; }
           .container { max-width: 800px; margin: 0 auto; }
           .download { background: #007bff; color: white; padding: 10px 20px; text-decoration: none; border-radius: 5px; }
       </style>
   </head>
   <body>
       <div class="container">
           <h1>ComfyUI Veo 3 Experimental</h1>
           <p>Extensión de ComfyUI para generación de videos con Google Veo 3</p>
           <a href="https://github.com/yourusername/ComfyUI-Veo3-Experimental/archive/refs/heads/main.zip" class="download">Descargar ZIP</a>
           <h2>Instalación</h2>
           <ol>
               <li>Descarga el archivo ZIP</li>
               <li>Extrae en tu carpeta ComfyUI/custom_nodes/</li>
               <li>Instala dependencias: <code>pip install -r requirements.txt</code></li>
               <li>Configura tu API key de Google en un archivo .env</li>
               <li>Reinicia ComfyUI</li>
           </ol>
       </div>
   </body>
   </html>
   ```

#### Opción B: Netlify

1. **Conectar con GitHub**:
   - Ve a [Netlify](https://netlify.com)
   - Conecta tu cuenta de GitHub
   - Selecciona tu repositorio

2. **Configuración de build**:
   - Build command: `echo "Static site"`
   - Publish directory: `/`

#### Opción C: Vercel

1. **Conectar con GitHub**:
   - Ve a [Vercel](https://vercel.com)
   - Importa tu repositorio de GitHub

2. **Configuración automática**:
   - Vercel detectará automáticamente que es un sitio estático

### 4. Configuración de Dominio Personalizado (Opcional)

1. **Comprar dominio** (ej: comfyui-veo3.com)
2. **Configurar DNS**:
   - Añadir registro CNAME apuntando a tu sitio
3. **Configurar en la plataforma**:
   - Añadir dominio personalizado en GitHub Pages/Netlify/Vercel

### 5. SEO y Metadatos

Actualiza el archivo `index.html` con metadatos SEO:

```html
<meta name="description" content="ComfyUI extension for Google's Veo 3 text-to-video generation">
<meta name="keywords" content="comfyui, veo3, google, ai, video-generation, text-to-video">
<meta name="author" content="Your Name">
<meta property="og:title" content="ComfyUI Veo 3 Experimental">
<meta property="og:description" content="Generate high-quality videos with Google's Veo 3 model">
<meta property="og:type" content="website">
```

### 6. Analytics (Opcional)

Añade Google Analytics o similar:

```html
<!-- Google Analytics -->
<script async src="https://www.googletagmanager.com/gtag/js?id=GA_MEASUREMENT_ID"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'GA_MEASUREMENT_ID');
</script>
```

### 7. Verificación Post-Despliegue

1. **Probar la descarga**: Verifica que el ZIP se descarga correctamente
2. **Probar la instalación**: Instala en un ComfyUI limpio
3. **Probar la funcionalidad**: Genera un video de prueba
4. **Verificar SEO**: Usa herramientas como Google Search Console

### 8. Mantenimiento

- **Actualizaciones regulares**: Mantén las dependencias actualizadas
- **Monitoreo**: Revisa logs y errores regularmente
- **Feedback**: Responde a issues y pull requests

## URLs de Despliegue

Una vez desplegado, tu proyecto estará disponible en:

- **GitHub Pages**: `https://yourusername.github.io/ComfyUI-Veo3-Experimental/`
- **Netlify**: `https://your-project-name.netlify.app/`
- **Vercel**: `https://your-project-name.vercel.app/`
- **Dominio personalizado**: `https://tu-dominio.com/`

## Soporte

Para soporte técnico o preguntas sobre el despliegue:
- Abre un issue en GitHub
- Contacta a través de tu sitio web
- Consulta la documentación en el README.md 