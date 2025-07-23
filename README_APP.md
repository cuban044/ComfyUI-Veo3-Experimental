# 🎬 Veo 3 Video Generator - Aplicación Web

Una aplicación web interactiva que permite a los usuarios generar videos usando Google Veo 3 directamente desde el navegador, similar a Pika Labs o Imagine Art.

## ✨ Características

- 🎯 **Generación en tiempo real**: Escribe tu prompt y recibe videos instantáneamente
- 🎨 **Interfaz moderna**: Diseño atractivo y fácil de usar
- ⚙️ **Configuración flexible**: Duración, aspecto, generación de personas
- 💡 **Ejemplos incluidos**: Prompts de ejemplo para inspirarte
- 🌐 **Enlace público**: Comparte tu aplicación con otros
- 📱 **Responsive**: Funciona en móviles y tablets

## 🚀 Instalación Rápida

### 1. Clonar el repositorio
```bash
git clone https://github.com/cuban044/ComfyUI-Veo3-Experimental.git
cd ComfyUI-Veo3-Experimental
```

### 2. Instalar dependencias
```bash
pip install -r requirements.txt
```

### 3. Configurar API key
```bash
export GOOGLE_API_KEY=tu_api_key_aqui
```

### 4. Ejecutar la aplicación
```bash
python app.py
```

## 🌐 Opciones de Despliegue

### Opción 1: Local (Recomendado para pruebas)
```bash
python deploy_app.py
# Selecciona opción 1: Ejecutar localmente
```

### Opción 2: Enlace Público (Compartir con otros)
```bash
python deploy_app.py
# Selecciona opción 2: Ejecutar con enlace público
```

### Opción 3: Railway (Despliegue en la nube)
```bash
python deploy_app.py
# Selecciona opción 3: Desplegar en Railway
```

### Opción 4: Heroku (Despliegue en la nube)
```bash
python deploy_app.py
# Selecciona opción 4: Desplegar en Heroku
```

## 🎮 Cómo Usar

### 1. Escribe tu prompt
Describe el video que quieres generar:
```
"Un gato bailando en la luna con estrellas brillantes alrededor"
```

### 2. Configura los parámetros
- **Duración**: 5-8 segundos
- **Aspecto**: 16:9 (horizontal) o 9:16 (vertical)
- **Personas**: Permitir o no generar personas

### 3. Haz clic en "Generar Video"
La aplicación procesará tu solicitud y mostrará el progreso.

### 4. Descarga tu video
Una vez generado, puedes descargar el video directamente.

## 💡 Ejemplos de Prompts

### 🎭 Dramático
```
"Una mujer misteriosa bailando en una tormenta de fuego, vestida con ropas que brillan como estrellas"
```

### 🌍 Naturaleza
```
"Un bosque mágico donde los árboles se mueven como si estuvieran bailando, con luces brillantes flotando"
```

### 🚀 Ciencia Ficción
```
"Una nave espacial futurista volando a través de un cinturón de asteroides con efectos de luz espectaculares"
```

### 🎨 Artístico
```
"Un pintor creando un cuadro que cobra vida, con pinceladas que se convierten en movimiento"
```

### 🐉 Fantasía
```
"Un dragón dorado volando sobre un castillo en las nubes, con rayos de sol atravesando las nubes"
```

## ⚠️ Información Importante

### Costos
- **Google cobra $0.35 por segundo** de video generado
- Un video de 8 segundos cuesta aproximadamente $2.80

### Limitaciones
- **Duración máxima**: 8 segundos
- **Resolución**: 720p a 24 fps
- **Disponibilidad**: Puede no estar disponible en todos los países
- **Tiempo de generación**: Puede tomar varios minutos

### Requisitos
- **API key de Google**: Necesaria para usar Veo 3
- **Conexión a internet**: Para comunicarse con la API de Google
- **Navegador moderno**: Chrome, Firefox, Safari, Edge

## 🔧 Configuración Avanzada

### Variables de Entorno
```bash
export GOOGLE_API_KEY=tu_api_key_aqui
export GRADIO_SERVER_PORT=7860
export GRADIO_SERVER_NAME=0.0.0.0
```

### Personalización
Puedes modificar `app.py` para:
- Cambiar el tema de colores
- Añadir más parámetros
- Modificar la interfaz
- Añadir nuevas funcionalidades

## 🐛 Solución de Problemas

### Error: "API key no configurada"
```bash
export GOOGLE_API_KEY=tu_api_key_aqui
```

### Error: "No se pudo generar el video"
- Verifica que tu prompt sea apropiado
- Intenta con un prompt más simple
- Verifica tu conexión a internet

### Error: "Dependencias faltantes"
```bash
pip install -r requirements.txt
```

## 📞 Soporte

- **Issues**: [GitHub Issues](https://github.com/cuban044/ComfyUI-Veo3-Experimental/issues)
- **Discusiones**: [GitHub Discussions](https://github.com/cuban044/ComfyUI-Veo3-Experimental/discussions)
- **Documentación**: [README principal](README.md)

## 📄 Licencia

Este proyecto está bajo la licencia MIT. Ver [LICENSE](LICENSE) para más detalles.

## 🙏 Agradecimientos

- **Google**: Por proporcionar la API de Veo 3
- **Gradio**: Por el framework de interfaz web
- **ComfyUI**: Por la inspiración del proyecto

---

**¡Disfruta generando videos increíbles con Veo 3! 🎬✨** 