#User function Template for python3
# https://practice.geeksforgeeks.org/problems/doubling-the-value4859/1/?difficulty[]=-1&page=1&query=difficulty[]-1page1#
class Solution:
    def solve(self,n : int, a : list, b : int):
        # Complete this function
        
        for i in range(n):
            
            if a[i] == b:
                
                b = b*2
                
        return b

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n , b = map(int, input().split())
        arr = [int(x) for x in input().split()]
        ob = Solution()
        print(ob.solve(n, arr, b))
# } Driver Code Ends