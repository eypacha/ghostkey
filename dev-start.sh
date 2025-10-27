#!/bin/zsh

# Script para iniciar el juego Ghostkey
if [ -f ".venv/bin/python" ]; then
	.venv/bin/python app/main.py
else
	python3 app/main.py
fi
