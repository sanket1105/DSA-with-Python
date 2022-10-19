

## reverse the sentence

stack = []
s = 'Hey, I am Sanket.'

n = len(s)
temp = ""
for i in range(n):
    if s[i]==" ":
        stack.append(temp)
        temp = " "
    else:
        temp += s[i]   

## for last word
stack.append(temp)

while len(stack)>0:
    print(stack.pop(),end=" ")





