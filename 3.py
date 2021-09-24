# Q 3. https://practice.geeksforgeeks.org/problems/rotate-array-by-n-elements/0

t = int(input())

for i in range(t):
    n,d = map(int,input().split())
    
    ar = list(map(int,input().split()))
    
    
    for i in range(d,n):
        
        
        print(ar[i],end=" ")
        
    for i in range(d):
        
        print(ar[i], end = " ")
    
    
    print(" ")
