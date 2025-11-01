# game_state.py

import random
from .commands import COMMANDS_LEVEL_1


class GameState:
    def __init__(self, screen):
        self.screen = screen
        self.word = random.choice(COMMANDS_LEVEL_1)
        self.typed_letters = ""
        self.x = screen.width // 2 - len(self.word) // 2
        self.y = 0.0
        self.input_y = screen.height - 3
        self.last_time = None
        self.fall_speed = 1
        self.score = 0
        self.level = 1
        self.words_completed = 0
        self.running = True
        self.combo = 0  # Contador de aciertos consecutivos
        self.combo_message = ""  # Mensaje temporal para efectos
        self.combo_timer = 0  # Temporizador para el mensaje (en frames)

    def reset_word(self):
        self.word = random.choice(COMMANDS_LEVEL_1)
        self.typed_letters = ""
        self.x = self.screen.width // 2 - len(self.word) // 2
        self.y = 0.0
