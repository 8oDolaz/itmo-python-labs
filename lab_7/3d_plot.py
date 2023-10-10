from math import pi

import numpy as np
import matplotlib.pyplot as plt

def main():
    ax = plt.axes(projection='3d')

    x_line = np.linspace(-pi, pi, 100)
    y_line = x_line
    z_line = np.tan(x_line)

    ax.plot3D(x_line, y_line, z_line, 'gray')

    plt.show()

if __name__ == '__main__':
    main()
