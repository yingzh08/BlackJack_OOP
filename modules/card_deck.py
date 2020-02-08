'''
This file defines the object class --> card deck. 
'''
import random

class CardDeck:
    '''Create an instance of a card deck.
    
    Attributes: 
        deck: shows the list of cards in the deck
        deckID: shows a 4-digit ID of the current deck being played. 
    
    Methods:
        new_deck = create a new 52 card deck
        shuffle_deck = shuffle the current 54 card deck'''
    
    # Object attributes
    def __init__(self,deck=list(), deckID = ''):
        self.deck = deck
        self.deckID = deckID
    
    # Methods for creating a new card deck
    def new_deck(self):
        '''create a new 52 card deck. Attach an unique ID to this deck.
        '''
        # create new card deck
        deck_unique = ['A',2,3,4,5,6,7,8,9,10,'J','Q','K']
        deck = list()
        for item in deck_unique:
            for num in range(0,4):
                deck.append(item)
        random.shuffle(deck)
        self.deck = deck

        # generate a 4-digit deck ID
        for num in range(0,4):
            self.deckID += str(random.randint(1,9))

        print(f"New deck created. The current deck's ID is {self.deckID}.")
            
    def shuffle_deck(self):
        '''Take in an existing deck of cards. reshuffle them upon request. 
        Operations will be done on the existing deck of cards. no new deck will be created.
    
        '''
        random.shuffle(self.deck)
        print('Deck shuffled.')
