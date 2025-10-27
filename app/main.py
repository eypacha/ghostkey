

# main.py - Punto de entrada del juego Ghostkey

from asciimatics.screen import Screen
from intro import demo
from instructions import show_instructions
from game import start_game
from game_over import show_game_over

def main():
    def wrapped(screen):
        demo(screen)
        show_instructions(screen)
        start_game(screen)
    Screen.wrapper(wrapped)

if __name__ == "__main__":
    main()
