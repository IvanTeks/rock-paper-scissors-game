import random
wins = 0
losses = 0
while True:

    player = input("rock, paper or scissors? ")
    while player not in ["rock", "paper", "scissors"]:
        print("invalid choice! type rock, paper or scissors")
        player = input("rock, paper or scissors? ")

    computer = random.choice(["rock", "paper", "scissors"])
    print('you chose ' + player)
    print('the computer chose ' + computer)
    if player == 'rock' and computer == 'scissors':
        print('you win!')
        wins +=1
    elif player == 'rock' and computer == 'paper':
        print('you lose!')
        losses +=1
    elif player == 'paper' and computer == 'rock':
        print('you win!')
        wins +=1
    elif player == 'paper' and computer == 'scissors':
        print('you lose!')
        losses +=1
    elif player == 'scissors' and computer == 'paper':
        print('you win!')
        wins +=1
    elif player == 'scissors' and computer == 'rock':
        print('you lose!')
        losses +=1
    else:
        print('it is a tie!')
    
    again = input('play again? (y/n) ')
    print("wins: " + str(wins) + " losses: " + str(losses))
    if again == 'n':
        print('goodbye!')
        break


