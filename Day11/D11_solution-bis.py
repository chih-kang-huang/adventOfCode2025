linkDict = dict()

with open('input.txt') as f: 
    for line in f: 
        line = ''.join(c for c in line if c not in ":")
        line = line.strip().split(" ")
        linkDict[line[0]] = line[1:]


import functools as ft # cache the results

@ft.cache
def dfs(curr, target): 
    if curr == target: 
        return 1
    return sum([dfs(connection, target) for connection in linkDict.get(curr, [])])

# There is only one possible path between fft -> dac and dac -> ftt, otherwise the result would be infinite due to cyclics
print(dfs("svr", "fft")*dfs("fft", "dac")* dfs("dac", "out"))
print(dfs("svr", "dac")*dfs("dac", "fft")* dfs("fft", "out"))
