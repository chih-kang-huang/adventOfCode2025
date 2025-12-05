
with open("input.txt", 'r') as f: 
    lines = f.read().strip().split("\n")

blank_index = lines.index("")
range_lines = lines[:blank_index]
avalableIDs = lines[blank_index+1:]

rangeIDs = []
for r in range_lines:
    start, end = r.split("-")
    rangeIDs.append((int(start), int(end)))

avalableIDs = [int(x) for x in avalableIDs]


count = 0

for ID in avalableIDs:
    if any(start <= ID <= end for start, end in rangeIDs):
        count += 1
print(count)
