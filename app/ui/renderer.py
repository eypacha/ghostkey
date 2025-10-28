from asciimatics.renderers import FigletText

# renderer.py - Función para dibujar la pantalla del juego Ghostkey

def render_game(game_state):
    screen = game_state.screen
    screen.clear()
    # Mostrar puntaje arriba a la derecha en amarillo (color 3)
    score_text = f"Score: {game_state.score}"
    # Usar FigletText para un efecto ascii si hay espacio suficiente
    if screen.width > 40:
        # PUNTOS
        figlet = FigletText(str(game_state.score), font="digital")
        rendered = figlet.rendered_text
        lines = []
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
        lines = [line for line in lines if isinstance(line, str) and line.strip() and line.strip().upper() != 'NONE']
        # Escribir "POINTS" encima del puntaje
        points_label = "POINTS"
        screen.print_at(points_label, screen.width - len(points_label) - 2, 1, colour=3, bg=0)
        for i, text in enumerate(lines):
            screen.print_at(text, screen.width - len(text) - 2, 2 + i, colour=3, bg=0)
        # NIVEL
        level_figlet = FigletText(str(game_state.level), font="digital")
        level_lines = []
        rendered_level = level_figlet.rendered_text
        if isinstance(rendered_level, str):
            level_lines = rendered_level.splitlines()
        elif isinstance(rendered_level, (tuple, list)):
            for part in rendered_level:
                if isinstance(part, str):
                    level_lines.extend(part.splitlines())
                elif isinstance(part, (tuple, list)):
                    for subpart in part:
                        if isinstance(subpart, str):
                            level_lines.extend(subpart.splitlines())
        level_lines = [line for line in level_lines if isinstance(line, str) and line.strip() and line.strip().upper() != 'NONE']
        nivel_label = "LEVEL"
        screen.print_at(nivel_label, screen.width - len(nivel_label) - 2, 2 + len(lines), colour=3, bg=0)
        for i, text in enumerate(level_lines):
            screen.print_at(text, screen.width - len(text) - 2, 3 + len(lines) + i, colour=3, bg=0)
    else:
        screen.print_at(score_text, screen.width - len(score_text) - 2, 1, colour=3, bg=0)
    display_y = int(game_state.y)
    for i, letter in enumerate(game_state.word):
        if i < len(game_state.typed_letters):
            colour = 2  # Verde
        else:
            colour = 7  # Blanco
        screen.print_at(letter, game_state.x + i, display_y, colour=colour, bg=0)
    screen.print_at("Escribe: ", 2, game_state.input_y, colour=7, bg=0)
    screen.print_at(game_state.typed_letters, 11, game_state.input_y, colour=2, bg=0)
    screen.refresh()
