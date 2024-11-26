# Edge Detector

A command-line tool for detecting edges in images using the Laplacian of Gaussian (LoG) filter and thresholding techniques. This project was completed as part of the GNR607 course taught by Prof. B. Krishna Mohan. 

## Requirements

This script requires Python to run. To install the necessary libraries, use the following command:

```bash
pip install matplotlib numpy pillow scipy
```

Nix users can use the nix develop to setup the development environment.


## Usage/Example

```bash
python main.py [sigma] [threshold] [file_path] [-s SAVE_PATH]
```

**Arguments:**

* **sigma (float):** Standard deviation for Gaussian blurring.
* **threshold (float):** Threshold value for edge detection.
* **file_path (str):** Path to the input image.

**Optional Argument:**

* **-s SAVE_PATH (str):** Path to save the output image.

**Example:**

```bash
python main.py 2 0.1 images/lotus.jpg -s results/lotus_edges.png
```

This command will process the image `images/lotus.jpg`, apply Gaussian blur with a sigma of 2, and detect edges with a threshold of 0.1. The resulting edge-detected image will be saved to `results/lotus.png`.

## Results
Here are results tested on the images in the images folder:
![lotus](./results/lotus.png)
<!---->
<!--### Results-->
<!---->
<!--the results are in the results folder-->
<!---->
<!--parameters used for the images are:-->
