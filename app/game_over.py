# game_over.py - Pantalla de game over

from asciimatics.effects import Cycle, Print
from asciimatics.renderers import FigletText, Rainbow
from asciimatics.scene import Scene

def show_game_over(screen):
    effects = [
        Cycle(
            screen,
            FigletText("GAME OVER", font='big'),
            int(screen.height / 2 - 8)
        ),
        Print(
            screen,
            Rainbow(screen, FigletText("GAME OVER", font="small")),
            int(screen.height / 2 + 8)
        )
    ]
    scene = Scene(effects, 100, name="game_over")
    screen.play([scene], stop_on_resize=True, repeat=False)