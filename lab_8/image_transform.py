import os
import argparse
from math import ceil

import cv2
import numpy as np

def new_filename(filename: str) -> str:
    name, file_extension = filename.split('.')

    return f'{name}_halftone.{file_extension}'

def segmentize(image: np.ndarray, size: int = 10) -> np.ndarray:
    segments = np.ndarray([])

    for x in range(size, len(image[0]) + size, size):
        for y in range(size, len(image) + size, size):
            segment = image[y - size:y, x - size:x]

            avg_color = int(ceil(np.average(segment)))

            segments = np.append(segments, avg_color)

    return segments

def halftone(image_shape: tuple[int, int], circles: np.ndarray, diameter: int = 10) -> np.ndarray:
    halftone_image = np.zeros(shape=image_shape, dtype=np.uint8)

    circle_index = 0
    for x in range(diameter, image_shape[1] + diameter, diameter):
        for y in range(diameter, image_shape[0] + diameter, diameter):
            circle_diameter = int(ceil(circles[circle_index] * diameter))

            halftone_image = cv2.circle(
                halftone_image,
                (x - diameter // 2, y - diameter // 2),
                circle_diameter,
                WHITE,
                thickness=-1,
            )

            circle_index += 1

    return halftone_image

def main():
    image = cv2.imread(image_filename)
    image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    image_shape = (len(image_gray), len(image_gray[0]))

    segment_size = 10
    image_segments = segmentize(image_gray, size=segment_size)

    circles_diameters = image_segments / 255.0
    halftone_image = halftone(
        image_shape=image_shape,
        circles=circles_diameters,
        diameter=segment_size
    )

    cv2.imwrite(new_filename(image_filename), halftone_image)

if __name__ == '__main__':
    WHITE = (255, 255, 255)

    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-i', '--image', 
        default='variant-1.jpg', type=str, help='Image to halftone'
    )

    base_path = os.getcwd() 
    image_filename = os.path.join(base_path, parser.parse_args().image)

    main()
