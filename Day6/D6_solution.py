import numpy as np


file_path ="input.txt"

all_lines = []
try:
    with open(file_path, 'r') as file:
        all_lines = file.readlines()
except FileNotFoundError:
    print(f"Error: File not found at {file_path}")
except Exception as e:
    print(f"An error occurred: {e}")

operator_line = all_lines[-1].strip()
data_lines = all_lines[:-1]

numeric_list = []

for line in data_lines: 
    numeric_list.append([int(val) for val in line.strip().split()])

numeric_data = np.array(numeric_list, dtype=int)

# Transpose the array for better instructions
numeric_data = numeric_data.T 

operator_list = [op for op in operator_line.strip().split()]

count = 0 

for i, op in enumerate(operator_list):
    if op == "+": 
        count += np.sum(numeric_data[i])
    if op == "*":
        count += np.prod(numeric_data[i])
print(f"The grand total is {count}")




