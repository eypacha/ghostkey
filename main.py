


from asciimatics.effects import Cycle, Stars
from asciimatics.renderers import FigletText
from asciimatics.scene import Scene
from asciimatics.screen import Screen

from asciimatics.effects import Print, Cycle, Stars
from asciimatics.renderers import FigletText, Rainbow
from asciimatics.scene import Scene
from asciimatics.screen import Screen
from asciimatics.event import KeyboardEvent

def demo(screen):
    effects = [
        Cycle(
            screen,
            FigletText("GHOSTKEY", font='big'),
            int(screen.height / 2 - 8)
        ),
        Print(
            screen,
            Rainbow(screen, FigletText("ENTER TO START", font="small")),
            int(screen.height / 2 + 8)
        ),
        Stars(screen, 200)
    ]
    scene = Scene(effects, 80, name="intro")
    screen.play([scene], stop_on_resize=True, repeat=False)
    # Ya no se espera otro Enter aquí: la animación se detiene con Enter

def show_instructions(screen):
    screen.clear()
    instructions = [
        "GHOSTKEY",
        "",
        "Escribe comandos rápido para limpiar el virus.",
        "ENTER para jugar."
    ]
    y = screen.height // 2 - len(instructions) // 2
    for i, line in enumerate(instructions):
        screen.print_at(line, (screen.width - len(line)) // 2, y + i, colour=7, bg=0)
    screen.refresh()
    while True:
        ev = screen.get_key()
        if ev in (10, 13):
            break

def on_enter(event, screen):
    from asciimatics.event import KeyboardEvent
    if isinstance(event, KeyboardEvent) and event.key_code in (10, 13):
        # Limpiar pantalla y mostrar todo negro
        screen.clear()
        screen.refresh()
        screen.wait_for_input(1)


def main():
    def wrapped(screen):
        demo(screen)
        show_instructions(screen)
        # Aquí irá la lógica del juego
    Screen.wrapper(wrapped)

if __name__ == "__main__":
    main()
