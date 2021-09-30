// Implement a Lexical Analyzer in C.

#include<string.h>
#include<ctype.h>
#include<stdio.h>
main()
{
    FILE *f1;
    
    printf("\nEnter the c Program: ");
    f1=fopen("input","w");
    while((c=getchar())!=EOF)
        putc(c,f1);
    fclose(f1);
    
    while(ch = getc(f1)!=EOF)
    {
        while(1){
            
            state = 0;
            
            switch(state)
            {
                case 0 :    if(ch == "<")
                            state = 1 
                        
                            if(ch == ">") 
                        
                            state = 5
                            
                            if(ch == "=") 
                        
                            state = 8
                            
                            if(ch == letter) 
                        
                            state = 10
                            
                            if(ch == "+") 
                        
                            state = 12
                            
                            if(c=="-") 
                        
                            state = 15
                            
                            if(c=="*") 
                        
                            state = 18
                            
                            if(c=="/") 
                        
                            state = 19
                            
                            if(c=="%") 
                        
                            state = 20
                        
            }   
            
        }
    }