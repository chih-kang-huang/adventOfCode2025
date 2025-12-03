def twelveBatteries(s):
    # greedy 
    stack = []
    n = len(s)
    k = n - 12
    for c in s: 
        c = int(c)
        while k > 0 and stack and stack[-1] < c: 
            stack.pop()
            k -= 1
        stack.append(c)

    return sum([ stack[i] * 10**(11-i) for i in range(12)])

res = 0
with open("input.txt", "r") as f:
    for s in f:
        s = s.strip() # remove trailing lines
        res += twelveBatteries(s)

print(res)

