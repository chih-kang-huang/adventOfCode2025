import math
def checkInvalid(n):
    digits = int(math.log10(n)+1)
    for k in range(1, digits//2+1):
        if digits % k == 0: 
            m = digits // k
            # construct divider
            divider = 0
            for i in range(m):
                divider += 10**(i*k)
            if n % divider ==0:
                return True
    return False


with open("input.txt", "r") as f: 
    line = f.readline().strip()                                                                                  
ranges = line.split(",") 
res = 0                                                          
for r in ranges: 
    head, tail = r.split("-") 
    head, tail = int(head), int(tail)                
    for n in range(head, tail+1):
        if checkInvalid(n): 
            res += n
print(res)   
