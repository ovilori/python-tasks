#this program imports the deck_module (both files are in the same folder)

#importing the module
import deck_module

#calling the function create_deck() from the deck_module
my_cards = deck_module.create_deck()

#printing each cards from my_cards
for card in my_cards:
    print(card)

#printing the deck of cards as a list
print(my_cards)
#printing the no of items in the list
print(len(my_cards))

#deck_module reproduced below:
#def create_deck():
    #suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
    #ranks = ['Ace','2','3','4','5','6','7','8','9','10', 'Jack', 'Queen', 'King']
    #deck_of_cards = []

    #for suit in suits:
        #for rank in ranks:
           #deck_of_cards.append(f'{rank} of {suit}')
            
    #return deck_of_cards