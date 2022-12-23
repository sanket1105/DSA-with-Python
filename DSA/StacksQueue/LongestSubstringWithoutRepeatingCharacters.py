
a = 'abcabcbb'
seen = ""
maxl = 0

for i in a:
    if i in seen:
        seen = seen[seen.index(i)+1:] + i
    else:
        seen+=i

    maxl=  max(maxl,len(seen))

print(maxl)



     