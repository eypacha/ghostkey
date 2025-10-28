# game.py - Lógica del juego principal

import time
from game_over import show_game_over
from core.game_state import GameState
from utils.input_handler import handle_input
from ui.renderer import render_game
from utils.audio import play_tone

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

    # Triada triste descendente al perder
    play_tone(523, 0.18, 0.2)  # C5
    time.sleep(0.1) 
    play_tone(415, 0.18, 0.2)  # G#4
    time.sleep(0.1) 
    play_tone(349, 0.25, 0.2)  # F4
    time.sleep(0.1)  # Pausa breve para asegurar que el último tono termine
    show_game_over(screen)