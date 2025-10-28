from asciimatics.effects import Print, Stars
from asciimatics.renderers import FigletText
from asciimatics.scene import Scene


def show_game_over(screen, score=None):
    text = "GAME OVER"
    figlet = FigletText(text, font="big")
    y = screen.height // 2 - 6
    effects = [
        Stars(screen, 200),
        Print(screen, figlet, y, colour=1, speed=0),
    ]
    # Puntaje final en ascii-art si se pasa
    if score is not None:
        score_text = f"SCORE: {score}"
        figlet_score = FigletText(score_text, font="small")
        y_score = y + 8
        effects.append(Print(screen, figlet_score, y_score, colour=3, speed=0))
    scene = Scene(effects, duration=50, name="game_over")  # ~5 segundos a 10 fps
    screen.play([scene], stop_on_resize=True, repeat=False)
