import random

def mystery_function(x, y):
    random_number = random.randint(0,2) # What's the range of randoms?
    if random_number > 0: # What's the probability that random_number is greater than 0?
        z = x + y
    else:
        z = x * y
    return z
mystery_function(1, 2) 
#nothing happens when you run it
print mystery_function(1,2) 
#my first try was to put print mystery_function without any parameters and that didn't work
