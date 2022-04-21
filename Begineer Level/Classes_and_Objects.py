## classes and objects
'''
many things cannot be described using the existing data structures available
so we use classes and objects to make our new type of data struct to define the new variable

'''

## importing the Student file
## since we have define the class named student in the Student file
## lets imprt that

## class is waht defines the matter you wanna define
## object is that matter

from Student import student
  
## see the Student file to see the student class
## student1 is the object

student1 = student("jim","Business",3.04,False)

print(student1.name)
print(student1.gpa)
print(student1.is_on_probation)


print(student1.on_honor_roll())

print("########################################################")
print("########################################################")


## inheritance :
## inhert the attributes of previously defined object in the newly defined class


from Chef import Chef

mychef  = Chef()
mychef.make_salad()


## now lets define a chinese chef which does all the above mentin traits
## and has some extra traits too

print("chinese one")

from ChineseChef import ChineseChef

myChineseChef  = ChineseChef()
myChineseChef.make_special_dish()
myChineseChef.proper_dish()