with open("input.txt", 'r') as f: 
    lines = f.read().strip().split("\n")

blank_index = lines.index("")
range_lines = lines[:blank_index]

rangeIDs = []
for r in range_lines:
    start, end = r.split("-")
    rangeIDs.append((int(start), int(end)))

rangeIDs.sort(key=lambda a : a[0])

count = 0

curr_start, curr_end = float("-inf"), float("-inf")

for start, end in rangeIDs: 
    if start > curr_end: 
        count += end - start +1 
        curr_start = start 
        curr_end = end 
    elif end > curr_end: 
        count += end - curr_end
        curr_end = end

print(count)








