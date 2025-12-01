count = 0
start = 50
with open("input.txt", "r") as f:
    for rotation in f:
        rotation = rotation.strip() # remove trailing lines
        # print(rotation)
        r, steps = rotation[0], int(rotation[1:])
        if r == 'R':
            count += (start + steps)//100
            start = (start + steps) % 100
        else: 
            count -= (start - steps)//100 + (start == 0)
            start = (start - steps) % 100
            count += (start ==0)

print(f"The password is {count}")
