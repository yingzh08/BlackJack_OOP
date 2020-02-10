'''This file execute the game play. This portion of the code uses functioning programing.
'''
import time
from modules.card_deck import CardDeck
from modules.human_player import HumanPlayer
from modules.computer_dealer import ComputerDealer
import functions

# ------------------------ INITIALIZING GAME PLAY -----------------------------
print('Welcome to Human vs. Computer Black Jack Game')
time.sleep(2)

# Create an instance of human player and computer dealer
player1 = HumanPlayer()
dealerbot = ComputerDealer()

game_continue = True
while game_continue:
    ###########################################################################
    ## STEP 1: CREATE A NEW DECK OF CARDS ##
    ###########################################################################
    current_deck = CardDeck()
 
    time.sleep(2)

    # reset player and dealer's hand to 0
    player1.current_hand = []
    player1.current_points = 0
    dealerbot.current_hand = []
    dealerbot.current_points = 0


    #########################
    ## STEP 2: PLACE A BET ##
    #########################

    #deposit $50 into human player's account
    player1.deposit(50)

    functions.placebet(player1, dealerbot)
    

    ########################
    ## STEP 3: DEAL CARDS ##
    ########################

    print("Now dealing cards...")
    time.sleep(2)
    
    functions.dealcards(player1, dealerbot, current_deck.deck)
    
    
    #-------------------------------- GAME STARTS -----------------------------------

    time.sleep(3)
    end_round = False
    while end_round == False:
        #################################
        ## STEP 4: HUMAN PLAYER'S MOVE ##
        #################################

        player1.next_move(current_deck.deck)
        time.sleep(2)

        #talley points and determine whether human player had gone bust
        print(f"Player 1's current hand is :{player1.current_hand}")

        finalcount = False
        end_round = functions.check_win(player1, dealerbot, finalcount)
        
        # mid-way check
        if end_round == True:
            break

        time.sleep(3)

        ####################################
        ## STEP 5: COMPUTER DEALER'S TURN ##
        ####################################
        # Computer dealer reveals both of its cards
        print(f"Dealer reveals the full hand:{dealerbot.current_hand}")
        time.sleep(1)
        print(f"Dealer's current point total is: {dealerbot.points()}")

        #Computer dealer makes the next move
        dealerbot.next_move(current_deck.deck)
        time.sleep(2)

        #talley points and determine winner
        time.sleep(2)

        finalcount = True
        end_round = functions.check_win(player1,dealerbot,finalcount)

    time.sleep(2)
    
    print(f"Player 1's account balance is: {player1.money_account} dollars.")
    time.sleep(2)

    #######################################
    ## STEP 6: ASK WHETHER TO PLAY AGAIN ##
    #######################################

    play_again = ''
    while play_again.lower() not in ('y', 'n'):
        play_again = input('Would you like to play again? (Y/N)')
        if play_again.lower() == 'y':
            # Check account balance = 0. deposit
            if player1.money_account == 0:
                print('Your current account balance is 0. $10 has been deposited into your account.')
                player1.money_account = 10

        elif play_again.lower() == 'n':
            print('Thank you for playing. See you next time.')
            game_continue = False