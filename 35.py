#https://www.hackerrank.com/challenges/strong-password/problem

def minimumNumber(n, password):
    # Return the minimum number of characters to make the password strong
    
    count=0
    if n<6:
        count = 6-n
    return count

    else:
        for i in range(n):
            if any password[i].isdigit() == False:
                
                count+=1
                
                
            if any password[i].isupper() == False:
                
                count+=1
                
            
            if any password[i].islower() == False:
                
                count+=1
            
            if any password[i]."!@#$%^&*()-+" == False:
                
                count+=1
                
    return count
     
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    password = input()

    answer = minimumNumber(n, password)

    fptr.write(str(answer) + '\n')

    fptr.close()
