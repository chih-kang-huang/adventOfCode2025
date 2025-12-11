# Use scipy.optimize.milp for efficiency

import scipy
import numpy as np

# def pressJoltage(joltage, button): 
#     for b in button: 
#         joltage[b] -= 1
#     return joltage
# def cancelPressJoltage(joltage, button): 
#     for b in button: 
#         joltage[b] += 1
#     return joltage
# def validButton(joltage, button):
#     for b in button:
#         if joltage[b] <= 0:
#             return False
#     return True
#

def minimumPressesJoltage(target, buttons): 
    """
    BFS
    ------
    target
    buttons = list of buttons
    """
    n = len(target)
    m = len(buttons)
    target = np.array(target, dtype=int) 
    c = np.ones((m), dtype=int)
    A =np.zeros((n, m))
    for i, button in enumerate(buttons):
        for b in button:
            A[b,i]= 1
    # print(f"A = {A} |  c = {c} | target = {target}")
    constraints = scipy.optimize.LinearConstraint(
            A, target, target
            )
    res = scipy.optimize.milp(c=c, constraints=constraints, integrality = np.ones_like(c))
    assert(np.allclose(A @ res.x, target))
    print("Milp", target, buttons, res.x, c.T@res.x)
    # print("Milp", c.T@res.x)
    return round(c.T @ res.x) # sometimes it gives float, round to the nearest interger
    
    
# print(minimumPressesJoltage(
        # [3, 5, 4, 7], [[3], [1,3], [2], [2, 3], [0, 2], [0, 1]]
        # )
      # )
count = 0
with open("input.txt") as f: 
    for line in f: 
        line = ''.join(c for c in line if c not in "(){}<>[]'")
        line = line.strip().split(" ")
        #objective = [ int(c == '#') for c in line[0]]
        joltageReq = [ int(c) for c in line[-1].split(',')]
        buttons = [ l.split(",") for l in line[1:-1]]
        buttons = [[int(b) for b in button ] for button in buttons]
        a= minimumPressesJoltage(joltageReq, buttons)
        # print(joltageReq, buttons, a)
        count += (a)

print(count)
