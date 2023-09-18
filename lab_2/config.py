from math import ceil

def esc(code: int) -> str:
    return f'\u001b[{code}m'

def round_up(x: float) -> int:
    return ceil(x / 10.0) * 10

RED = esc(41)
BLUE = esc(44)
WHITE = esc(47)
BLACK = esc(40)
END = esc(0)

encoding = 'Windows-1251'
