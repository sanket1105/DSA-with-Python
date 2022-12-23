

open_list = ['{','(','[']
close_list = ['}',')',']']

def check(str):
    stack=[]
    for i in str:
        if i in open_list:
            stack.append(i)
        elif i in close_list:
            pos = close_list.index(i)

            if ((len(stack)>0) and (open_list[pos] == stack[len(stack)-1])):
                stack.pop()
            else:
                return "Unbalanced"

    if len(stack)==0: return "Balanced"
    else: return "Unbalanced"     

string = "{[]{()}}"
print(string,"-", check(string))
  
string = "[{}{})(]"
print(string,"-", check(string))
  
string = "((()"
print(string,"-",check(string))   
