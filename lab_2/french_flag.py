def esc(code):
    return f'\u001b[{code}m'

def draw_flag():
    strip_length, flag_length = 7, 5

    flag = []
    for _ in range(flag_length):
        flag.append(f'{BLUE}{" " * strip_length}{WHITE}{" " * strip_length}{RED}{" " * strip_length}{END}')

    print('\n'.join(flag))

if __name__ == '__main__':
    RED = esc(41)
    BLUE = esc(44)
    WHITE = esc(47)
    END = esc(0)

    draw_flag()
