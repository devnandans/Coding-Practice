# Q 4. https://practice.geeksforgeeks.org/problems/geek-onacci-number/0/



def onacci(a,b,c,n):
    

    if n == 1:
        return a
        
        
    if n == 1:
        return b
        
        
    if n == 1:
        return c
        
        
   
        
    return onacci(a, b, c, n-1) + onacci(a, b, c, n-2) + onacci(a, b, c, n-3)
        




t = int(input())


for i in range(t):

    
    a,b,c,n = map(int,input().split())
    #print(n)
    
    print(onacci(a,b,c,n))
  
  
  