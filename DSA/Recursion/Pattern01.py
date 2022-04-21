
def pattern(rows,columns):
    if rows==0: return 

    if rows>columns:
        print("* ",end=" ")
        pattern(rows,columns+1)


    else:
        print("")
        pattern(rows-1,0) 

pattern(4,0)