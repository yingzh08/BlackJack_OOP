'''
This file creates a computer dealer class.
'''
import random

class ComputerDealer:
    """A computer dealer
    
    Attributes:
        ID: shows the unique ID of the generated computer dealer
        money_account: computer dealer's money account
        received_bet: computer dealer's received bet at each run. 
        current_hand: a list of cards that are currently in player's hands
        current_points: the total number of points from player's hand.

        
    Methods:
        receive_bet: receives bet from players. 
        next_move: add a card if the points haven't reached 21. Otherwise, stop.
        points: return points Similar to the one from method players_hand. 
                      However, this method will automatically assign a value to 'A', it 
                      will choose whatever is most benefitial for it.
        bust: Return True if busted
        lose_bet: computer dealer loses the game. return double bet to player
        collect_bet: dealer wins the game. collect the bet. deposit it into money_account
        tie_return: dealer returns the bet amount. Game is a tie.    
    
    
    
    """
    # Object Attribute
    def __init__(self):
        self.ID = random.randint(10,99)
        self.money_account = 0
        self.received_bet = 0
        self.current_hand = []
        self.current_points = 0
        

    # Methods
    def receive_bet(self, bet_amount):
        ''' Keep the player's bet in a separate account (on the table) during the game.
        At the moment, this function is tailored to games with one Human Player only. 
        '''
        self.received_bet = bet_amount
    
    def deal_cards(self,deck):
        '''Deals cards from the deck. Update both the dealer's hand and the deck.
        
        input: 
            deck: list. card deck
        '''
        for i in range(0,2):
            self.current_hand.append(deck.pop())
    
    def next_move(self,deck):
        ''' Computer dealer's turn. add a card if the points haven't reached 21. Otherwise, stop. '''
        if self.current_points < 21:
            print("Dealer hasn't reached 21. One more card added to dealer's hand")
            self.current_hand.append(deck.pop())
            print(f"Dealer's current hand is:{self.current_hand}")
        else:
            print("Dealer has already reached 21. No more cards added.")

    def points(self):
        """Count the total points currently in the dealer's hand. generate 'bust' alert
        if the total points has exceed 21.
        
        Cards 'J', 'Q', and 'K' are counted as 10s
        Card 'A' can either be counted as '1' or '11'. Choose automatically to result
        in the higher score.
        """
        points = 0
        count_A = 0
        for i in range(0,len(self.current_hand)): 
            if self.current_hand[i] != 'J' and self.current_hand[i] != 'Q' and self.current_hand[i] !='K' and self.current_hand[i] != 'A':
                points += self.current_hand[i]

            elif self.current_hand[i] == 'J' or self.current_hand[i] == 'Q' or self.current_hand[i] == 'K':
                points += 10

            elif self.current_hand[i] == 'A':
                points += 11
                count_A += 1
                
        while points > 21 and count_A > 0:
            for num in range(0,count_A):
                points -= 10
        
        self.current_points = points
        
        return points

    def bust(self):
        '''Return True if the dealer busts.'''
        bust = False
        if self.current_points > 21:
            bust = True
        
        #return bust status directly when calling this method 
        return bust
            
    def lose_bet(self):
        ''' Computer dealer pays the human player double. Received bet clears to 0.'''
        self.money_account -= self.received_bet
        self.received_bet = 0

    def collect_bet(self):
        ''' dealer wins the game. collect the bet.'''
        self.money_account += self.received_bet
        self.received_bet = 0

    def tie_return(self):
        ''' there is a tie in the game. dealer returns the original bet amount.'''
        self.received_bet = 0
