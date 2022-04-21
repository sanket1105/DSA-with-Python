
## dictionary
## its just a key value pair.
## all the keys should be unique

monthConversion = {
    "jan":"january", 
    "feb":'february',
     "mar":"march"
     }

print(monthConversion['jan'])
print(monthConversion.get("jan"))


print("################################################")
print("########################################")

print("if the values isnt in the dict, it should print the default value \n")

print(monthConversion.get("dec","not a valid key to dict"))

print("################################################")
print("########################################")


## while loop:

i = 1
while i<=10:
    print(i)
    i += 1

print("################################################")
print("########################################")

## guessing word game


secret_word = "giraffe"
guess = ""
k = 2
guess_count = 1
out_of_guesses = False

print(" guess the word within 2 guesses ")
while guess != secret_word and not(out_of_guesses):
    if guess_count <= k:
        guess = input("enter guess :")
        guess_count += 1

    else:
        out_of_guesses = True

if out_of_guesses: print(" you lose")
else : print(" you win")
        
print("################################################")
print("########################################")

## For loops

for letters in "Giraffe":
    print(letters)  ## prints each letter in seperate line

for letters in "Giraffe":
    print(letters,end=" ")    ## prints output in the same line
print("\n")
friends = ['Sanket','Zanwar',"nanded"]
for i in friends:
    print(i)    

for index in range(10):
    print(index, end= " ")

print("\n")

for index in range(3,10):
    print(index, end=" ")
print("\n")

for i in range(len(friends)):
    print(i,end=" ")
    print(friends[i])    

print("#############################################")

friend = ['Sanket','Zanwar','Nanded']
for i in range(len(friend)):
    print(i,friend[i])


print("#####################################")
print("###################################")
## exponent function  


def pow_num(n1,power):
    result = 1
    while(power>0):
        result = result*n1
        power -= 1

    return result 
print(" answer of exponent defination is : ")
print(pow_num(2,3))



