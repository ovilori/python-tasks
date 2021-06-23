#this program lists every combination of suit and rank in a set of 52 cards.
#rather than print the card, adds the card to a list that represents a deck of cards.
#then, displays the number of cards in the deck by using the function that provides a count of items in the list.

import random
suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
ranks = ['Ace','2','3','4','5','6','7','8','9','10', 'Jack', 'Queen', 'King']
deck_of_cards = []
player_hand = []

for suit in suits:
    for rank in ranks:
        deck_of_cards.append(f'{rank} of {suit}')
        #print(deck_of_cards)
print(f'There are {len(deck_of_cards)} cards in the deck')
print('Dealing ...')

#randomly choose five cards to add to a player's hand by:
#creating a second list for the results of a deal,
#choose a card and add to the list that represents the player's hand,
#remove the card from the list that represents the deck.
#print out the number of cards in the list that represents the deck.
#finally, print out the cards in the player's hand.

while len(player_hand) < 5:
    player_hand = random.choices(deck_of_cards, k=5)
    for value in player_hand[:]:
        deck_of_cards.remove(value)
    print(f'There are {len(deck_of_cards)} cards in the deck')
print('Player has the following cards in their hand:')
print(player_hand)

