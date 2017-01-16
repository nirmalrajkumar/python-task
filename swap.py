lis = []
while True:
        str1 = raw_input()
        lis.append(str1)
        text = ''.join(lis)
        n=len(lis)
        if lis[n-1]=="EOF":
        	break

print text.swapcase()  
