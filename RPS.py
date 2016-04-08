import random
list = ['rock', 'paper', 'scissors'] #the game is meant for a user and computer to pick either r,p,s so I knew I had to make a list
choice = random.choice(list) #the random item should be chosen from the list
print "Rock, paper, scissors say shoot"
user= raw_input("User: ")
print "Computer: " + choice
while user == choice: #if it's a tie, then you go again until someone wins
    print "Tie!"
    print "Rock, paper, scissors say shoot"
    user= raw_input("User: ")
    choice = random.choice(list)
    print "Computer: " + choice
if user == "rock" and choice == "scissor" or user == "paper" and choice == "rock" or user == "scissors" and choice == "paper": #this helps determine when the user wins
    print "User wins"
else: #this helps determine when the user loses
    print "Computer wins"
