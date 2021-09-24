# Q. https://practice.geeksforgeeks.org/problems/rotate-array-by-n-elements/0/?problemType=full&page=1&sortBy=submissions&query=problemTypefullpage1sortBysubmissions

# Given an unsorted array arr[] of size N, rotate it by D elements (clockwise)

t = int(input())

for i in range(t):
    n,d = map(int,input().split())
    
    ar = list(map(int,input().split()))
    
    
    for i in range(d,n):
        
        
        print(ar[i],end=" ")
        
    for i in range(d):
        
        print(ar[i], end = " ")
    
    
    print(" ")