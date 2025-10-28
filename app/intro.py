from asciimatics.effects import Cycle, Snow, Print
from asciimatics.renderers import FigletText, Rainbow
from asciimatics.scene import Scene


def demo(screen):
    effects = [
        Snow(screen),
        Cycle(screen, FigletText("GHOSTKEY", font="big"), int(screen.height / 2 - 8)),
        Print(
            screen,
            Rainbow(screen, FigletText("ENTER TO START", font="small")),
            int(screen.height / 2 + 8),
        ),
    ]
    scene = Scene(effects, -1, name="intro")  # -1 para duración infinita
    # Mostrar la animación hasta que el usuario presione Enter
    screen.play([scene], stop_on_resize=True, repeat=False)
    # Limpiar el buffer de entrada
    while screen.get_key() is not None:
        pass
    # Esperar Enter para continuar
    while True:
        key = screen.get_key()
        if key in (10, 13):
            break
