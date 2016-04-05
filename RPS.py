import random
list = ['rock', 'paper', 'scissors']
choice = random.choice(list)
print "Rock, paper, scissors say shoot"
user= raw_input("User: ")
print "Computer: " + choice
while user == choice:
    print "Tie!"
    print "Rock, paper, scissors say shoot"
    user= raw_input("User: ")
    choice = random.choice(list)
    print "Computer: " + choice
    #I need an else or elif
