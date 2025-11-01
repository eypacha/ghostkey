# input_handler.py

import select
import sys


def handle_input(game_state):
    """
    Procesa el input del usuario y actualiza el estado del juego.
    """
    while select.select([sys.stdin], [], [], 0)[0]:
        try:
            key = game_state.screen.get_key()
            if key:
                char = chr(key)
                expected_index = len(game_state.typed_letters)
                if expected_index < len(game_state.word):
                    if char == game_state.word[expected_index]:
                        game_state.typed_letters += char
                        game_state.score += 1  # Sumar 1 punto por cada letra correcta
                        # Si completó la palabra, resetear
                        if len(game_state.typed_letters) == len(game_state.word):
                            game_state.words_completed += 1
                            game_state.combo += 1  # Incrementar combo
                            # Efecto de combo: mostrar mensaje
                            if game_state.combo > 1:
                                game_state.combo_message = f"Combo x{game_state.combo}!"
                            else:
                                game_state.combo_message = "Correct!"
                            game_state.combo_timer = 30  # Mostrar por 30 frames (~0.3 segundos)
                            # Cada 3 palabras, subir de nivel y aumentar velocidad
                            if game_state.words_completed % 3 == 0:
                                game_state.level += 1
                                game_state.fall_speed += 0.7  # Aumenta la velocidad
                            game_state.reset_word()
                    else:
                        print("\a", end="", flush=True)  # Bell terminal al equivocarse
                        game_state.combo = 0  # Resetear combo al equivocarse
        except:
            break
