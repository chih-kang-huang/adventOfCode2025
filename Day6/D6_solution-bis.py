import numpy as np


file_path ="input.txt"

all_lines = []
try:
    with open(file_path, 'r') as f:
        all_lines = [line.rstrip("\n") for line in f.readlines()]
except FileNotFoundError:
    print(f"Error: File not found at {file_path}")
except Exception as e:
    print(f"An error occurred: {e}")

operator_line = all_lines[-1]
data_line = all_lines[:-1]

numeric_list = [[]]

# for i in range(len(data_line[0])-1, -1, -1): 
for i in range(len(data_line[0])): 
    s = ([ data_line[c][i] for c in range(len(data_line))])
    number = ("".join([ c for c in s if c != ' ']))
    # print(s, number)
    if number: 
        numeric_list[-1].append(int(number))
    else: 
        numeric_list.append([])
operator_list = [op for op in operator_line.strip().split()]

assert(len(operator_list) == len(numeric_list))

count = 0 

for i, op in enumerate(operator_list):
   if op == "+": 
       count += sum(numeric_list[i])
   if op == "*":
       count += np.prod(np.array(numeric_list[i]))
print(f"The grand total is {count}")




