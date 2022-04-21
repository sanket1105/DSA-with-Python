import random

feet_in_miles = 5280
meter_in_km = 1000
beatles = ['John lennon','Paul','George','Ringo']

## function to get the extension of the file

def get_file_ext(filename):
    return filename[filename.index(".")+1:]

## random number

def roll_dice(num):
    return random.randint(1,num)