
def pattern(rows,columns):
    if rows==0: return 

    if rows>columns:
        pattern(rows,columns+1)
        print("* ",end=" ")



    else:
        pattern(rows-1,0) 
        print("")


pattern(4,0)