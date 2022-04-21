
# print(" How to take input in python :")
# name = input("enter your name")
# print("hello "+name)


## when you are taking input, the inputs type becomes string

# num1 = input("enter first number :")
# num2 = input("Enter second number :")
# result = int(num1) + int(num2)
# print(result)


## but what if the input numbers are floating point numbers

# num1 = input("enter first number :")
# num2 = input("Enter second number :")
# result = float(num1) + float(num2)
# print(result)


print("######################################################")
print("###############################################")
 
## lists :

friends = ['a','b',"dk",2,3,True,"Shankii"]
print(friends)
print(friends[0])

print("entries from the back: ")
print(friends[-1])

print(friends[1:3])

print("changing the entries in list :")
friends[1] = "Sanket"
print(friends)
 

lucky_numbers = [4,8,15,16,23,42]

print("######################################################")
print("###############################################")


print("Adding two lists using extend function :") ## just do friends + lucky_numbers, just inplace==False in this + operator
friends.extend(lucky_numbers) ## by default, inplace==True in this
print(friends) 


a1 = [1,2,'a']
a2 = [4,5]
print(a1+a2)  ## inplace for a1==False
print(a1)

print("######################################################")
print("###############################################")

print("adding the element at the end of the list usiing append:")
friends.append("Zanwar")
print(friends)

print("######################################################")
print("###############################################")


print("inserting the element at the particular index :")
friends.insert(1,"list")
print(friends)

print("######################################################")
print("###############################################")

print(" removing the element from the list:")
friends.remove("Sanket")
print(friends)

print("######################################################")
print("###############################################")

print("remove function when 2 entries are same in the lisst")
friends.append("dk")
print(friends)

print("######################################################")
print("###############################################")

friends.remove("dk")  ## removes the first occurence of the word given to remove
print(friends)

print("######################################################")
print("###############################################")

print(" deleeting the entries of the lists")
friends.clear()
print(friends)

print("######################################################")
print("###############################################")

friends=['a','b',1,2,3,'b']
print("deleting the elements one by one from the last")
friends.pop()
print(friends)

print("######################################################")
print("###############################################")

print("getting index of the entry of b")
print(friends.index('b'))

print("######################################################")
print("###############################################")

friends = ['b','a','b','Sanket','Zanwar']
print("number of times b appear in lists")
print(friends.count('b'))


print("######################################################")
print("###############################################")

print("sorting the list")
friends.append('9')
print(friends)
friends.sort()  ## intergers, Capital letters, then small letters : priority while sorting
print(friends)


print("######################################################")
print("###############################################")

print("reversing the lucky numbers")
lucky_numbers.reverse()
print(lucky_numbers)

print("######################################################")
print("###############################################")

print("copying the list")
friends_2 = friends.copy()
print(friends_2)