with open("input.txt", "r") as f: 
    line = f.readline().strip()                                                                                  
ranges = line.split(",") 
res = 0                                                          
for r in ranges: 
    head, tail = r.split("-") 
    head, tail = int(head), int(tail)                
    k = 1                                                                                            
    while (1+ 10**k)*(10**k-1) < head: 
        k+= 1                                                                                        
    # so we have (1+10**k)*(10**(k-1)) >= head
    while (1+ 10**k)*(10**(k-1)) <= tail:        
        j = 10**(k-1)
        while (1+10**k)*j <= tail and j<10**k:
            if (1+10**k)*j >= head:
                res += (1+10**k)*j
            j+=1

        k+=1
print(res)   
