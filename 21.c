// Implement a Lexical Analyzer in C.
/*
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
    */

   #include<stdio.h>
#include<string.h>
#include<ctype.h>
#include<stdlib.h>
int MAXLINE=10;
int main()
{
    char ch,word[30];
    char buffer[MAXLINE];
    char symbol[30][30],keyw[20][20]={"int","print","printf","float","main","char","long","double","if","else","for","while","void","do","switch","case","break"};
    int state=0,i,p=0,id,flag=0,k=0,m,wordlen,z;
   
    FILE *f,*fp,*fptr;
    f=fopen("c.c","r");
    
    while(1)
    {
        switch(state)
        {
            case 0:
                ch=fgetc(f);
                if(ch=='<')
                {
                    ch=fgetc(f);
                    if (ch=='=')
                        printf("<= - LE\n");
                    else if(ch=='>')
                        printf("<> - NE\n");
                    else 
                        {
                            printf("< - LT\n");
                            fseek(f,-1,SEEK_CUR);
                            state=0;
                        }
                }
                else if(ch=='>')
                {
                    ch=fgetc(f);
                    if (ch=='=')
                        printf(">= - GE\n");
                    else 
                        printf("> - GT\n");
                }
                else if(ch=='=')
                {
                    ch=fgetc(f);
                    if (ch=='=')
                        printf("== - EQ\n");          
                    else
                    {
                        printf("= - ASSIGN\n");
                        fseek(f,-1,SEEK_CUR);
                        state=0;
                    }                       
                }
                else if(isalpha(ch))
                    {   p=0;
                        word[p]=ch;
                        p++;
                        while(isalnum(ch=fgetc(f)))
                        {                        
                            word[p]=ch;p++;
                        }
                       
                        fseek(f,-1,SEEK_CUR);
                        word[p]='\0';
                        wordlen=p;
                        p=0;
                        for(i=0;i<14;i++)
                            if(strcmp(keyw[i],word)==0)
                            {
                                printf("%s - Keyword\n",word);
                                id=1;
                                break;
                            }
                        if(id==0)
                            {printf("%s - Identifier\n",word);
                                    fp=fopen("symboltable.txt","a");
                                    fputs(word,fp);
                                    fputs("\n",fp);
                                    fclose(fp);
                            }
                        state=0;
                        id=0;
                    }
                else if(ch=='+')
                {
                    ch=fgetc(f);
                    if (ch=='+')
                        printf("++ - INC\n");
                    else 
                        {
                            fseek(f,-1,SEEK_CUR);
                            printf("+ - PLU\n");
                        }
                }
                else if(ch=='-')
                {
                    ch=fgetc(f);
                    if (ch=='=')
                        printf("-= - DEC\n");
                    else 
                        printf("- - MIN\n");
                }
                else if(ch=='*')
                    printf("* - MUL\n");
                else if(ch=='/')
                    printf("/ - DIV\n");
                else if(ch=='%')
                    printf(" MOD\n");
                else if(isdigit(ch))
                    {
                        p=0;
                        word[p]=ch;
                        p++;
                        while(isdigit(ch=fgetc(f)))
                        {
                            word[p]=ch;
                            p++;
                        }
                        fseek(f,-1,SEEK_CUR);
                        word[p]='\0';
                        printf("%s - NUM\n",word);
                        p=0;
                    }
                else if(ch=='{')
                    printf("{ - Opening bracket\n");
                else if(ch=='}')
                    printf("} - Closing bracket\n");
            break;
            default: break;
                  
        }
        if(ch==EOF)
            break;
    }

    return 0;
}
%{
    #include<stdio.h>
%}
letter [A-Za-z]
digit [0-9]
%%
"int"|"printf"|"float"|"main"|"char"|"long"|"double"|"if"|"else"|"for"|"while"|"void"|"do"|"switch"|"case"|"break" {printf("\n%s -- KEYWORD",yytext);}
"{"|"}"|"("|")"|"["|"]" {printf("\n%s -- PARANTHESIS",yytext);}
{digit}* {printf("\n%s -- NUM",yytext);}
{letter}({letter}|{digit})* {printf("\n%s -- IDENTIFER",yytext);}
"==" {printf("\n%s -- EQU",yytext);}
";" {printf("\n%s -- DELIM",yytext);}
\".*\" {printf("\n%s -- STRING",yytext);}
"<=" {printf("\n%s -- LE",yytext);}
"<>" {printf("\n%s -- NE",yytext);}
"<" {printf("\n%s -- LT",yytext);}
">=" {printf("\n%s -- GE",yytext);}
">" {printf("\n%s -- GT",yytext);}
"=" {printf("\n%s -- ASSIGN",yytext);}
"++" {printf("\n%s -- INC",yytext);}
"+" {printf("\n%s -- PLU",yytext);}
"-=" {printf("\n%s -- DEC",yytext);}
"-" {printf("\n%s -- MIN",yytext);}
"*" {printf("\n%s -- MUL",yytext);}
"/" {printf("\n%s -- DIV",yytext);}


int main()
{
    FILE *fp;
    fp=fopen("var.c","r");
    yyin=fp;
    yylex();
    fclose(fp);
    return 0;
}