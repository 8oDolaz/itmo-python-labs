from time import perf_counter
from random import randint

import numpy as np

def generate_array(length: int = 1_000_000, max_val: int = 100):
    return [
        randint(1, max_val)
        for _ in range(length)
    ]

def main():
    array_start = perf_counter()
    experimental_array = generate_array()
    array_stop = perf_counter()

    default_start = perf_counter()

    product_default = 1
    for elem in experimental_array:
        product_default *= elem

    default_stop = perf_counter()

    numpy_array = np.array(experimental_array)
    numpy_start = perf_counter()

    product_numpy = np.prod(numpy_array)

    numpy_stop = perf_counter()

    print(f'Array generated in {(array_stop - array_start):.3f} second')
    print(f'Numpy multiplied all elemts of array in {(numpy_stop - numpy_start):.3f} seconds')
    print(f'Python for loop did it in {(default_stop - default_start):.3f} seconds')

if __name__ == '__main__':
    main()
