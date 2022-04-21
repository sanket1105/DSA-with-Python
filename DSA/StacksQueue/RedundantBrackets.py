
a = "(a+(b)/c)"
stack  =[]
open = ['(','{','[']
close = [')','}',']']
keys = ['+','-','*','/']

def redundant_checker(a):
    for i in a:
        if i in open or i in keys:
            stack.append(i)
        elif i in close:
            k = stack.pop()
            if k not in  keys:
                return True
                break
            elif k in keys:
                stack.pop()
    return False       

print(redundant_checker(a))

