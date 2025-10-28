# game.py - Lógica del juego principal

import time
import random
from game_over import show_game_over
from commands import COMMANDS_LEVEL_1

def start_game(screen):
    screen.clear()
    word = random.choice(COMMANDS_LEVEL_1)  # Seleccionar comando aleatorio
    typed_letters = ""  # Letras que el usuario ya tipeó correctamente
    x = screen.width // 2 - len(word) // 2
    y = 0.0  # Usar float para posición más precisa

    # Área de input en la parte inferior
    input_y = screen.height - 3
    screen.print_at("Escribe: ", 2, input_y, colour=7, bg=0)

    last_time = time.time()
    fall_speed = 2  # Velocidad de caída (caracteres por segundo)

    while y < screen.height:
        current_time = time.time()
        delta_time = current_time - last_time
        last_time = current_time

        # Actualizar posición basada en tiempo transcurrido
        y += fall_speed * delta_time

        # Procesar input continuamente
        import select
        import sys
        while select.select([sys.stdin], [], [], 0)[0]:
            try:
                key = screen.get_key()
                if key:
                    char = chr(key)
                    expected_index = len(typed_letters)
                    if expected_index < len(word):
                        # Permitir cualquier caracter, no solo letras
                        if char == word[expected_index]:
                            typed_letters += char
                            # Si completó la palabra, resetear para la siguiente
                            if len(typed_letters) == len(word):
                                word = random.choice(COMMANDS_LEVEL_1)
                                typed_letters = ""
                                x = screen.width // 2 - len(word) // 2
                                y = 0.0  # Resetear posición de la palabra
            except:
                break

        # Dibujar la pantalla
        screen.clear()

        # Mostrar la palabra cayendo con colores
        display_y = int(y)  # Convertir a int para display
        for i, letter in enumerate(word):
            if i < len(typed_letters):
                # Letra tipeada correctamente - verde
                colour = 2  # Verde
            else:
                # Letra pendiente - blanco
                colour = 7  # Blanco
            screen.print_at(letter, x + i, display_y, colour=colour, bg=0)

        # Mostrar input del usuario
        screen.print_at("Escribe: ", 2, input_y, colour=7, bg=0)
        screen.print_at(typed_letters, 11, input_y, colour=2, bg=0)  # Verde para lo tipeado

        screen.refresh()

        # Pequeña pausa para no consumir CPU al 100%
        time.sleep(0.01)

    # Si llegó aquí, la palabra llegó abajo sin completarse
    show_game_over(screen)