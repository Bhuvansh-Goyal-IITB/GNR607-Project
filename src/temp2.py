import tkinter as tk
from tkinter import filedialog, messagebox


def select_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        file_input.set(file_path)


def show_output():
    file_path = file_input_box.get()
    try:
        float1 = float(float_input1.get())
        float2 = float(float_input2.get())
        messagebox.showinfo(
            "Output", f"File: {file_path}\nFloat 1: {float1}\nFloat 2: {float2}"
        )
    except ValueError:
        messagebox.showerror("Error", "Please enter valid float numbers.")


# Initialize the app
app = tk.Tk()
app.geometry("600x400")
app.title("Tkinter GUI")

# File input section
file_input_label = tk.Label(app, text="File Input:")
file_input_label.pack(pady=(10, 5))

file_input_frame = tk.Frame(app)
import tkinter as tk
from tkinter import filedialog, messagebox


def select_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        file_input_box.delete(0, tk.END)
        file_input_box.insert(0, file_path)


def show_output():
    file_path = file_input_box.get()
    try:
        float1 = float(float_input1.get())
        float2 = float(float_input2.get())
        messagebox.showinfo(
            "Output", f"File: {file_path}\nFloat 1: {float1}\nFloat 2: {float2}"
        )
    except ValueError:
        messagebox.showerror("Error", "Please enter valid float numbers.")


# Initialize the app
app = tk.Tk()
app.geometry("400x200")
app.title("Tkinter GUI")

# File input section
file_input_label = tk.Label(app, text="File Input:")
file_input_label.pack(pady=(10, 5))

file_input_frame = tk.Frame(app)
file_input_frame.pack(fill="x", padx=10)

file_input_box = tk.Entry(file_input_frame, width=40)
file_input_box.pack(side="left", padx=(0, 5), pady=5)

file_browse_button = tk.Button(file_input_frame, text="Browse", command=select_file)
file_browse_button.pack(side="left")

# Float input section
float_input1_label = tk.Label(app, text="Float Input 1:")
float_input1_label.pack(pady=(10, 5))

float_input1 = tk.Entry(app)
float_input1.pack(pady=5, padx=10)

float_input2_label = tk.Label(app, text="Float Input 2:")
float_input2_label.pack(pady=(10, 5))

float_input2 = tk.Entry(app)
float_input2.pack(pady=5, padx=10)

# Show Output Button
show_output_button = tk.Button(app, text="Show Output", command=show_output)
show_output_button.pack(pady=(15, 10))

# Run the application
app.mainloop()

file_input = tk.StringVar()
file_input_box = tk.Entry(file_input_frame, textvariable=file_input, width=40)
file_input_box.pack(side="left", padx=(0, 5), pady=5)

file_browse_button = tk.Button(file_input_frame, text="Browse", command=select_file)
file_browse_button.pack(side="left")

file_input_frame.pack()

# Float input section
float_input1_label = tk.Label(app, text="Float Input 1:")
float_input1_label.pack(pady=(10, 5))

float_input1 = tk.Entry(app)
float_input1.pack(pady=5, padx=10)

float_input2_label = tk.Label(app, text="Float Input 2:")
float_input2_label.pack(pady=(10, 5))

float_input2 = tk.Entry(app)
float_input2.pack(pady=5, padx=10)

# Show Output Button
show_output_button = tk.Button(app, text="Show Output", command=show_output)
show_output_button.pack(pady=(15, 10))

# Run the application
app.mainloop()
