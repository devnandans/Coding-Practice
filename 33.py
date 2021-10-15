'''
Q .The Utopian Tree goes through 2 cycles of growth every year. Each spring, it doubles in height. Each summer, its height increases by 1 meter.

A Utopian Tree sapling with a height of 1 meter is planted at the onset of spring. How tall will the tree be after  growth cycles?

For example, if the number of growth cycles is N = 5, the calculations are as follows:

'''

def utopianTree(n):
    
    

    if n == 0:
        
        return 1
    else :
        H=1
        for j in range(1,n):
            
            if not j%2:
                H = H*2
            else :
                H = H+1
        return H
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        result = utopianTree(n)

        fptr.write(str(result) + '\n')

    fptr.close()
