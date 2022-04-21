
## __init__ is initialize function
## lets create a student datatype

class student:
    def __init__(self, name, major, gpa, is_on_probation):
        self.name = name
        self.major = major
        self.gpa = gpa
        self.is_on_probation = is_on_probation

    ## class function
    def on_honor_roll(self):
        if self.gpa >=3.5:
            return True
        else : return False    



## self.name and rest all are the attributes of the class        
