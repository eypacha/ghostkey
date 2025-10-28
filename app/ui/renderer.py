# renderer.py - Función para dibujar la pantalla del juego Ghostkey

def render_game(game_state):
    screen = game_state.screen
    screen.clear()
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
