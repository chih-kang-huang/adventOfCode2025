pointList = []
with open('input_example.txt') as f: 
    for line in f: 
        a, b = line.strip().split(',')
        pointList.append((int(a),int(b)))



# domain = []

# domain += [(a, b) for a in range(7, 12) for b in range(1, 3)]
# domain += [(a, b) for a in range(2, 12) for b in range(3, 6)]
# domain += [(a, b) for a in range(9, 12) for b in range(6, 8)]
print(pointList)


def isValid(pt1, pt2): 
    x_min, x_max = min(pt1[0], pt2[0]), max(pt1[0], pt2[0])
    y_min, y_max = min(pt1[1], pt2[1]), max(pt1[1], pt2[1])
    pList = pointList.copy()
    pList.append(pointList[0])
    curr = pList.pop()
    print("rectangle", pt1, pt2)
    while pList: 
        nextt = pList.pop()
          # Endpoint strictly inside 
        if (x_min < curr[0] < x_max and y_min < curr[1] < y_max):
            return True
        if (x_min < nextt[0] < x_max and y_min < nextt[1] < y_max):
            return True

        # If it is a single point, and not inside, no intersection
        if curr[0] == nextt[0] and curr[1] == nextt[1]:
            return False

        # Horizontal segment
        if curr[1] == nextt[1]:
            y = curr[1]
            if y_min < y < y_max:
                seg_min, seg_max = sorted([curr[0], nextt[0]])
                return seg_max > x_min and seg_min < x_max
            return False

        # Vertical segment
        if curr[0] == nextt[0]:
            x = curr[0]
            if x_min < x < x_max:
                seg_min, seg_max = sorted([curr[1], nextt[1]])
                return seg_max > y_min and seg_min < y_max
        return False



        curr = nextt
    return True


from dataclasses import dataclass 
from typing import List

@dataclass
class Point:
    x: float
    y: float

points = []
with open("input_example.txt", "r") as f:
    for line in f:
        line = line.strip()
        x_str, y_str = line.split(",")
        points.append(Point(int(y_str),int(x_str)))


def area(p1:Point,p2:Point):
    return (abs(p1.x - p2.x) + 1) * (abs(p1.y - p2.y) + 1)

def test_segment_cut_rectangle(p_start: Point, p_end: Point, p1: Point, p2: Point) -> bool:
    x_min, x_max = min(p1.x, p2.x), max(p1.x, p2.x)
    y_min, y_max = min(p1.y, p2.y), max(p1.y, p2.y)

    # Endpoint strictly inside 
    if (x_min < p_start.x < x_max and y_min < p_start.y < y_max):
        return True
    if (x_min < p_end.x < x_max and y_min < p_end.y < y_max):
        return True

    # If it is a single point, and not inside, no intersection
    if p_start.x == p_end.x and p_start.y == p_end.y:
        return False

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

    raise ValueError("Segment must be horizontal or vertical")



def test_cut_rectangle(points: List[Point], p1: Point, p2: Point):    
    for i in range(len(points)):
        start = points[i-1]
        end = points[i]
        if test_segment_cut_rectangle(start,end,p1,p2) :
            return False
    return True

def candidate_area(p0: Point, points: List[Point]) -> Point:
    max_area_p = 0
    for p in points :
        if test_cut_rectangle(points,p,p0):
            a = area(p,p0)
            if a > max_area_p :
                max_area_p = a
    return  max_area_p 

max_area = 0
for i in range(len(points)):
    a = candidate_area(points[i], points)
    print(f"iter {i} : Candidate {a}")
    if a > max_area :
        max_area = a

print(f"Result: {max_area}")
