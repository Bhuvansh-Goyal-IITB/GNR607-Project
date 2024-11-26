import os
import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from PIL import Image, UnidentifiedImageError
import numpy as np
from scipy.signal import convolve2d

from kernel import get_kernel
from threshold import get_threshold_img

import matplotlib.pyplot as plt


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Edge Detector")
        self.geometry("600x400")
        self.resizable(False, False)

        self.file_path = tk.StringVar()
        self.sigma = tk.StringVar()
        self.threshold = tk.StringVar()

        # Layout configuration
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.file_input = FileInput(self, self.file_path)
        self.file_input.grid(row=0, column=0, padx=20, pady=(20, 10), sticky="ew")

        self.parameter_input = ParameterInput(self, self.sigma, self.threshold)
        self.parameter_input.grid(row=1, column=0, padx=20, pady=10, sticky="ew")

        self.button_frame = ttk.Frame(self)
        self.button_frame.grid(row=2, column=0, padx=20, pady=(10, 20), sticky="ew")

        self.output_button = ttk.Button(
            self.button_frame, text="Show Output", command=self.show_output
        )
        self.output_button.pack(side="left", padx=5)

        self.save_button = ttk.Button(
            self.button_frame, text="Save", command=self.save_output, state="disabled"
        )
        self.save_button.pack(side="left", padx=5)

        self.clear_button = ttk.Button(
            self.button_frame, text="Clear Variables", command=self.clear_variables
        )
        self.clear_button.pack(side="left", padx=5)

        self.last_output = None

    def clear_variables(self):
        self.file_path.set("")
        self.sigma.set("")
        self.threshold.set("")
        self.save_button.config(state="disabled")
        self.last_output = None

    def check_input(self):
        file_path = self.file_path.get()
        if not os.path.exists(file_path):
            return 1

        try:
            float(self.sigma.get())
        except ValueError:
            return 2

        try:
            float(self.threshold.get())
        except ValueError:
            return 3

        return 0

    def save_output(self):
        file_path = filedialog.asksaveasfilename(
            defaultextension=".png",
            filetypes=[
                ("PNG Files", "*.png"),
                ("JPEG Files", "*.jpg;*.jpeg"),
                ("All Files", "*.*"),
            ],
        )

        if file_path and self.last_output is not None:
            try:
                plt.imsave(file_path, self.last_output, cmap="gray")
                messagebox.showinfo(
                    "File Saved", f"File {file_path} was successfully saved"
                )
            except FileNotFoundError as e:
                messagebox.showerror("Error", f"Directory not found: {e}")
            except ValueError as e:
                messagebox.showerror("Error", f"Invalid image data: {e}")
            except OSError as e:
                messagebox.showerror("Error", f"Error saving the image: {e}")
            except Exception as e:
                messagebox.showerror("Error", f"An unexpected error occurred: {e}")

    def show_output(self):
        self.output_button.config(state="disabled")
        check_output = self.check_input()
        if check_output == 0:
            try:
                img = Image.open(self.file_path.get()).convert("L")
                self.last_output = self.process_img(img)
                self.save_button.config(state="normal")

                plt.imshow(self.last_output, cmap="gray")
                plt.axis("off")
                plt.tight_layout()
                plt.show()
            except UnidentifiedImageError:
                messagebox.showerror("Error", "File is not an image")

        elif check_output == 1:
            messagebox.showerror("Error", "File does not exist")
        elif check_output == 2:
            messagebox.showerror("Error", "Please enter a valid value for sigma")
        elif check_output == 3:
            messagebox.showerror("Error", "Please enter a valid value for threshold")

        self.output_button.config(state="normal")

    def process_img(self, img: Image.Image):
        img_array = np.array(img).astype(np.float64)
        kernel = get_kernel(float(self.sigma.get()))
        convolution_output = convolve2d(img_array, kernel, mode="same")
        return get_threshold_img(convolution_output, float(self.threshold.get()))


class FileInput(ttk.Frame):
    def __init__(self, master, file_path):
        super().__init__(master)

        self.file_input_label = ttk.Label(self, text="File Input:")
        self.file_input_label.pack(side="left", padx=5)

        self.file_path = file_path
        self.file_input = ttk.Entry(self, textvariable=self.file_path, width=40)
        self.file_input.pack(side="left", padx=5)

        self.file_browse_button = ttk.Button(
            self, text="Browse", command=self.select_file
        )
        self.file_browse_button.pack(side="left", padx=5)

    def select_file(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            self.file_path.set(file_path)


class ParameterInput(ttk.Frame):
    def __init__(self, master, sigma, threshold):
        super().__init__(master)
        self.threshold = threshold
        self.sigma = sigma

        self.sigma_input_label = ttk.Label(self, text="Sigma:")
        self.sigma_input_label.pack(anchor="w", padx=5, pady=(0, 2))

        self.sigma_input = ttk.Entry(self, textvariable=self.sigma)
        self.sigma_input.pack(fill="x", padx=5, pady=(0, 10))

        self.threshold_input_label = ttk.Label(self, text="Threshold:")
        self.threshold_input_label.pack(anchor="w", padx=5, pady=(0, 2))

        self.threshold_input = ttk.Entry(self, textvariable=self.threshold)
        self.threshold_input.pack(fill="x", padx=5, pady=(0, 10))


app = App()
app.mainloop()
