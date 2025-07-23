#!/usr/bin/env python3
"""
Script para desplegar la aplicación Veo 3 Video Generator
"""

import os
import subprocess
import sys

def check_dependencies():
    """Verifica que todas las dependencias estén instaladas"""
    print("🔍 Verificando dependencias...")
    
    required_packages = [
        "gradio",
        "google-genai", 
        "opencv-python",
        "Pillow",
        "torch",
        "numpy"
    ]
    
    missing_packages = []
    
    for package in required_packages:
        try:
            __import__(package.replace("-", "_"))
            print(f"✅ {package}")
        except ImportError:
            missing_packages.append(package)
            print(f"❌ {package} - FALTANTE")
    
    if missing_packages:
        print(f"\n📦 Instalando paquetes faltantes: {', '.join(missing_packages)}")
        subprocess.run([sys.executable, "-m", "pip", "install"] + missing_packages)
    
    return len(missing_packages) == 0

def check_api_key():
    """Verifica que la API key esté configurada"""
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        print("⚠️  ADVERTENCIA: GOOGLE_API_KEY no está configurada")
        print("   Configura tu API key antes de continuar:")
        print("   export GOOGLE_API_KEY=tu_api_key_aqui")
        return False
    else:
        print("✅ API key configurada")
        return True

def run_local():
    """Ejecuta la aplicación localmente"""
    print("🚀 Iniciando aplicación local...")
    print("   La aplicación estará disponible en: http://localhost:7860")
    print("   Presiona Ctrl+C para detener")
    
    try:
        subprocess.run([sys.executable, "app.py"])
    except KeyboardInterrupt:
        print("\n👋 Aplicación detenida")

def run_public():
    """Ejecuta la aplicación con enlace público"""
    print("🌐 Iniciando aplicación con enlace público...")
    print("   Se creará un enlace público que puedes compartir")
    print("   Presiona Ctrl+C para detener")
    
    try:
        # Modificar app.py temporalmente para usar share=True
        with open("app.py", "r") as f:
            content = f.read()
        
        # Asegurar que share=True esté configurado
        if "share=True" not in content:
            content = content.replace("share=False", "share=True")
            with open("app.py", "w") as f:
                f.write(content)
        
        subprocess.run([sys.executable, "app.py"])
    except KeyboardInterrupt:
        print("\n👋 Aplicación detenida")

def deploy_railway():
    """Despliega en Railway"""
    print("🚂 Desplegando en Railway...")
    
    # Crear archivo de configuración para Railway
    railway_config = """
{
  "build": {
    "builder": "nixpacks"
  },
  "deploy": {
    "startCommand": "python app.py",
    "healthcheckPath": "/",
    "healthcheckTimeout": 300,
    "restartPolicyType": "on_failure"
  }
}
"""
    
    with open("railway.json", "w") as f:
        f.write(railway_config)
    
    print("✅ Archivo railway.json creado")
    print("📋 Pasos para desplegar en Railway:")
    print("   1. Ve a https://railway.app")
    print("   2. Conecta tu repositorio de GitHub")
    print("   3. Railway detectará automáticamente la configuración")
    print("   4. Configura la variable de entorno GOOGLE_API_KEY")

def deploy_heroku():
    """Despliega en Heroku"""
    print("🦸 Desplegando en Heroku...")
    
    # Crear Procfile para Heroku
    procfile = "web: python app.py"
    with open("Procfile", "w") as f:
        f.write(procfile)
    
    # Crear runtime.txt
    runtime = "python-3.11.0"
    with open("runtime.txt", "w") as f:
        f.write(runtime)
    
    print("✅ Archivos de Heroku creados")
    print("📋 Pasos para desplegar en Heroku:")
    print("   1. Instala Heroku CLI")
    print("   2. Ejecuta: heroku login")
    print("   3. Ejecuta: heroku create tu-app-name")
    print("   4. Ejecuta: heroku config:set GOOGLE_API_KEY=tu_api_key")
    print("   5. Ejecuta: git push heroku main")

def main():
    """Función principal"""
    print("🎬 Veo 3 Video Generator - Deploy Script")
    print("=" * 50)
    
    # Verificar dependencias
    if not check_dependencies():
        print("❌ Error: No se pudieron instalar las dependencias")
        return
    
    # Verificar API key
    if not check_api_key():
        print("❌ Error: API key no configurada")
        return
    
    print("\n🎯 Opciones de despliegue:")
    print("1. 🏠 Ejecutar localmente")
    print("2. 🌐 Ejecutar con enlace público")
    print("3. 🚂 Desplegar en Railway")
    print("4. 🦸 Desplegar en Heroku")
    print("5. ❌ Salir")
    
    choice = input("\nSelecciona una opción (1-5): ").strip()
    
    if choice == "1":
        run_local()
    elif choice == "2":
        run_public()
    elif choice == "3":
        deploy_railway()
    elif choice == "4":
        deploy_heroku()
    elif choice == "5":
        print("👋 ¡Hasta luego!")
    else:
        print("❌ Opción inválida")

if __name__ == "__main__":
    main() 