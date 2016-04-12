import random
score = 0

player_one= raw_input("Player One's Name: ")
player_two= raw_input("Player Two's Name: ")
# shuffled_deck: will return a shuffled deck to the user
#input:
#output: a list representing a shuffled deck
def shuffled_deck():
    basic_deck = range(2, 54)
    random.shuffle(basic_deck)
    return basic_deck
deck= shuffled_deck()
def player_turn(player_name):
    card= deck.pop()
    print player_name, 'drew card', card
    return (card)

while len(deck) > 0:
    print len(deck)
    card= player_turn(player_one)
    card1=player_turn(player_two)
    if card > card1:
        print "Player One Wins!"
    elif card < card1:
        print "Player Two Wins!"


# compare_scores= deck.pop()
# while player_turn(player_one) or player_turn(player_two):
#
