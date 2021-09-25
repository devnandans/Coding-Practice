#User function Template for python3
# Q. Find the Frequency
#  https://practice.geeksforgeeks.org/problems/find-the-frequency/1/?difficulty[]=0&page=3&query=difficulty[]0page3
"""
You're given an array (arr) of length n
Return the frequency of element x in the given array
"""
def findFrequency (arr, n, x):
    
    count = 0
    for i in range(n):
        
        if x == arr[i]:
            
            count=count+1
            
    return count


#{ 
#  Driver Code Starts
#Initial Template for Python 3

t = int (input ())
for tc in range (t):
    n = int (input ())
    arr = list (map (int, input ().split ()))
    x = int (input ())
    print (findFrequency (arr, n, x))
    

# } Driver Code Ends