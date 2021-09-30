#Given two sorted arrays of distinct elements. There is only 1 difference between the arrays. First array has one element extra added in between. Find the index of the extra element.

class Solution:
    def findExtra(self,a,b,n):
        #add code here
        c = 0
        for i in range(n):
            
            c = a[i]
            
        #return i
        
            for j in range(len(b)):
                
                if c != b[j]:
                    
                    o = i
                    
                else:
                    
                    continue
        print(o)        
        return o

#{ 
#  Driver Code Starts
if __name__ == "__main__":
    t=int(input())
    for i in range(t):
        n=int(input())
        a=list(map(int,input().split()))
        b=list(map(int,input().split()))
        print(Solution().findExtra(a,b,n))
# } Driver Code Ends