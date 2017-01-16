lis = [2,1784,145,14,484,8,17,4]
new = []

while lis:
    minimum = lis[0]  
    for x in lis: 
        if x < minimum:
            minimum = x
    new.append(minimum)
    lis.remove(minimum)    

print new
