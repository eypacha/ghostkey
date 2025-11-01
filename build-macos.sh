#!/bin/zsh
# Script para compilar Ghostkey para macOS
# Requiere pyinstaller instalado en el entorno actual

# Activar entorno virtual si existe
echo "Activando entorno virtual..."
if [ -d ".venv" ]; then
    source .venv/bin/activate
fi

# Instalar dependencias si es necesario
if [ -f "requirements.txt" ]; then
    echo "Instalando dependencias..."
    pip install -r requirements.txt
fi

# Compilar usando pyinstaller y el spec

echo "Compilando con pyinstaller..."
pyinstaller ghostkey-mac.spec

# Mostrar resultado
if [ -d "build/ghostkey-mac" ]; then
    echo "Compilación exitosa. Ejecutable en build/ghostkey-mac/"
else
    echo "Error en la compilación."
    exit 1
fi
