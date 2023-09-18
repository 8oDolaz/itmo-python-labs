from config import RED, BLUE, WHITE, END

def draw_flag() -> None:
    strip_length, flag_length = 7, 5

    flag = []
    for _ in range(flag_length):
        flag.append(f'{BLUE}{" " * strip_length}{WHITE}{" " * strip_length}{RED}{" " * strip_length}{END}')

    print('\n'.join(flag))

if __name__ == '__main__':
    draw_flag()
