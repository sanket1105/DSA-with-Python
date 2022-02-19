


keypad = [".","abc","def","ghi","jkl","mno","pqrs","tu","vwx","yz"]

def printComb(str,idx,Combinations1):

    if idx==len(str):
        print(Combinations1)
        return
    currChar = str[idx]
    mapping = keypad[int(currChar) - int('0')]

    for i in range(len(mapping)):
        printComb(str,idx+1,Combinations1+mapping[i])

printComb('23',0,"")        