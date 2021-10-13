#https://www.hackerrank.com/challenges/drawing-book/problem

def pageCount(n, p):
    # Write your code here
    if not n%2:
        n += 1
    return min(p//2, (n-p)//2)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    p = int(input().strip())

    result = pageCount(n, p)

    fptr.write(str(result) + '\n')

    fptr.close()
