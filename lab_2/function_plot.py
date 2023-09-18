from config import WHITE, RED, END
from config import round_up

def func(x: int) -> float:
    return x ** 2

def func_values() -> list[list[int]]:
    return [
        [x, round_up(func(x))]
        for x in range(1, 10)
    ]

def draw_plot(values: list[list[int]]) -> None:
    plot = [
        f'{WHITE}{y_axis[0]}\t {WHITE}{" ".join(str(x[0]) for x in values)}{END}'
    ]

    for y in y_axis[1:]:
        row = f'{WHITE}{y}\t' + ''.join(
            (RED if pixel == y else WHITE) + " " * 2
            for _, pixel in values
        ) + END

        plot.append(row)

    print('\n'.join(plot[::-1]))

if __name__ == '__main__':
    y_axis = [i for i in range(0, 91, 10)]

    draw_plot(func_values())
