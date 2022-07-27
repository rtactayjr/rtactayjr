import random
import os


def rock_paper_scissors_game():
    player_user = input("What's your choice? 'r' for rock, 'p' for paper, 's' for scissors\n")
    computer_player= random.choice(['r', 'p', 's'])

    #conditional statements for playing the game
    if player_user == computer_player:
        print('Player selection: ' + player_user + ' Computer selection: '+ computer_player + ' Its a draw!')
    
    if win(player_user, computer_player):
        print('Player selection: ' + player_user + ' Computer selection: '+ computer_player + ' You won!')

    if lose(player_user, computer_player):
        print('Player selection: ' + player_user + ' Computer selection: '+ computer_player + ' Aww you lose....')

#def for winning the gam
def win(player, opponent):
    if player == 's' and opponent == 'p' or player == 'p' and opponent == 'r' \
    or player == 'r' and opponent == 's':
        return True
#def when you lose the game
def lose(player, opponent):
    if player == 'p' and opponent == 's' or player == 'r' and opponent == 'p' \
    or player == 's' and opponent == 'r':
        return True

#def for choosing if you still want to play or stop
def repeat():
    choice = 1
    while choice > 0:
        replay =  input("Would you like to play again? ('y'for yes, 'n' for no.)")
        if replay == "y":
            choice = choice + 1
            print("enjoy!")
            rock_paper_scissors_game()
        elif replay == "n":
            choice = 0
            print("Thank you for playing!")
            os._exit
        else:
            print('Please enter y or n')
            choice - 0
            repeat()

rock_paper_scissors_game()
repeat() 
