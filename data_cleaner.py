import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()
input_file_path = filedialog.askopenfilename(title="Select Input File", filetypes=[("Text files", "*.txt")])

if not input_file_path:
    print("No file selected. Exiting.")
else:
    output_file_path = 'output.txt'

    with open(input_file_path, 'r') as input_file, open(output_file_path, 'w') as output_file:

        for line in input_file:
            values = line.strip().split('\t')
            last_value = values[-1]
            output_file.write(last_value + '\n')

    print(f"Output written to {output_file_path}")
