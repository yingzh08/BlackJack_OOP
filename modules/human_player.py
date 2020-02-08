'''
This file creates the human_player class.
'''

from modules.submodules.players_hand import PlayersHand

class HumanPlayer(PlayersHand):
    """A human player

    Attributes:
        money_account: the current amount of money the player owns. 
                       Player has $50 in the money_account as a default.
        bet_amount: the amount of money currently being betted in the game
    
    Imported Attributes from PlayersHand:
        current_hand: a list of cards that are currently in player's hands
        points: the total number of points from player's hand.
        bust: True or False for busting. If the player's hand is busted, player 
              automatically loses
    
    Methods:
        place_bet: player place bet (subtracted from money). bet_amount gets updated
        players_play: player's choice of play. Either choose hit or stand. If chosen hit, player
                     receives a new card. update hands and update points. If player chooses 'stand'. 
                     skip his turn. points and hands remain the same
        lose_bet: player lost all bet. bet_amount clears to 0
        win_double: player wins the game. the betted amount doubles and gets deposited
                    into player's money_account
        tie_return: game is a tie. Player gets back his or her original bet.
        deposit: deposit 10 dollars into account if the player's account 
                 balance is 0. Option available at the end of the game.

    Imported Methods:
        deal_cards: create an initial list of cards that are in a player's hand when the cards are dealt.
        count_points: calculate the total points given the current hand

    """
    # Object attributes
    def __init__(self, money_account=50, bet_amount=0, bust=False):
        '''Return a new human player object'''
        self.money_account = money_account
        self.bet_amount = bet_amount
        PlayersHand.__init__(self)

    # Methods
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

    def players_play(self,deck):
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

    def lose_bet(self):
        '''player lost all bet. bet_amount clears to 0'''
        print(f'You have lost your bet: {self.bet_amount}')
        self.bet_amount = 0

    def win_double(self):
        '''player wins double the amount he or she bet for'''
        self.money_account += self.bet_amount * 2

    def tie_return(self):
        '''game is a tie. Player gets back his or her original bet.'''
        self.money_account += self.bet_amount
        self.bet_amount = 0
    
    def deposit(self):
        """deposit: deposit 10 dollars into account if the player's account 
           balance is 0. Option available at the end of the game.
        """
        self.money_account += 10

