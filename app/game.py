# game.py - Lógica del juego principal

import time
from game_over import show_game_over
from core.game_state import GameState
from utils.input_handler import handle_input
from ui.renderer import render_game

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
        render_game(game_state)
        time.sleep(0.01)

    # Mostrar pantalla de game over con puntaje final
    show_game_over(screen, score=game_state.score)