#Given an array A of positive integers. Your task is to find the leaders in the array. An element of array is leader if it is greater than or equal to all the elements to its right side. The rightmost element is always a leader. 

class Solution:
    #Back-end complete function Template for Python 3
    
    #Function to find the leaders in the array.
    def leaders(self, A, N):
        #Code here
        maxi = A[N-1]
        ar = []
        #for i in range(N):
            
            #if A[i]>maxi:
                
                #maxi = A[i]
                
        for i in range(N-1,-1,-1):
            
            if A[i] > maxi:
                
                ar.append(A[i])
                
                maxi = A[i]
        
        ar.reverse()   
        
        return ar
#{ 
#  Driver Code Starts
#Initial Template for Python 3

import math


    
def main():
    
    T=int(input())
    
    while(T>0):
        
        
        N=int(input())
        
        A=[int(x) for x in input().strip().split()]
        obj = Solution()
        
        A=obj.leaders(A,N)
        
        for i in A:
            print(i,end=" ")
        print()
        
        T-=1

if __name__=="__main__":
    main()