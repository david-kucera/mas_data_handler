import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()
input_file_path = filedialog.askopenfilename(title="Select Input File", filetypes=[("Text files", "*.txt")])

if not input_file_path:
    print("No file selected. Exiting.")
else:
    data = []
    with open(input_file_path, 'r') as input_file:
        for line in input_file:
            if line.strip():
                try:
                    data.append(int(line))
                except ValueError:
                    print(f"Skipping invalid line: {line}")

    try:
        min_value = int(input("Enter the minimum value: "))
        max_value = int(input("Enter the maximum value: "))
    except ValueError:
        print("Invalid input. Please enter valid integer values. Exiting.")
        exit()

    filtered_data = [value for value in data if min_value <= value <= max_value]

    output_file_path = "output_specified.txt"
    with open(output_file_path, 'w') as output_file:
        for value in filtered_data:
            output_file.write(str(value) + '\n')

    print(f"Filtered data saved to {output_file_path}")
