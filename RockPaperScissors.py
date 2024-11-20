import random

def play():
    print("Welocme to our mini game of Rock, Paper, Scissors")
    print("Pick your choice")
    print("'r' for rock, 'p' for paper and 's' for scissors")

    while True:
        user = input("Enter your choice:")
        if user in ['r', 'p', 's']:
            break
        else:
            print("Your input is invalid. Only type (r,p,s) in lower casse letters.")
            user = input("Enter your choice:")

    computer = random.choice(['r', 'p', 's'])

    if user== computer:
        return 'It is a tie'
    
    if player_win(user, computer):
        return 'You Win!'
    
    return 'You Lose'
    
def player_win(player, com):
    if(player == 'r' and com =='s') or (player == 'p' and com == 'r') or (player == 's' and com == 'p'):
        return True

state = 1
while state == 1:  
    print(play())
    print("Do you want to continue?")

    while True:
        try:
            state = int(input("Type 1 to play a new round and Type 0 to quit the game:"))
            if state in [0,1]:
                break
            else:
                print("Invalid input. Please input either 0 or 1.")
        except ValueError:
            print("Invalid input. Please enter a number (1 or 0).")
    
    if state == 1:
        continue
    else:
        print("Quiting")
        break

