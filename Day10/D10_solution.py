def press(state, button): 
    for b in button: 
        state[b] = 1 - state[b]
    return state


def minimumPresses(objective, buttons): 
    """
    using backtracking to find the minimum number of presses required
    ------
    objective = objective state represented by 0s and 1s
    buttons = list of buttons
    """
    res = float("inf") 
    #print(f"Objective {objective} | buttons {buttons}")

    def dfs(curr, nb_press, i):
        """ 
        curr = current state represented by 0 and 1s
        nb_press = number of presses
        i = decistion at ith button
        """
        nonlocal res
        if i == len(buttons): 
            if curr == objective: 
                res = min(res, nb_press)
                return
            return
        #print(f"Current state {curr} | nb_press {nb_press} | Button {buttons[i]}")
        curr = press(curr, buttons[i]) # press the ith button
        dfs(curr, nb_press+1, i+1)
        curr = press(curr, buttons[i]) # remove the ith button
        dfs(curr, nb_press, i+1)

    dfs([0 for _ in range(len(objective))], 0, 0)
    return res

count = 0
with open("input.txt") as f: 
    for line in f: 
        line = ''.join(c for c in line if c not in "(){}<>[]'")
        line = line.strip().split(" ")
        objective = [ int(c == '#') for c in line[0]]
        buttons = [ l.split(",") for l in line[1:-1]]
        buttons = [[int(b) for b in button ] for button in buttons]
        count += minimumPresses(objective, buttons)

print(count)
