# You are given an array arr[], you have to re-construct an array arr[].
#The values in arr[] are obtained by doing Xor of consecutive elements in the array.

def game_with_number (arr,  n) : 
    #Complete the function
        for i in range(0,n-1):
            arr[i]=arr[i]^arr[i+1]
            
        return arr
#{ 
#  Driver Code Starts
#Initial Template for Python 3


for _ in range(0,int(input())):
    
    n = int(input())
    arr = list(map(int,input().strip().split()))
    res = game_with_number(arr, n);
    print(*res)




# } Driver Code Ends