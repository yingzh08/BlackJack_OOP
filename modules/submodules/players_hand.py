"""
This file creates a class for players' hand.
"""

class PlayersHand():
    """
    Create a class object of Player's Hand. 

    Attributes: 
        current_hand: a list of cards that are currently in player's hands
        points: the total number of points from player's hand.
        bust: True or False. If the points goes above 21, turns True.
    
    Methods:
        deal_cards: create an initial list of cards that are in a player's hand when the cards are dealt.
        count_points: calculate the total points given the current hand
    """

    # Object attributes
    def __init__(self, current_hand = list(), points = 0, bust = False):
        self.current_hand = current_hand
        self.points = points
        self.bust = bust

    # Methods
    def deal_cards(self,deck):
        '''Deals cards from the deck. Update both the player's hand and the deck.
        '''
        current_hand = list()
        for i in range(0,2):
            current_hand.append(deck.pop())
        self.current_hand = current_hand

    def count_points(self):
        """Count the total points currently in the player's hand. generate 'bust' alert
        if the total points has exceed 21.
        
        Cards 'J', 'Q', and 'K' are counted as 10s
        Card 'A' can either be counted as '1' or '11'. Ask player when that happens. 
        """
        self.points = 0
        for i in range(0,len(self.current_hand)): 
            if self.current_hand[i] != 'J' and self.current_hand[i] != 'Q' and self.current_hand[i] !='K' and self.current_hand[i] != 'A':
                self.points += self.current_hand[i]

            elif self.current_hand[i] == 'J' or self.current_hand[i] == 'Q' or self.current_hand[i] == 'K':
                self.points = self.points + 10

            elif self.current_hand[i] == 'A':
                try:
                    A_choice = int(input('Would you like A to be 1 or 11?'))
                except ValueError:
                    A_choice = int(input('Please enter numbers only. Would you like A to be 1 or 11?'))
                else:
                    self.points = self.points + A_choice
        if self.points > 21:
            self.bust = True

