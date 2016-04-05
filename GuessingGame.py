guesses=1
user=raw_input("What is your name?")
highest_number=input("What's the highest number you would like to choose from:")
import random
answer=random.randint(0,highest_number)
guess= input("What's your guess?")
# print answer; this would give away the answer to the user
while guess != answer:
    if guess > answer:
        print "Too high"
        guess= input("What's your guess?")
        guesses= guesses+1
    else:
        # guess < answer; this is unnecesarry because the else part already knows that if it's not too high, then it's automatically too low.
        print "Too low"
        guess= input("What's your guess?")
        guesses= guesses+1
print "Your guess was correct!"
print "It took you " + str(guesses) + " tries"
