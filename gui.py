import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from Signal import compute_function, functions  # Import your defined functions and compute_function

def plot_function():
    # Get selected function
    func_name = function_var.get()
    
    # Collect parameters from the input fields
    try:
        params = {
            "frequency": float(frequency_entry.get()) if frequency_entry.get() else None,
            "amplitude": float(amplitude_entry.get()) if amplitude_entry.get() else None,
            "start_time": float(start_time_entry.get()) if start_time_entry.get() else None,
            "end_time": float(end_time_entry.get()) if end_time_entry.get() else None,
            "cutoff_low": float(cutoff_low_entry.get()) if cutoff_low_entry.get() else None,
            "cutoff_high": float(cutoff_high_entry.get()) if cutoff_high_entry.get() else None,
            "levels": int(levels_entry.get()) if levels_entry.get() else None,
            "window_size": int(window_size_entry.get()) if window_size_entry.get() else None,
        }
    except ValueError:
        result_label.config(text="Please enter valid numbers for the parameters.")
        return

    # Compute function values
    try:
        result = compute_function(func_name, params)
        if isinstance(result, tuple):  # Assume the result is (x, y) for plotting
            x, y = result
        else:
            result_label.config(text=f"Result: {result}")
            return
    except ValueError as e:
        result_label.config(text=str(e))
        return
    
    result_label.config(text="")  # Clear error message
    
    # Clear previous plot
    ax.clear()
    ax.plot(x, y, label=func_name)
    ax.legend()
    ax.grid(True)
    
    # Redraw canvas
    canvas.draw()

# Create the main window
root = tk.Tk()
root.title("Signal Function Plotter")

# Dropdown menu for function selection
function_var = tk.StringVar(value="plot_signals")
function_label = tk.Label(root, text="Select Function:")
function_label.grid(row=0, column=0, padx=5, pady=5)
function_menu = ttk.Combobox(root, textvariable=function_var, values=list(functions.keys()))
function_menu.grid(row=0, column=1, padx=5, pady=5)

# Entry fields for parameters
fields = [
    ("Frequency", "frequency_entry"),
    ("Amplitude", "amplitude_entry"),
    ("Start Time", "start_time_entry"),
    ("End Time", "end_time_entry"),
    ("Cutoff Low", "cutoff_low_entry"),
    ("Cutoff High", "cutoff_high_entry"),
    ("Quantization Levels", "levels_entry"),
    ("Window Size", "window_size_entry"),
]

entries = {}
for idx, (label_text, var_name) in enumerate(fields, start=1):
    label = tk.Label(root, text=label_text + ":")
    label.grid(row=idx, column=0, padx=5, pady=5)
    entry = tk.Entry(root)
    entry.grid(row=idx, column=1, padx=5, pady=5)
    entries[var_name] = entry

# Make entries accessible by variable names
frequency_entry = entries["frequency_entry"]
amplitude_entry = entries["amplitude_entry"]
start_time_entry = entries["start_time_entry"]
end_time_entry = entries["end_time_entry"]
cutoff_low_entry = entries["cutoff_low_entry"]
cutoff_high_entry = entries["cutoff_high_entry"]
levels_entry = entries["levels_entry"]
window_size_entry = entries["window_size_entry"]

# Plot button
plot_button = tk.Button(root, text="Plot", command=plot_function)
plot_button.grid(row=len(fields) + 1, column=0, columnspan=2, pady=10)

# Result label for error messages or results
result_label = tk.Label(root, text="", fg="red")
result_label.grid(row=len(fields) + 2, column=0, columnspan=2)

# Matplotlib figure
fig, ax = plt.subplots(figsize=(5, 4))
canvas = FigureCanvasTkAgg(fig, master=root)
canvas_widget = canvas.get_tk_widget()
canvas_widget.grid(row=len(fields) + 3, column=0, columnspan=2, pady=10)

# Start the application
root.mainloop()
