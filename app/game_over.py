# game_over.py

from asciimatics.effects import Cycle, Print
from asciimatics.renderers import FigletText, Rainbow
from asciimatics.scene import Scene

from asciimatics.renderers import FigletText

def show_game_over(screen, score=None):
    screen.clear()
    text = "GAME OVER"
    figlet = FigletText(text, font="big")
    y = screen.height // 2 - 6

    lines = []
    rendered = figlet.rendered_text
    if isinstance(rendered, str):
        lines = rendered.splitlines()
    elif isinstance(rendered, (tuple, list)):
        for part in rendered:
            if isinstance(part, str):
                lines.extend(part.splitlines())
            elif isinstance(part, (tuple, list)):
                for subpart in part:
                    if isinstance(subpart, str):
                        lines.extend(subpart.splitlines())
    for i, line in enumerate(lines):
        screen.print_at(line, screen.width // 2 - len(line) // 2, y + i, colour=1)

    # Puntaje final en ascii-art si se pasa
    if score is not None:
        score_text = f"SCORE: {score}"
        figlet_score = FigletText(score_text, font="small")
        y_score = y + 8
        score_lines = []
        rendered_score = figlet_score.rendered_text
        if isinstance(rendered_score, str):
            score_lines = rendered_score.splitlines()
        elif isinstance(rendered_score, (tuple, list)):
            for part in rendered_score:
                if isinstance(part, str):
                    score_lines.extend(part.splitlines())
                elif isinstance(part, (tuple, list)):
                    for subpart in part:
                        if isinstance(subpart, str):
                            score_lines.extend(subpart.splitlines())
        for i, line in enumerate(score_lines):
            screen.print_at(line, screen.width // 2 - len(line) // 2, y_score + i, colour=3)

    import time
    screen.refresh()
    time.sleep(3)