n=int(input("Enter the number:: "))
for i in range(2,n):
    r=i
    k=0
    for j in range(2,r-1):
        if(r%j==0):
            k=k+1
    if(k==0):
        print(r)


