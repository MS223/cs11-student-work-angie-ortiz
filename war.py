import random
p1_score = 0
p2_score= 0

player_one= raw_input("Player One's Name: ")
player_two= raw_input("Player Two's Name: ")
# shuffled_deck: will return a shuffled deck to the user
#output: a list representing a shuffled deck
def shuffled_deck():
    basic_deck = range(2, 15)* 4
    random.shuffle(basic_deck)
    return basic_deck
deck= shuffled_deck()
def player_turn(player_name):
    card= deck.pop()
    print player_name, 'drew card', str(card)
    return str(card)

while len(deck) > 0: #this can only work if there are more than 0 elements
    print len(deck)
    card= player_turn(player_one)
    card1=player_turn(player_two)
    if card > card1:
        print "Player One Wins!"
        p1_score= p1_score + 1

    elif card < card1:
        print "Player Two Wins!"
        p2_score= p2_score + 1

    else:
        print "Tie!"

print "Player One's Score: " + str(p1_score)
print "Player Two's Score: " + str(p2_score)



