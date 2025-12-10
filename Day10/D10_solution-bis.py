# Code to be optimized further

def pressJoltage(joltage, button): 
    for b in button: 
        joltage[b] -= 1
    return joltage
def validButton(joltage, button):
    for b in button:
        if joltage[b] <= 0:
            return False
    return True



def minimumPressesJoltage(joltageReq, buttons): 
    """
    using backtracking to find the minimum number of presses required
    ------
    joltageReq = joltage current state
    buttons = list of buttons
    """
    res = float("inf") 
    #print(f"Objective {objective} | buttons {buttons}")

    def dfs(currJol, nb_press, i):
        """ 
        currJol = current joltage state
        nb_press = number of presses
        i = decistion at ith button
        """
        nonlocal res
        if sum(currJol) == 0: 
            res = min(res, nb_press)
            return
        if i == len(buttons): 
            return
        if validButton(currJol, buttons[i]):
            currJol = pressJoltage(currJol, buttons[i]) # press the ith button
            dfs(currJol, nb_press+1, i)
            for b in buttons[i]: # backtracking
                currJol[b] += 1
            dfs(currJol, nb_press, i+1) # Not pressing the ith button
        else: 
            dfs(currJol, nb_press, i+1)
    dfs(joltageReq, 0, 0)
    return res


# print(minimumPressesJoltage(
#         [3, 5, 4, 7], [[3], [1,3], [2], [2, 3], [0, 2], [0, 1]]
#         )
#       )
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
        print(a)
        count += a

print(count)
