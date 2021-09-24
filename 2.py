#Q 2. Print the pattern.
#12345
#22345
#33345
#44445
#55555

n = 5

for i in range(n):
    
    for j in range(i+1):
        print(i+1, end = "")
        
    for j in range(i+1,n):
        
        print(j+1, end = "")
        
    print(" ")