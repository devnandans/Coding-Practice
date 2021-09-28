#Q .  You are given two strings S1 and S2. You need to find weights of both strings and compare them. The weight of a string can be obtained by adding individual weights of the characters that make the string. The weight of individual characters are the position on which they occur in the english alphabets table; for eg, a has weight 1, z has weight 26.

t = int(input())
for i in range(t):
    
    s1 = input()
    s2 = input()
    c = 0
    s = 0
    for i in range(len(s1)):
        
        c = c + (ord(s1[i]) - 96)
        
    for i in range(len(s2)):
        
        s = s + (ord(s2[i]) - 96)
        
    if c > s:
        
        print("1")
        
    elif s > c:
        
        print("2")
        
    elif c == s:
        
        print("equal")