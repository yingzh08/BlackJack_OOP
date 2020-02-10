'''
This file creates the human_player class.
'''

import random

class HumanPlayer:
    """Create a human player class
    
    Attributes:
        ID: shows the unique ID of the generated human player. 
        money_account: the current amount of money the player owns. 
                       Player has $50 in the money_account as a default.
        bet_amount: the amount of money currently being betted in the game.
        current_hand: a list of cards that are currently in player's hands.
        current_points: the total number of points from player's hand.
    
    Methods:
        deposit: deposit 10 dollars into account if the player's account 
                 balance is 0. Option available at the end of the game.
        place_bet: player place bet (subtracted from money account). bet_amount gets updated.
        deal_cards: create an initial list of cards that are in a player's hand when the cards are dealt.
        next_move: player's choice of play. Either choose hit or stand. If chosen hit, player
                     receives a new card. update hands and update points. If player chooses 'stand'. 
                     skip his turn. points and hands remain the same.
        points: return the points of player's current hand
        bust: return True if player has gone bust. 
        lose_bet: player lost all bet. bet_amount clears to 0.
        win_double: player wins the game. the betted amount doubles and gets deposited
                    into player's money_account.
        tie_return: game is a tie. Player gets back his or her original bet.


    """
    
    # Object attributes
    def __init__(self):
        '''Return a new human player object'''
        self.ID = random.randint(100,999)
        self.money_account = 0
        self.bet_amount = 0
        self.current_hand = []
        self.current_points = 0
    
    # Methods
    def deposit(self, amount):
        """deposit: deposit dollars into account if the player's account.
        """
        self.money_account += amount
        print(f'{amount} dollars have been deposited.')
    
    def place_bet(self):
        """Ask user to place bet as a integer. The amount automatically gets withdrawn
        from the user's money_account."""
        while True:
            try:
                self.bet_amount = int(input(f' Your current account balance is {self.money_account}.\
                Please place bet (in dollars):'))
            except ValueError:
                print('Please enter whole number only.')
                continue
            else:
                if self.bet_amount > self.money_account:
                    self.bet_amount = int(input(f'Please only place bet that you can afford.\
                    Your current account balance is {self.money_account}:'))
                else:
                    break
        print(f'You have placed a bet of {self.bet_amount} dollars')
        #subtract bet from money account
        self.money_account = self.money_account - self.bet_amount

    def deal_cards(self,deck):
        '''Deals cards from the deck. Update both the player's hand and the deck.
        
        input: 
            deck: list. card deck
        '''
        for i in range(0,2):
            self.current_hand.append(deck.pop())

    def next_move(self,deck):
        '''Player chooses either to hit or stand. If chosen hit, receive one more card from the
        bottom of the deck and place it on the players_hand. If chosen stand, receive no card. 
        player skips the turn.
        '''
        while True: 
            play = input('Human Player: hit or stand?')
            if play == 'hit':
                self.current_hand.append(deck.pop())
                print('Hit me!')
                break
            elif play == 'stand':
                print('Human Player skips the turn. No actions taken.')
                break
            else:
                print("Please provide valid answer. Type 'hit' or 'stand'.")

    def points(self):
        """Count the total points currently in the player's hand. generate 'bust' alert
        if the total points has exceed 21.
        
        Cards 'J', 'Q', and 'K' are counted as 10s
        Card 'A' can either be counted as '1' or '11'. Ask player when that happens. 
        """
        points = 0
        for i in range(0,len(self.current_hand)): 
            if self.current_hand[i] != 'J' and self.current_hand[i] != 'Q' and self.current_hand[i] !='K' and self.current_hand[i] != 'A':
                points += self.current_hand[i]

            elif self.current_hand[i] == 'J' or self.current_hand[i] == 'Q' or self.current_hand[i] == 'K':
                points += 10

            elif self.current_hand[i] == 'A':
                try:
                    A_choice = int(input('Would you like A to be 1 or 11?'))
                except ValueError:
                    A_choice = int(input('Please enter numbers only. Would you like A to be 1 or 11?'))
                else:
                    points += A_choice
        
        # stored the points value for later use
        self.current_points = points
        
        #return points directly when calling this method
        return points
        

    def bust(self):
        '''Return True if the player busts.'''
        bust = False
        if self.current_points > 21:
            bust = True
        
        #return bust status directly when calling this method 
        return bust
    
    def lose_bet(self):
        '''player lost all bet. bet_amount clears to 0'''
        print(f'Human player lost a bet of {self.bet_amount} dollars')
        self.bet_amount = 0

    def win_double(self):
        '''player wins double the amount he or she bet for'''
        print(f"Human player won {self.bet_amount*2}")
        self.money_account += self.bet_amount*2
        self.bet_amount = 0 

    def tie_return(self):
        '''game is a tie. Player gets back his or her original bet.'''
        self.money_account += self.bet_amount
        self.bet_amount = 0
    
