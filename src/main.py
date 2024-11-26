import argparse
import os

from PIL import Image
import numpy as np

from kernel import get_kernel
from scipy.signal import convolve2d

from threshold import get_threshold_img

import matplotlib.pyplot as plt

parser = argparse.ArgumentParser()

parser.add_argument("-s", "--save", help="file path for saving the outptu")

parser.add_argument("sigma", help="sigma for gaussian", type=float)
parser.add_argument("threshold", help="threshold value", type=float)
parser.add_argument("file_path", help="image file path")


args = parser.parse_args()

sigma = args.sigma
threshold = args.threshold
file_path = args.file_path

save_path = args.save

img = np.array(Image.open(os.path.abspath(file_path)).convert("L")).astype(np.float64)

kernel = get_kernel(sigma)

convolution_output = convolve2d(img, kernel, mode="same")

threshold_img = get_threshold_img(convolution_output, threshold)

plt.imshow(threshold_img, cmap="gray")
plt.axis("off")
plt.tight_layout()
plt.show()

if save_path:
    save_path = os.path.abspath(save_path)
    plt.imsave(save_path, threshold_img, cmap="gray")
