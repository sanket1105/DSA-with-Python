
## if apple is there in string, skip it

a = 'applesanappleketapple'

def skipApple(a):
    if len(a)==0:
        return ""

    if a.startswith('apple'):
        return skipApple(a[5:])
    else:
        return a[0] + skipApple(a[1:])  

print(skipApple(a))              