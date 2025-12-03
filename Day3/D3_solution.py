def maxJoltage(s):
    # s = string of numbers
    digit1 = float("-inf")
    digit2 = float("-inf")
    for c in s[:-1]: 
        c = int(c)
        if c > digit1: 
            digit1 = c 
            digit2 = float("-inf") # reset digit2
        elif c > digit2: 
            digit2 = c
    # case where digit2 not affected by the end
    digit2 = max(digit2, int(s[-1]))

    return digit1*10 + digit2

res = 0
with open("input.txt", "r") as f:
    for s in f:
        s = s.strip() # remove trailing lines
        # print(f"{maxJoltage(s)} and {s}")
        res += maxJoltage(s)

print(res)

