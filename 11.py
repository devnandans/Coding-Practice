#User function Template for python3
# Q . Print first letter of every word in the string

# https://practice.geeksforgeeks.org/problems/print-first-letter-of-every-word-in-the-string3632/1/?difficulty[]=-1&page=3&query=difficulty[]-1page3#
class Solution:
	def firstAlphabet(self, S): 
	    st = ""
	    st=st+S[0]
        for i in range(len(S)):
        
		    
		    #st = ""
		    
		    #print(st[0])
            if S[i] == " ":

                st = st + S[i+1]
        
        return st
#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		S = input()
		ob = Solution()
		answer = ob.firstAlphabet(S)
		
		print(answer)


# } Driver Code Ends