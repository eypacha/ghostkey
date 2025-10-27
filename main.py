


from asciimatics.effects import Cycle, Stars
from asciimatics.renderers import FigletText
from asciimatics.scene import Scene
from asciimatics.screen import Screen

def demo(screen):
    from asciimatics.effects import Print
    from asciimatics.renderers import Rainbow
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
    screen.play([Scene(effects, 500)])


def main():
    Screen.wrapper(demo)
    # Aquí irá la lógica del juego

if __name__ == "__main__":
    main()
