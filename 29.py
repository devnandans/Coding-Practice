#https://www.hackerrank.com/challenges/taum-and-bday/problem
#
import math
import os
import random
import re
import sys



def taumBday(b, w, bc, wc, z):
    # Write your code here
    for _ in range(input()):
        b, w = map(int, raw_input().split())
        bc, bw, z = map(int, raw_input().split())
        print min(b * bc + w * wc, bc * (b + w) + w * z, wc * (b + w) + b * z)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(raw_input().strip())

    for t_itr in xrange(t):
        first_multiple_input = raw_input().rstrip().split()

        b = int(first_multiple_input[0])

        w = int(first_multiple_input[1])

        second_multiple_input = raw_input().rstrip().split()

        bc = int(second_multiple_input[0])

        wc = int(second_multiple_input[1])

        z = int(second_multiple_input[2])

        result = taumBday(b, w, bc, wc, z)

        fptr.write(str(result) + '\n')

    fptr.close()