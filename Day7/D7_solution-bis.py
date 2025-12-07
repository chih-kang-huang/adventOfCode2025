visit = dict()

with open("input.txt") as f: 
    lines = []
    for line in f: 
        line = line.strip()
        lines.append(line)

# Initialization
for i, c in enumerate(lines[0]):
    if c == 'S': 
        visit[i] = 1

for d in range(1, len(lines)):
    new_visit = dict()
    for q in visit: 
        if lines[d][q] == '^': 
            if q+1 < len(lines[d]):
                new_visit[q+1] = new_visit.get(q+1, 0) + visit[q]
            if q-1 >=0:
                new_visit[q-1] = new_visit.get(q-1, 0) + visit[q]
        else: 
            new_visit[q] = new_visit.get(q, 0) + visit[q]
    visit = new_visit

print(sum(visit.values()))





    





