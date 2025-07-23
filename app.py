import gradio as gr
import os
import time
from veo_api import VeoAPI

# Configuración de la API
def get_api_key():
    return os.getenv("GOOGLE_API_KEY")

def generate_video(prompt, duration, aspect_ratio, person_generation):
    """Genera un video usando Veo 3"""
    try:
        # Verificar API key
        api_key = get_api_key()
        if not api_key:
            return None, "❌ Error: API key de Google no configurada. Contacta al administrador."
        
        # Crear instancia de la API
        api = VeoAPI(api_key)
        
        # Mostrar mensaje de progreso
        yield None, "🔄 Generando video con Veo 3... Esto puede tomar varios minutos."
        
        # Generar video
        video_paths = api.generate_video_from_text(
            prompt=prompt,
            duration_seconds=duration,
            aspect_ratio=aspect_ratio,
            person_generation=person_generation,
            number_of_videos=1
        )
        
        if video_paths and len(video_paths) > 0:
            video_path = video_paths[0]
            yield video_path, "✅ ¡Video generado exitosamente!"
        else:
            yield None, "❌ Error: No se pudo generar el video. Verifica tu prompt o intenta de nuevo."
            
    except Exception as e:
        yield None, f"❌ Error: {str(e)}"

# Configuración de la interfaz
def create_interface():
    with gr.Blocks(
        title="🎬 Veo 3 Video Generator",
        theme=gr.themes.Soft(
            primary_hue="blue",
            secondary_hue="purple",
        ),
        css="""
        .gradio-container {
            max-width: 1200px !important;
            margin: 0 auto !important;
        }
        .header {
            text-align: center;
            padding: 20px;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            border-radius: 15px;
            margin-bottom: 20px;
        }
        """
    ) as interface:
        
        # Header
        with gr.Row():
            gr.HTML("""
            <div class="header">
                <h1>🎬 Veo 3 Video Generator</h1>
                <p>Genera videos increíbles con Google Veo 3 usando solo texto</p>
            </div>
            """)
        
        with gr.Row():
            with gr.Column(scale=1):
                # Panel de configuración
                gr.Markdown("### ⚙️ Configuración")
                
                prompt = gr.Textbox(
                    label="📝 Describe tu video",
                    placeholder="Ej: Un gato bailando en la luna con estrellas brillantes alrededor...",
                    lines=4,
                    max_lines=6
                )
                
                with gr.Row():
                    duration = gr.Slider(
                        minimum=5,
                        maximum=8,
                        value=8,
                        step=1,
                        label="⏱️ Duración (segundos)"
                    )
                    
                    aspect_ratio = gr.Dropdown(
                        choices=["16:9", "9:16"],
                        value="16:9",
                        label="📐 Aspecto"
                    )
                
                person_generation = gr.Dropdown(
                    choices=["dont_allow", "allow_adult"],
                    value="dont_allow",
                    label="👤 Generación de personas"
                )
                
                generate_btn = gr.Button(
                    "🎬 Generar Video",
                    variant="primary",
                    size="lg"
                )
                
                # Información importante
                gr.Markdown("""
                ### ⚠️ Información Importante
                - **Costo**: Google cobra $0.35 por segundo de video generado
                - **Tiempo**: La generación puede tomar varios minutos
                - **Calidad**: Videos en 720p a 24 fps
                - **Disponibilidad**: Puede no estar disponible en todos los países
                """)
            
            with gr.Column(scale=1):
                # Panel de resultados
                gr.Markdown("### 🎥 Resultado")
                
                video_output = gr.Video(
                    label="Video Generado",
                    height=400
                )
                
                status_output = gr.Textbox(
                    label="Estado",
                    interactive=False,
                    lines=2
                )
        
        # Ejemplos
        with gr.Accordion("💡 Ejemplos de Prompts", open=False):
            gr.Markdown("""
            ### Prompts de Ejemplo:
            
            **🎭 Dramático:**
            - "Una mujer misteriosa bailando en una tormenta de fuego, vestida con ropas que brillan como estrellas"
            
            **🌍 Naturaleza:**
            - "Un bosque mágico donde los árboles se mueven como si estuvieran bailando, con luces brillantes flotando"
            
            **🚀 Ciencia Ficción:**
            - "Una nave espacial futurista volando a través de un cinturón de asteroides con efectos de luz espectaculares"
            
            **🎨 Artístico:**
            - "Un pintor creando un cuadro que cobra vida, con pinceladas que se convierten en movimiento"
            
            **🐉 Fantasía:**
            - "Un dragón dorado volando sobre un castillo en las nubes, con rayos de sol atravesando las nubes"
            """)
        
        # Evento de generación
        generate_btn.click(
            fn=generate_video,
            inputs=[prompt, duration, aspect_ratio, person_generation],
            outputs=[video_output, status_output],
            show_progress=True
        )
        
        # Ejemplos interactivos
        examples = [
            ["Un gato bailando en la luna con estrellas brillantes alrededor", 8, "16:9", "dont_allow"],
            ["Una mujer misteriosa bailando en una tormenta de fuego", 8, "9:16", "allow_adult"],
            ["Un bosque mágico donde los árboles se mueven como si estuvieran bailando", 6, "16:9", "dont_allow"],
        ]
        
        gr.Examples(
            examples=examples,
            inputs=[prompt, duration, aspect_ratio, person_generation],
            label="🚀 Ejemplos Rápidos"
        )
    
    return interface

# Configuración del servidor
if __name__ == "__main__":
    # Verificar API key
    if not get_api_key():
        print("⚠️  ADVERTENCIA: GOOGLE_API_KEY no está configurada")
        print("   Configura tu API key en las variables de entorno")
        print("   export GOOGLE_API_KEY=tu_api_key_aqui")
    
    # Crear y lanzar la aplicación
    app = create_interface()
    app.launch(
        server_name="0.0.0.0",
        server_port=7860,
        share=True,  # Crear enlace público
        show_error=True,
        title="🎬 Veo 3 Video Generator"
    ) 