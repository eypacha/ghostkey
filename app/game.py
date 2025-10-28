# game.py - Lógica del juego principal

import time
import random
from game_over import show_game_over
from commands import COMMANDS_LEVEL_1
from game_state import GameState
from input_handler import handle_input

def start_game(screen):
    game_state = GameState(screen)
    game_state.last_time = time.time()

    while game_state.y < screen.height:
        current_time = time.time()
        delta_time = current_time - game_state.last_time
        game_state.last_time = current_time

        # Actualizar posición basada en tiempo transcurrido
        game_state.y += game_state.fall_speed * delta_time

        # Procesar input usando función modular
        handle_input(game_state)

        # Dibujar la pantalla
        screen.clear()
        display_y = int(game_state.y)
        for i, letter in enumerate(game_state.word):
            if i < len(game_state.typed_letters):
                colour = 2  # Verde
            else:
                colour = 7  # Blanco
            screen.print_at(letter, game_state.x + i, display_y, colour=colour, bg=0)
        screen.print_at("Escribe: ", 2, game_state.input_y, colour=7, bg=0)
        screen.print_at(game_state.typed_letters, 11, game_state.input_y, colour=2, bg=0)
        screen.refresh()
        time.sleep(0.01)

    show_game_over(screen)