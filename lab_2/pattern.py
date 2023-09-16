from config import WHITE, BLACK, END

import argparse

def draw_pattern(size=3):
    colors = [WHITE, BLACK]

    pattern = []
    for i in range(size):
        color_offset = i % 2
        row = [
            f'{colors[(j + color_offset) % len(colors)]}'
            for j in range(size + 1)
        ]

        pattern.append(f'{" ".join(row)}{END}')
    
    print('\n'.join(pattern))

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-s', '--size', 
        default=3, type=int, help='Pattern square size'
    )

    size = parser.parse_args().size

    draw_pattern(size)
