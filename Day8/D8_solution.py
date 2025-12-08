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
            if len(shortestdistances)<1000: 
                heapq.heappush(shortestdistances, (-d_ij, i, j)) # append negative distance 
            else: 
                neg_d, a, b = heapq.heappop(shortestdistances) 
                if d_ij < -neg_d:
                    heapq.heappush(shortestdistances, (-d_ij, i, j)) # append negative distance 
                else: 
                    heapq.heappush(shortestdistances, (neg_d, a, b)) # append negative distance 

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


for neg_d, a, b in shortestdistances: 
    if a not in parent: 
        parent[a] = a
        size[a] = 1
    if b not in parent: 
        parent[b] = b
        size[b] = 1
    union(a, b)

cluster_size = {}
for x in parent: 
    root = find(x)
    cluster_size[root] = size[root]
s = 1
for a in sorted(cluster_size.values())[-3:]: 
    s *=a
print(s)







