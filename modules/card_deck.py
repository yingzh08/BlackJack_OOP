'''
This file defines the object class --> card deck. 
'''
import random

class CardDeck:
    '''Create an instance of a card deck.
    
    Attributes: 
        deck: list of cards in an instance of card deck
        deckID: shows a 4-digit ID of the current deck being played. 
    
    Methods:
        new_deck = create a new 52 card deck
        shuffle_deck = shuffle the current 54 card deck'''
    
    # Object attributes
    def __init__(self):
        self.deck = []
        self.deckID = ''

        # create new card deck
        deck_unique = ['A',2,3,4,5,6,7,8,9,10,'J','Q','K']
        for item in deck_unique:
            for num in range(0,4):
                self.deck.append(item)
        random.shuffle(self.deck)

        # generate a 4-digit deck ID
        self.deckID = str(random.randint(1000,9999))
        print(f"New deck created. The current deck's ID is {self.deckID}.")
            
    def shuffle(self):
        '''Take in an existing deck of cards. reshuffle them upon request. 
        Operations will be done on the existing deck of cards. no new deck will be created.
    
        '''
        random.shuffle(self.deck)
        print('Deck shuffled.')
        
    def __str__(self):
        '''print the Card Deck object.'''
        return f"The current Deck ID is {self.deckID}. The current number of cards in the deck is: {len(self.deck)}."