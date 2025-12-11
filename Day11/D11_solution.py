linkDict = dict()

with open('input.txt') as f: 
    for line in f: 
        line = ''.join(c for c in line if c not in ":")
        line = line.strip().split(" ")
        linkDict[line[0]] = line[1:]

assert("you" in linkDict)


def dfs(curr, target): 
    if curr == target: 
        return 1
    return sum([dfs(connection, target) for connection in linkDict.get(curr, [])])

print(dfs("you", "out"))
