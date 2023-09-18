from config import RED, BLUE, WHITE, END

def draw_flag() -> None:
    strip_length, flag_length = 7, 5

    print('\n'.join(
        f'{BLUE}{" " * strip_length}{WHITE}{" " * strip_length}{RED}{" " * strip_length}{END}'
        for _ in range(flag_length)
    ))

if __name__ == '__main__':
    draw_flag()
