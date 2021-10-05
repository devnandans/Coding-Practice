# Midori and chocolates 
# https://practice.geeksforgeeks.org/problems/midori-and-chocolates2438/1/?page=1&query=page1#

class Solution:
    def leftShops (self, i, L):
        # code here 
        N = pow(2,L)
        
        return N-i

        
        
        
        

#{ 
#  Driver Code Starts
#Initial Template for Python 3

#Initial Template for Python 3
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        i, L = input().split()
        i = int(i)
        L = int(L)
        ob = Solution()
        print(ob.leftShops(i, L))
# } Driver Code Ends