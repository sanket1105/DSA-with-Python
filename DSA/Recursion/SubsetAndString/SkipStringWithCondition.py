
## only skip 'app' if its not 'apple'

a = 'appsanketappleapp'

def skipStringWithCondition(a):
    if len(a)==0:
        return ""

    if a.startswith('app') and not a.startswith('apple'):
        return  skipStringWithCondition(a[3:])
 
    else: 
       return  a[0] + skipStringWithCondition(a[1:])

print(skipStringWithCondition(a))
