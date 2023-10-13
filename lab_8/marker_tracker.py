import os
import argparse

import cv2
import numpy as np

def detect_marker(detector: cv2.aruco.ArucoDetector, image: np.ndarray) -> np.ndarray:
    marker_corners, _, _ = detector.detectMarkers(image)
    marker_corners = marker_corners[0]
    marker_corners = marker_corners.astype(int)

    return marker_corners[0]

def draw_marker(image: np.ndarray, cords: tuple) -> np.ndarray:
    cv2.rectangle(
        image,
        pt1=(0, 0),
        pt2=(400, 100),
        color=WHITE,
        thickness=-1
    )
    cv2.putText(
        image,
        text=f'x_1, y_1: {tuple(cords[0])}; x_2, y_2: {tuple(cords[1])}',
        org=(10, 50),
        fontFace=cv2.FONT_ITALIC,
        fontScale=0.5,
        color=RED
    )

    cv2.rectangle(
        image,
        pt1=cords[0],
        pt2=cords[1],
        color=RED,
        thickness=2
    )

    return image

def main():
    aruco_dict = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_4X4_100)
    aruco_params = cv2.aruco.DetectorParameters()
    detector = cv2.aruco.ArucoDetector(aruco_dict, aruco_params)

    image = cv2.imread(image_filename)

    marker_cords = detect_marker(detector, image)

    image = draw_marker(image, (marker_cords[0], marker_cords[-2]))

    cv2.imwrite('detected_marker.png', image)

if __name__ == '__main__':
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    RED = (0, 0, 255)

    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-i', '--image', 
        default='photo_with_marker.jpg', type=str, help='Image to halftone'
    )

    base_path = os.getcwd() 
    image_filename = os.path.join(base_path, parser.parse_args().image)

    main()
