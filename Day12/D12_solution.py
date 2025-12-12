


totalsurfaces = 54-15

def condition3x3(a, b, presentList): 
    # Assume all the present shapes or just 3x3 squares, check if it is possible to filled the regions of a x b
    s = sum(presentList) 
    if (a//3) * (b//3) >= s: 
        return True
    return False

nb_of_presents = 0
regionList = [] #[(a, b, presentList)]
with open("input.txt") as f: 
    for line in f: 
        if 'x' in line:
            line = ''.join(c for c in line if c not in "l") 
            line = line.strip().split(" ")
            presentList = [int(c) for c in line[1:]]
            a,b = line[0].strip(':').split('x')
            regionList.append([int(a), int(b), presentList])


count = 0

for  a, b, presentList in regionList:
    if condition3x3(a, b, presentList):
        count += 1
    elif sum(presentList)*totalsurfaces > a*b: 
        continue
    else:
        print("Undecidable yet")

print(count)



