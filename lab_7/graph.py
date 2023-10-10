import os

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def main():
    table = pd.read_csv(table_file, encoding='windows-1251', sep=';')
    table = table[table.columns[3:5]]
    columns = table.columns

    plt.figure()
    plt.plot(
        table[columns[0]],
        label='Обороты',
        color='red'
    )
    plt.plot(
        table[columns[1]],
        label='Положение заслонки',
        color='blue'
    )
    plt.xlabel('Индекс строки')
    plt.ylabel('Значения')
    plt.legend()

    plt.figure()
    plt.scatter(
        x=table[columns[0]],
        y=table[columns[1]],
    )
    plt.xlabel(columns[0])
    plt.ylabel(columns[1])

    plt.show()

if __name__ == '__main__':
    base_path = os.path.dirname(os.path.realpath(__file__))
    table_file = os.path.join(base_path, 'data1.csv')

    main()
