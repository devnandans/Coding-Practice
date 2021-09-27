#Q . https://practice.geeksforgeeks.org/problems/sum-of-upper-and-lower-triangles-1587115621/1/?difficulty[]=-1&page=1&query=difficulty[]-1page1
# Sum of upper and lower triangles
class Solution:
    
    #Function to return sum of upper and lower triangles of a matrix.
    def sumTriangles(self,matrix, n):
        # code here
        c = 0
        s = 0
        m = 0
        ar = []
        for i in range(n):
            
            for j in range(n):
                
                if i == j:
                    
                    c = c + matrix[i][j]
                    
                elif j > i:
                    
                    s = s + matrix[i][j]
                
                elif i > j:
                    
                    m = m + matrix[i][j]
                    
        Sum1 = s + c
        Sum2 = m + c
        #for i in range(3):
        ar.append(Sum1)
        ar.append(Sum2)     
        
        return ar
        

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        matrix = [[0 for j in range(n)] for i in range(n)]
        line1 = [int(x) for x in input().strip().split()]

        k=0
        for i in range(n):
            for j in range (n):
                matrix[i][j]=line1[k]
                k+=1
        obj = Solution()
        ans = obj.sumTriangles(matrix, n)
        for i in ans:
            print(i,end=" ")
        print()
# } Driver Code Ends