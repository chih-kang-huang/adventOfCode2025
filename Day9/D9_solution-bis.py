pointList = []
with open('input.txt') as f: 
    for line in f: 
        a, b = line.strip().split(',')
        pointList.append((int(a),int(b)))

pointList.sort()

def area(pt1, pt2): 
    return (abs(pt1[0] - pt2[0])+1) * (abs(pt1[1] - pt2[1])+1)



res = 0


# To be optimized
for i in range(len(pointList)): 
    for j in range(len(pointList)):
        res = max(res, area(pointList[i], pointList[j]))
print(res)

