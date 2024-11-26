#!/usr/bin/env python

import os
import sys
import numpy as np
import math

from PIL import Image
from scipy.signal import convolve2d
import matplotlib.pyplot as plt

if len(sys.argv) < 3:
    print(f"USAGE: {sys.argv[0]} <sigma value> <relative image path> <threshold>")
    exit(1)

try:
    sigma = float(sys.argv[1])
except ValueError:
    print("invalid sigma")
    exit(1)

try:
    threshold = float(sys.argv[2])
except ValueError:
    print("invalid threshold")
    exit(1)

file_path = sys.argv[3]

absolute_path = os.path.abspath(file_path)

absolute_save_path = ""
if len(sys.argv) >= 5:
    absolute_save_path = os.path.abspath(sys.argv[4])

if not os.path.isfile(absolute_path):
    print("image file does not exist")
    exit(1)

kernel_half_width = math.floor(3 * sigma)

meshgrid_coordinates = (
    np.array([i for i in range(0, (2 * kernel_half_width) + 1)]) - kernel_half_width
)

kernel_X, kernel_Y = np.meshgrid(meshgrid_coordinates, meshgrid_coordinates)

img = np.array(Image.open(absolute_path).convert("L")).astype(np.float64)

sigma_sq = sigma * sigma

gaussian = (1 / (2 * math.pi * sigma_sq)) * np.exp(
    -1 * (np.square(kernel_X) + np.square(kernel_Y)) / (2 * sigma_sq)
).astype(np.float64)

kernel = (
    (1 / sigma_sq)
    * (((np.square(kernel_X) + np.square(kernel_Y)) / sigma_sq) - 2)
    * gaussian
)

conv = convolve2d(img, kernel, mode="same")

threshold_image = np.zeros_like(conv)


def check_threshold(a: float, b: float, threshold: float) -> bool:
    return (a > threshold and b < -threshold) or (a < -threshold and b > threshold)


for y in range(threshold_image.shape[0]):
    for x in range(threshold_image.shape[1]):
        if (x - 1) >= 0:
            if check_threshold(conv[y, x], conv[y, x - 1], threshold):
                threshold_image[y, x] = 255
                continue
        elif (x + 1) < threshold_image.shape[1]:
            if check_threshold(conv[y, x], conv[y, x + 1], threshold):
                threshold_image[y, x] = 255
                continue
        elif (y - 1) >= 0:
            if check_threshold(conv[y, x], conv[y - 1, x], threshold):
                threshold_image[y, x] = 255
                continue
        elif (y + 1) < threshold_image.shape[0]:
            if check_threshold(conv[y, x], conv[y + 1, x], threshold):
                threshold_image[y, x] = 255
                continue
        elif (y + 1) < threshold_image.shape[0] and (x + 1) < threshold_image.shape[1]:
            if check_threshold(conv[y, x], conv[y + 1, x + 1], threshold):
                threshold_image[y, x] = 255
                continue
        elif (y - 1) < 0 and (x - 1) < 0:
            if check_threshold(conv[y, x], conv[y - 1, x - 1], threshold):
                threshold_image[y, x] = 255
                continue
        elif (y + 1) < threshold_image.shape[0] and (x - 1) < 0:
            if check_threshold(conv[y, x], conv[y + 1, x - 1], threshold):
                threshold_image[y, x] = 255
                continue
        elif (y - 1) < 0 and (x + 1) < threshold_image.shape[1]:
            if check_threshold(conv[y, x], conv[y - 1, x + 1], threshold):
                threshold_image[y, x] = 255
                continue

plt.imshow(threshold_image, cmap="gray")
plt.show()

if absolute_save_path:
    plt.imsave(absolute_save_path, threshold_image, cmap="gray")

# out_img = Image.fromarray(threshold_image.astype(np.uint8), mode="L")
# out_img.show()
