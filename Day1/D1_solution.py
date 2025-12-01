count = 0
start = 50
with open("input.txt", "r") as f:
    for rotation in f:
        rotation = rotation.strip() # remove trailing lines
        # print(rotation)
        r, steps = rotation[0], int(rotation[1:])
        if r == 'R':
            start = (start + steps) % 100
        else: 
            start = (start - steps) % 100
        count += (start == 0)

print(f"The password is {count}")
