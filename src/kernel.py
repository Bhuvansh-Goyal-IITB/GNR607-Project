import math
import numpy as np
import numpy.typing as npt


def get_kernel(sigma: float) -> npt.NDArray[np.float64]:
    kernel_half_width = math.floor(3 * sigma)

    meshgrid_coordinates = (
        np.array([i for i in range(0, (2 * kernel_half_width) + 1)]) - kernel_half_width
    )

    kernel_X, kernel_Y = np.meshgrid(meshgrid_coordinates, meshgrid_coordinates)

    sigma_sq = sigma * sigma

    gaussian = (1 / (2 * math.pi * sigma_sq)) * np.exp(
        -1 * (np.square(kernel_X) + np.square(kernel_Y)) / (2 * sigma_sq)
    ).astype(np.float64)

    return (
        (1 / sigma_sq)
        * (((np.square(kernel_X) + np.square(kernel_Y)) / sigma_sq) - 2)
        * gaussian
    )
