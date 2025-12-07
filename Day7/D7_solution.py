count = 0 
visit = set()
with open("input.txt") as f: 
    for line in f: 
        line = line.strip()
        for i, c in enumerate(line): 
            if c == "S": 
                visit.add(i)
            if c == "^" and i in visit:
                count += 1
                visit.remove(i)
                if i +1 < len(line): 
                    visit.add(i+1)
                if i-1 >=0:
                    visit.add(i-1)

print(count)


