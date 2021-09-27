#User function Template for python3
# Q . https://practice.geeksforgeeks.org/problems/rotate-by-90-degree-1587115621/1/?difficulty[]=-1&page=5&query=difficulty[]-1page5
# Given a square matrix of size N x N. The task is to rotate it by 90 degrees in anti-clockwise direction without using any extra space.
class Solution:
    
    def transpose(self,a,n):
        
        for i in range(n): 
            for j in range(n): 
                
                
                t = a[i][j] 
                a[i][j] = a[j][i] 
                a[j][i] = t 
    
    def rotation(self,a,n):
        
        for i in range(n): 
            j = 0
            k = n-1
            while j < k: 
                
                
                t = a[j][i] 
                a[j][i] = a[k][i] 
                a[k][i] = t 
                j += 1
                k -= 1
    def rotateby90(self,a, n): 
        
        self.transpose(a,n) 
        self.rotation(a,n)
        
        
               
                
         
#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        n = int(input())
        matrix = [[0 for j in range(n)] for i in range(n)]
        line1 = [int(x) for x in input().strip().split()]
        k=0
        for i in range(n):
            for j in range (n):
                matrix[i][j]=line1[k]
                k+=1
        obj = Solution()
        obj.rotateby90(matrix,n)
        for i in range(n):
            for j in range(n):
                print(matrix[i][j],end=" ")
        print()

# } Driver Code Ends