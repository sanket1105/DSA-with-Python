
## since chinese chef does all what teh chef does
## so instead of copying the traits, just inherit the class

from Chef import Chef

class ChineseChef(Chef): 

    ## will have all the object defined functions from chef into chinese chef class
    ## fried rice is the extra trait
    
    ## overwriting the make_special_dish function

    def make_special_dish(self):
        print("can make fried rice")

    def proper_dish(self):
        print(" yes he can make")    