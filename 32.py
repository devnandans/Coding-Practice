#The factorial of the integer , written , is defined as:

#Calculate and print the factorial of a given integer.

def extraLongFactorials(n):
    f=1
    while(n>0):
        f=f*n
        n=n-1
        
    print(f)    
        
if __name__ == '__main__':
    n = int(input().strip())

    extraLongFactorials(n)