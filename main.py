'''This file execute the game play. This portion of the code uses functioning programing.
'''
from modules.card_deck import CardDeck
from modules.human_player import HumanPlayer
from modules.computer_dealer import ComputerDealer
import time

# ------------------------ INITIALIZING GAME PLAY -----------------------------
print('Welcome to Human vs. Computer Black Jack Game')
time.sleep(2)

# Create an instance of human player and computer dealer
player1 = HumanPlayer()
dealerbot = ComputerDealer()

game_continue = True
while game_continue == True:
    ###########################################################################
    ## STEP 1: CREATE A NEW DECK OF CARDS ##
    ###########################################################################
    current_deck = CardDeck()
    current_deck.new_deck()
    #- check -#
    # print (current_deck.deck)
    # print (len(current_deck.deck))

    time.sleep(2)

    #########################
    ## STEP 2: PLACE A BET ##
    #########################
    # Human player place a bet
    print('Note: each human player is given a default account balance of $50 at the start of the game.')
    player1.place_bet()
    #- check -#
    # print(player1.bet_amount)

    # Dealer takes the bet
    dealerbot.receive_bet(player1.bet_amount)
    print('The computer dealer received the bet. Thank you.')
    time.sleep(3)
    #- check -#
    # print(dealerbot.received_bet)

    ########################
    ## STEP 3: DEAL CARDS ##
    ########################
    # Go 1st: Human player
    print("Now dealing cards...")
    time.sleep(2)

    player1.deal_cards(current_deck.deck)
    print(f"Player 1's current hand: {player1.current_hand}")
    time.sleep(1)

    # talley points
    player1.count_points()
    print(f"Player 1's current point total is: {player1.points}")
    time.sleep(3)

    # Go 2nd: Computer dealer
    dealerbot.deal_cards(current_deck.deck)
    dealerbot.count_points() #tally points in the background and store

    # show only one of dealer's card
    print(f"Dealer's current hand: {dealerbot.current_hand[:1]+['hidden']}")


    #-------------------------------- GAME STARTS -----------------------------------

    time.sleep(3)

    while True:
            #################################
            ## STEP 4: HUMAN PLAYER'S MOVE ##
            #################################
            player1.players_play(current_deck.deck)
            time.sleep(2)

            #talley points and determine whether human player had gone bust
            print (f"Player 1's current hand is :{player1.current_hand}")

            player1.count_points()
            if player1.bust == False:
                print(f"Player 1's current point total is: {player1.points}")
            else:
                print(f"Player 1 has gone bust!. Your current point total is: {player1.points}")
                player1.lose_bet()
                print('Computer dealer won. Player 1 surrender the bet')
                dealerbot.collect_bet()
                break

            time.sleep(3)

            ####################################
            ## STEP 5: COMPUTER DEALER'S TURN ##
            ####################################
            # Computer dealer reveals both of its cards
            print(f"Dealer reveals the full hand:{dealerbot.current_hand}")
            time.sleep(1)
            print(f"Dealer's current point total is: {dealerbot.points}")

            #Computer dealer makes the next move
            dealerbot.next_move(current_deck.deck)
            time.sleep(2)

            #talley points and determine winner
            print(f"Dealer's current hand is:{dealerbot.current_hand}")
            time.sleep(2)

            dealerbot.count_points()
            if dealerbot.bust == False:
                print(f"Dealer's current point total is: {dealerbot.points}")
                if dealerbot.points > player1.points:
                    print(f"Computer dealer won. Player 1 surrender the bet")
                    player1.lose_bet()
                    dealerbot.collect_bet()
                    break

                elif dealerbot.points < player1.points: 
                    print("Player 1 won. Player 1 gets double the bet amount.")
                    player1.win_double()
                    dealerbot.lose_bet()
                    break

                elif dealerbot.points == player1.points:
                    print('It is a tie.')
                    player1.tie_return()
                    dealerbot.tie_return()
                    break
            else:
                print('Dealer had gone bust. Player 1 won. Player 1 gets double the bet amount.')
                player1.win_double()
                dealerbot.lose_bet()
                break

    time.sleep(2)

    print(f"Player 1's account balance is: {player1.money_account}")
    time.sleep(2)

    play_again = ''
    while play_again != 'Y' and play_again != 'N':
        play_again = input('Would you like to play again? (Y/N)')
        if play_again == 'Y':
            # Check account balance = 0. deposit
            if player1.money_account == 0:
                print('Your current account balance is 0. $10 has been deposited into your account.')
            continue
        
        elif play_again == 'N':
            print('Thank you for playing. See you next time.')
            game_continue = False
            break


