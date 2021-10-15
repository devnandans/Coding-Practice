#https://www.hackerrank.com/challenges/apple-and-orange/problem?h_r=profile

def countApplesAndOranges(s, t, a, b, apples, oranges):
    
    count = 0
    for i in  apples:
        if (a+i)>=s and (a+i)<=t:
            count += 1
    print(count)
    count = 0
    for i in  oranges:
        if (b+i)>=s and (b+i)<=t:
            count += 1
    print(count)
    
    

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    s = int(first_multiple_input[0])

    t = int(first_multiple_input[1])

    second_multiple_input = input().rstrip().split()

    a = int(second_multiple_input[0])

    b = int(second_multiple_input[1])

    third_multiple_input = input().rstrip().split()

    m = int(third_multiple_input[0])

    n = int(third_multiple_input[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
