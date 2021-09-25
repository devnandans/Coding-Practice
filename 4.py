# Q 4. https://practice.geeksforgeeks.org/problems/geek-onacci-number/0/


for i in range(int(input())):

    
    a,b,c,n = map(int,input().split())
    #print(n)
    s=0
    N=4
    while N<=n:
        s = a+b+c
        a,b,c=b,c,s
        N+=1
        
    print(s)
  
  
  