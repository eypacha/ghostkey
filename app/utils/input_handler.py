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
                        game_state.score += 1
                        if len(game_state.typed_letters) == len(game_state.word):
                            game_state.words_completed += 1
                            game_state.combo += 1 
                            if game_state.combo > 1:
                                game_state.combo_message = f"Combo x{game_state.combo}!"
                            else:
                                game_state.combo_message = "Correct!"
                            game_state.combo_timer = 30  
                            if game_state.words_completed % 3 == 0:
                                game_state.level += 1
                                game_state.fall_speed += 0.7
                            game_state.reset_word()
                    else:
                        print("\a", end="", flush=True)
                        game_state.combo = 0
        except:
            break
