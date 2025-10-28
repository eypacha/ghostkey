# game_state.py - Clase para manejar el estado del juego Ghostkey

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
        self.fall_speed = 2  # caracteres por segundo
        self.score = 0
        self.level = 1
        self.running = True

    def reset_word(self):
        self.word = random.choice(COMMANDS_LEVEL_1)
        self.typed_letters = ""
        self.x = self.screen.width // 2 - len(self.word) // 2
        self.y = 0.0
