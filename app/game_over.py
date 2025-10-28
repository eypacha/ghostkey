# game_over.py - Pantalla de game over

from asciimatics.effects import Cycle, Print
from asciimatics.renderers import FigletText, Rainbow
from asciimatics.scene import Scene

def show_game_over(screen):
    screen.clear()
    text = "GAME OVER"
    x = screen.width // 2 - len(text) // 2
    y = screen.height // 2
    screen.print_at(text, x, y, colour=1)
    msg = "Presiona cualquier tecla para salir..."
    screen.print_at(msg, screen.width // 2 - len(msg) // 2, y + 2, colour=7)
    screen.refresh()
    screen.get_key()