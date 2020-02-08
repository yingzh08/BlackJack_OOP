'''
This file creates the human_player class.
'''

from modules.submodules.players_hand import PlayersHand

class ComputerDealer(PlayersHand):
    """A computer dealer
    
    Attributes:
        money_account: computer dealer's money account
        received_bet: computer dealer's received bet at each run. 

    Imported Attributes from PlayersHand:
        current_hand: a list of cards that are currently in player's hands
        points: the total number of points from player's hand.
        bust: True or False for busting. If the player's hand is busted, player 
              automatically loses
    
    Methods:
        receive_bet: receives bet from players. 
        next_move: add a card if the points haven't reached 21. Otherwise, stop.
        lose_bet: computer dealer loses the game. return double bet to player
        collect_bet: dealer wins the game. collect the bet. deposit it into money_account
        tie_return: dealer returns the bet amount. Game is a tie.    
        count_points: count points method. Similar to the one from method players_hand. 
                      However, this method will automatically assign a value to 'A', it 
                      will choose whatever is most benefitial for it.
    
    Imported Methods:
    """
    # Object Attribute
    def __init__(self,money_account = 0, received_bet = 0):
        self.money_account = money_account
        self.received_bet = received_bet
        PlayersHand.__init__(self)

    # Methods
    def receive_bet(self, bet_amount):
        ''' Keep the player's bet in a separate account (on the table) during the game.
        At the moment, this function is tailored to games with one Human Player only. 
        '''
        self.received_bet = bet_amount
    
    def next_move(self,deck):
        ''' Computer dealer's turn. add a card if the points haven't reached 21. Otherwise, stop. '''
        if self.points <= 21:
            self.current_hand.append(deck.pop())
    
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

    def count_points(self):
        """Count the total points currently in the dealer's hand. generate 'bust' alert
        if the total points has exceed 21.
        
        Cards 'J', 'Q', and 'K' are counted as 10s
        Card 'A' can either be counted as '1' or '11'. Choose automatically to result
        in the higher score.
        """
        self.points = 0
        for i in range(0,len(self.current_hand)): 
            if self.current_hand[i] != 'J' and self.current_hand[i] != 'Q' and self.current_hand[i] !='K' and self.current_hand[i] != 'A':
                self.points += self.current_hand[i]

            elif self.current_hand[i] == 'J' or self.current_hand[i] == 'Q' or self.current_hand[i] == 'K':
                self.points = self.points + 10

            elif self.current_hand[i] == 'A':
                test_points = self.points + 11
                if test_points > 21:
                    self.points = self.points + 1
                else:
                    self.points = test_points
        if self.points > 21:
            self.bust = True
