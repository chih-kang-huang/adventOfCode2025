from dataclasses import dataclass 
from typing import List

@dataclass
class Point:
    x: float
    y: float

points = []
with open("input.txt", "r") as f:
    for line in f:
        line = line.strip()
        x_str, y_str = line.split(",")
        points.append(Point(int(y_str),int(x_str)))


def area(p1:Point,p2:Point):
    return (abs(p1.x - p2.x) + 1) * (abs(p1.y - p2.y) + 1)

def test_segment_cut_rectangle(p_start: Point, p_end: Point, p1: Point, p2: Point) -> bool:
    x_min, x_max = sorted([p1.x, p2.x])
    y_min, y_max = sorted([p1.y, p2.y])

    # # Endpoint strictly inside 
    # if (x_min < p_start.x < x_max and y_min < p_start.y < y_max):
    #     return True
    # if (x_min < p_end.x < x_max and y_min < p_end.y < y_max):
    #     return True

    # Horizontal segment
    if p_start.y == p_end.y:
        y = p_start.y
        if y_min < y < y_max:
            seg_min, seg_max = sorted([p_start.x, p_end.x])
            return seg_max > x_min and seg_min < x_max
        return False

    # Vertical segment
    if p_start.x == p_end.x:
        x = p_start.x
        if x_min < x < x_max:
            seg_min, seg_max = sorted([p_start.y, p_end.y])
            return seg_max > y_min and seg_min < y_max
        return False


def test_cut_rectangle(points: List[Point], p1: Point, p2: Point):    
    pList = points.copy()
    pList.append(points[0])
    curr = pList.pop()
    while pList:
        nextt = pList.pop()
        if test_segment_cut_rectangle(curr,nextt,p1,p2) :
            return False
        curr = nextt
    return True

res = 0
for i in range(len(points)):
    for j in range(i, len(points)):
        pi = points[i]
        pj = points[j]
        if test_cut_rectangle(points, pi, pj): 
            res = max(res, area(pi, pj))

print(res)
