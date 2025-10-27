# game.py - Lógica del juego principal

import time
from game_over import show_game_over

def start_game(screen):
    screen.clear()
    word = "GHOST"
    x = screen.width // 2 - len(word) // 2
    y = 0

    while y < screen.height:
        screen.clear()
        screen.print_at(word, x, y, colour=7, bg=0)
        screen.refresh()
        time.sleep(0.1)  # Velocidad de caída
        y += 1

    # Después de que la palabra llegue abajo, mostrar GAME OVER
    show_game_over(screen)