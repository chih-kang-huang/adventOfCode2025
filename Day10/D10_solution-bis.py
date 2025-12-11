# Code to be optimized further

def pressJoltage(joltage, button): 
    for b in button: 
        joltage[b] -= 1
    return joltage
def cancelPressJoltage(joltage, button): 
    for b in button: 
        joltage[b] += 1
    return joltage
def validButton(joltage, button):
    for b in button:
        if joltage[b] <= 0:
            return False
    return True

from collections import deque

def minimumPressesJoltage(target, buttons): 
    """
    BFS
    ------
    target
    buttons = list of buttons
    """
    # res = float("inf") 
    #print(f"Objective {objective} | buttons {buttons}")
    target = tuple(target)
    n = len(target)

    # BFS
    start = tuple([0]*n)
    queue = deque([(start, 0)])   # (state, number_of_presses)
    visited = {start}

    while queue:
        state, nb_presses = queue.popleft()

        if state == target:
            return nb_presses  

        # Try pressing each button
        # for inc in incs:
        for button in buttons :
            new_state = tuple(state[i] + int(i in button) for i in range(n))
            # prune: don't exceed target
            if any(new_state[i] > target[i] for i in range(n)):
                continue
            if new_state not in visited:
                visited.add(new_state)
                queue.append((new_state, nb_presses + 1))



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
        print(joltageReq, buttons)
        a= minimumPressesJoltage(joltageReq, buttons)
        count += a

print(count)
