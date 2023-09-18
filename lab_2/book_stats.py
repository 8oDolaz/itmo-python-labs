from config import RED, WHITE, END
from config import encoding, round_up

import csv

def count_stats(table_name: str) -> tuple:
    with open(table_name, 'r', encoding=encoding) as csv_file:
        table = csv.reader(csv_file, delimiter=';')
        next(table)

        total_books, new_books, old_books = 0, 0, 0
        for book in table:
            total_books += 1

            book_year = book[6][:book[6].find('-')]
            book_year = int(book_year)

            if book_year < 2014:
                old_books += 1
            else:
                new_books += 1

    new_books_presentege = round_up((new_books / total_books) * 100)
    old_books_presentege = round_up((old_books / total_books) * 100)

    return (new_books_presentege, old_books_presentege)

def draw_plot(precentge: tuple) -> None:
    plot = [
        f'{WHITE}Perc.\t{WHITE}Old Books    New Books{END}'
    ]

    for y in y_axis[1:]:
        row = f'{WHITE}{y}\t{" "}'

        row += f'{RED if precentge[1] >= y else WHITE}{" " * 7}'
        row += f'{WHITE}{" " * 2 * 3}'
        row += f'{RED if precentge[0] >= y else WHITE}{" " * 7}'
        row += f'{WHITE}{" "}{END}'

        plot.append(row)

    print('\n'.join(plot[::-1]))

if __name__ == '__main__':
    y_axis = [i for i in range(0, 101, 10)]

    draw_plot(count_stats('books.csv'))
