from config import WHITE, BLACK, END

import os
import sys
import time
import argparse

def frames() -> list[str]:
    frame_1 = f'{WHITE}{" " * 5 * 2}{END}\n' * 2
    frame_1 += f'{WHITE}{" " * 2}{BLACK}{" " * 3 * 2}{WHITE}{" " * 2}{END}\n'
    frame_1 += f'{WHITE}{" " * 5 * 2}{END}\n' * 2

    frame_2 = f'{WHITE}{" " * 5 * 2}{END}\n'
    frame_2 += f'{WHITE}{" " * 2 * 2}{BLACK}{" " * 2}{WHITE}{" " * 2 * 2}{END}\n' * 3
    frame_2 += f'{WHITE}{" " * 5 * 2}{END}\n'

    return [frame_1, frame_2]

def main(animation: list[str], fps: int = 2) -> None:
    frame_index = 0
    while True:
        sys.stdout.write(animation[frame_index])
        sys.stdout.flush()

        time.sleep(fps ** (-1))

        frame_index = (frame_index + 1) % 2

        os.system('clear')

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-f', '--fps', 
        default=2, type=int, help='Frames per second'
    )

    fps = parser.parse_args().fps

    main(frames(), fps)
