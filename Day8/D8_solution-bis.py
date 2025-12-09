import heapq  

pointList = []

with open("input.txt") as f: 
    for line in f: 
        pointList.append([int(a) for a in line.strip().split(",")])


def euclideanDistanceSquare(pt1, pt2): 
    return sum([(a-b)**2 for a, b in zip(pt1, pt2)])

shortestdistances = []

heapq.heapify(shortestdistances)

for i in range(len(pointList)):
    for j in range(len(pointList)):
        if i < j : 
            pti = pointList[i]
            ptj = pointList[j]
            d_ij = euclideanDistanceSquare(pti, ptj)
            heapq.heappush(shortestdistances, (d_ij, i, j)) # append negative distance 

parent = {}
size = {}

        
def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    px, py = find(x), find(y)
    if px != py:
        parent[py] = px
        size[px] += size[py]


while not parent or size[find(list(parent.keys())[0])] < len(pointList):
    d_ab, a, b = heapq.heappop(shortestdistances)
    # print(d_ab, pointList[a], pointList[b])
    if a not in parent: 
        parent[a] = a
        size[a] = 1
    if b not in parent: 
        parent[b] = b
        size[b] = 1
    union(a, b)

print(pointList[a][0]*pointList[b][0])
# cluster_size = {}
# for x in parent: 
#     root = find(x)
#     cluster_size[root] = size[root]
# s = 1
# for a in sorted(cluster_size.values())[-3:]: 
#     s *=a
# print(s)







