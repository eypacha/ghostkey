#!/bin/zsh

# Script para iniciar el juego Ghostkey
echo "Iniciando Ghostkey..."
if [ -f ".venv/bin/python" ]; then
	.venv/bin/python main.py
else
	python3 main.py
fi
