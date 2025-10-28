# intro.py - Animación de introducción

from asciimatics.effects import Cycle, Stars, Print
from asciimatics.renderers import FigletText, Rainbow
from asciimatics.scene import Scene


def demo(screen):
    effects = [
        Cycle(screen, FigletText("GHOSTKEY", font="big"), int(screen.height / 2 - 8)),
        Print(
            screen,
            Rainbow(screen, FigletText("ENTER TO START", font="small")),
            int(screen.height / 2 + 8),
        ),
        Stars(screen, 200),
    ]
    scene = Scene(effects, 80, name="intro")
    screen.play([scene], stop_on_resize=True, repeat=False)
    # Ya no se espera otro Enter aquí: la animación se detiene con Enter
