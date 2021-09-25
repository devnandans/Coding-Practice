#User function Template for python3
#Q 6. https://practice.geeksforgeeks.org/problems/sum-of-product-of-x-and-y-with-floornx-y3711/1/?page=1&query=page1#

#Sum of product of x and y with floor(n/x) = y 

class Solution:
	def sumofproduct(self, n):
		ans = 0
	    x = 1
	    
	    while x<=n:
	        y=n//x
	       
	        p = x * y
	    
	        ans = ans + p
	        
	        x = x + 1
	
        return ans
        
#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		ob = Solution()
		ans = ob.sumofproduct(n)
		print(ans)
# } Driver Code Ends