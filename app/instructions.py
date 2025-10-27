# instructions.py - Pantalla de instrucciones

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
