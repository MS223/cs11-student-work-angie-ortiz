# what does this function return ?
def print_only(x):
   y = x * 2
   print y
print_only(1) #this function returns the value of any number * 2

how is this one different ?
def return_only(x):
   y = x * 2
   return y
return_only(1) #the return is not showing me anything, only the print function can do so


def print_only(x):
   y = x * 2
   print y
print "running print_only ..."
print_only(7) #it is printing 14 which is the result of the parameter * 2

def return_only(x):
   y = x * 2
   return y
print "running return_only ..."
return_only(7) #it is printing running return_only because prints allows the user to see what the computer is doing, but I am not getting any value


def print_only(x):
   y = x * 2
   print y
print "printing print_only ..."
print print_only(7) #it is printing the function but it's printing none

def return_only(x):
   y = x * 2
   return y
print "printing return_only ..."
return_only(7) #I am not getting a value

def print_only(x):
   y = x * 2
   print y
print "using print_only ..."
print_only(7) + 6 #there is an error when it tries to add the 6 to the result of the parameter within the function
you can't add to a print

def return_only(x):
   y = x * 2
   return y
print "using return_only ..."
return_only(7) + 6 #it doesn't show me any error as the previous one
#you can add when you return
