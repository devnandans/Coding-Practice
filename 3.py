# Q 3. https://practice.geeksforgeeks.org/problems/rotate-array-by-n-elements/0
# Given a non null integer matrix Grid of dimensions NxM.Calculate the sum of its elements.

#User function Template for python3

class Solution:
    def sumOfMatrix(self,N,M,Grid):
        solu = 0
        for i in range(N):
            
            for j in range(M):
                
                solu = solu + Grid[i][j]
                
        return solu
                
                
        return sum

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        N,M=map(int,input().strip().split(' '))
        Grid = [[0 for i in range(M)] for j in range(N)]
        for i in range(N):
            s=list(map(int,input().strip().split(' ')))
            for j in range(M):
                Grid[i][j]=s[j]
        ob=Solution()
        print(ob.sumOfMatrix(N,M,Grid)) 
# } Driver Code Ends
