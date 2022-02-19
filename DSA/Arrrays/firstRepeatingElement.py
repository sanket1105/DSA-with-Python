global n
k = [3,7,5,4,1,8,8]
n = 1e6+2
print(n)

temparr = [-1]*int(n)
intmax = n

for i in range(len(k)):
    s = k[i]
    if temparr[s] == -1:
        temparr[s] = i
    else:
        intmax = min(temparr[s],i)

if intmax == n:
    print("No double occurence of any number")
else:
    print("first occurence of most occuring number is: ")
    print(intmax)