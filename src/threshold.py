import numpy as np
import numpy.typing as npt


def check(center_value: float, offset_value: float, threshold: float) -> bool:
    return (center_value > threshold and offset_value < -threshold) or (
        center_value < -threshold and offset_value > threshold
    )


def get_threshold_img(
    convolution_output: npt.NDArray[np.float64], threshold: float
) -> npt.NDArray[np.uint8]:
    height, width = convolution_output.shape
    threshold_image = np.zeros_like(convolution_output).astype(np.uint8)
    for y in range(height):
        for x in range(width):
            if (x - 1) >= 0:
                if check(
                    convolution_output[y, x], convolution_output[y, x - 1], threshold
                ):
                    threshold_image[y, x] = 255
                    continue
            elif (x + 1) < width:
                if check(
                    convolution_output[y, x], convolution_output[y, x + 1], threshold
                ):
                    threshold_image[y, x] = 255
                    continue
            elif (y - 1) >= 0:
                if check(
                    convolution_output[y, x], convolution_output[y - 1, x], threshold
                ):
                    threshold_image[y, x] = 255
                    continue
            elif (y + 1) < height:
                if check(
                    convolution_output[y, x], convolution_output[y + 1, x], threshold
                ):
                    threshold_image[y, x] = 255
                    continue
            elif (y + 1) < height and (x + 1) < threshold_image.shape[1]:
                if check(
                    convolution_output[y, x],
                    convolution_output[y + 1, x + 1],
                    threshold,
                ):
                    threshold_image[y, x] = 255
                    continue
            elif (y - 1) < 0 and (x - 1) < 0:
                if check(
                    convolution_output[y, x],
                    convolution_output[y - 1, x - 1],
                    threshold,
                ):
                    threshold_image[y, x] = 255
                    continue
            elif (y + 1) < height and (x - 1) < 0:
                if check(
                    convolution_output[y, x],
                    convolution_output[y + 1, x - 1],
                    threshold,
                ):
                    threshold_image[y, x] = 255
                    continue
            elif (y - 1) < 0 and (x + 1) < width:
                if check(
                    convolution_output[y, x],
                    convolution_output[y - 1, x + 1],
                    threshold,
                ):
                    threshold_image[y, x] = 255
                    continue
    return threshold_image
