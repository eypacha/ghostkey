# Ghostkey

Ghostkey es un juego de terminal hecho en Python.

## Cómo ejecutar

```bash
python main.py
```

## Descripción

- Al iniciar, el juego muestra el título "GHOSTKEY" en la terminal.
- Luego hay instrucciones donde explica que hay que tipear palabras
- empeizan a aparecer una palabra que baja de arriba a abajo y hay que tipear antes de que llegue abajo
- Incluye pantalla de "GAME OVER" con efectos visuales

## Pantallas disponibles

- `intro.py`: Animación de introducción con título
- `instructions.py`: Pantalla de instrucciones
- `game.py`: Lógica del juego con palabras cayendo
- `game_over.py`: Pantalla de fin de juego con efectos dramáticos


## Compilar ejecutable para macOS

1. Asegúrate de tener un entorno virtual y dependencias instaladas:
	```sh
	python3 -m venv .venv
	source .venv/bin/activate
	pip install -r requirements.txt
	```
2. Ejecuta el script de compilación:
	```sh
	./build-macos.sh
	```
3. El ejecutable se generará en:
	```sh
	dist/ghostkey-mac
	```
	Puedes ejecutarlo con:
	```sh
	./dist/ghostkey-mac
	```

## Compilar ejecutable para Windows (desde macOS)

1. Instala Wine y PyInstaller para Windows si no los tienes.
2. Ejecuta el script:
	```sh
	./build-windows.sh
	```
3. El ejecutable se generará en:
	```sh
	dist/windows/ghostkey-win.exe
	```
	Puedes transferirlo y ejecutarlo en una PC con Windows.

## Requisitos
- Python 3.x
