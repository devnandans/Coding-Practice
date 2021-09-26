#User function Template for python3
#Q . Cyclically rotate an array by one

# https://practice.geeksforgeeks.org/problems/cyclically-rotate-an-array-by-one2614/1/?difficulty[]=-1&page=2&query=difficulty[]-1page2
def rotate( arr, n):
    
    
    e = arr[n-1]
    
    
    for i in range(n-1,0,-1):
        
        arr[i]=arr[i-1]
        
        #j+=1
        
    arr[0]=e
    #return arr
    #print(arr[0], end = " ")
        
    

