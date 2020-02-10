'''This file contains the functions used in the main.py file.
'''
import time
from modules.card_deck import CardDeck
from modules.human_player import HumanPlayer
from modules.computer_dealer import ComputerDealer

def placebet(player, dealer):
    ''' Ask human player to place a bet. Then, dealer takes the bet.

    each human player is given a default account balance of $50 dollars.
    
    Input: 
        player: the human player object
        dealer: the computer dealer object
    
    '''
    # Human player place a bet
    player.place_bet()

    # Dealer takes the bet
    dealer.receive_bet(player.bet_amount)
    print('The computer dealer received the bet. Thank you.')
    time.sleep(3)


def dealcards(player, dealer, deck):
    """ Deal cards to human and then deal card to computer
    dealer.
    
    Input: 
        player: the human player object
        dealer: the computer dealer object
        deck: a list of currently played cards.

    """
    player.deal_cards(deck)
    print(f"Human player's current hand: {player.current_hand}")
    time.sleep(1)

    # talley points
    print(f"Human player's current point total is: {player.points()}")
    time.sleep(3)

    # Go 2nd: Computer dealer
    dealer.deal_cards(deck)

    # show only one of dealer's card
    print(f"Dealer's current hand: {dealer.current_hand[:1]+['hidden']}")

def check_win(player, dealer, countdealer):
    ''' check the player and dealer's point to determine
    end game scenarios. If no end game scenarios have reached,
    continue game play

    Input:
        player: human player object
        dealer: computer dealer object
        countdealer: Boolean indicating whether to count dealers points
    '''
    end_round = False
          
    if countdealer == False:
        player.points()
                                      
        # scenario 1: player bust
        if player.bust():
            print("Human player has gone bust!")
            player.lose_bet()
            dealer.collect_bet()
            end_round = True
        else:
            print(f"Human player's current point total is: {player.current_points}") 

    else:
        print(f'Your current point total is: {player.points()}')
        print(f"Dealer's current point total is: {dealer.points()}")
        
        # scenario 2: dealer bust                
        if dealer.bust():
            print('Human player won.')
            player.win_double()
            dealer.lose_bet()
            
        else:
            
            # scenario 3: no one busts, dealer win
            if dealer.current_points > player.current_points:
                print(f"Computer dealer won.")
                player.lose_bet()
                dealer.collect_bet()
                
            # scenario 4: no one busts, dealer loses
            elif dealer.current_points < player.current_points:
                print(f"Human player won.")
                player.win_double()
                dealer.lose_bet()
    
            # scenario 5: no one busts, it is a tie
            elif dealer.current_points == player.current_points:
                print('It is a tie.')
                player.tie_return()
                dealer.tie_return()
        
        # end game
        end_round = True
    return end_round