# input_handler.py - Función para manejar el input del usuario en Ghostkey

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
                            # Cada 3 palabras, subir de nivel y aumentar velocidad
                            if game_state.words_completed % 3 == 0:
                                game_state.level += 1
                                game_state.fall_speed += 0.7  # Aumenta la velocidad
                            game_state.reset_word()
                    else:
                        print('\a', end='', flush=True)  # Bell terminal al equivocarse
        except:
            break
