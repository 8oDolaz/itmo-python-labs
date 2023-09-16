def esc(code):
    return f'\u001b[{code}m'

RED = esc(41)
BLUE = esc(44)
WHITE = esc(47)
BLACK = esc(40)
END = esc(0)
