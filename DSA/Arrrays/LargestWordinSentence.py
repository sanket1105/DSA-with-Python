
s = "I am SanketZ"

res = 0
length = 0
for i in range(len(s)):
    if s[i]!=" ":
     length+=1
    else:
        res = max(res,length) 
        length=0 

res = max(res,length)
print(res)
    