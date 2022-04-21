## Drawing a picture
print("    /|")
print("   / |")
print("  /  |")
print(" /   |")
print("/    |")

print("#########################################################")
print("##################################################")


## Changing the name and the age in the text with builtin function
## its just basically concatenation of the strings

character_name = "John"
character_age = "35"
print("There was a man once named " + character_name + ", ")
print("he was "+ character_age + " yrs old. ")
print("He really liked the name " + character_name + ",")
print("but he didn't like being "+ character_age +".")

## so instead of changing the name by moving into the statement, just change the variable name

## suppose halfway through, you wish to change the name


print("##################################################")
print("##################################################")


print("There was a man once named " + character_name + ", ")
print("he was "+ character_age + " yrs old. ")

character_age="95"
character_name="Mary"
print("He really liked the name " + character_name + ",")
print("but he didn't like being "+ character_age +".")

print("##########################################################")
print("##################################################")

print("Sanket Zanwar")
print("Sanket\nZanwar")
print("Sanket\"Zanwar") ## the second " will act like it is the ending of the quotation marks, so use \" to let see it not the closing actually

phrase='Sanket Zanwar'
print(phrase + " is cool")

print("In lower case :"+ phrase.lower()) 
print("In upper case :"+ phrase.upper()) 

print(" is string in upper :")
print(phrase.isupper())  ## phrase : Sanket Zanwar : Neither lower, neither upper
print(phrase.islower())

print(phrase.upper().isupper())


print("length of string: ")
print(len(phrase))

print("first character of string : " + phrase[0])
print("'t' in string is at index: ")
print(phrase.index('t'))

print(" where the particular sub-string starts inside the string:")
print(phrase.index("ank"))

print("replace function :")
print(phrase.replace("Sanket","Mr. Sanket")) ## inplace==False in replace function

phrase = phrase.replace("Sanket","Replaced Sanket")  ## same as making inplace==True
print("phrase is : "+ phrase)


