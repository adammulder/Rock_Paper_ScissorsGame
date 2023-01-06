import random


def playRockPaperScissors():
    
    while True:
        comp_choice = random.choice(['rock', 'paper', 'scissors'])
        player_choice = input('Choose: rock, paper, scissors (Type quit to stop playing) ')
        if player_choice.lower() == comp_choice:
            print(f'Computer chose: {comp_choice}')
            print('Game Tied')
        elif player_choice.lower() == 'rock' and comp_choice == 'paper':
            print(f'Computer chose: {comp_choice}')
            print('You lose')
        elif player_choice.lower() == 'rock' and comp_choice == 'scissors':
            print(f'Computer chose: {comp_choice}')
            print('You Win')
        elif player_choice.lower() == 'paper' and comp_choice == 'rock':
            print(f'Computer chose: {comp_choice}')
            print('You Win')
        elif player_choice.lower() == 'paper' and comp_choice == 'scissors':
            print(f'Computer chose: {comp_choice}')
            print('You lose')
        elif player_choice.lower() == 'scissors' and comp_choice == 'paper':
            print(f'Computer chose: {comp_choice}')
            print('You Win')
        elif player_choice.lower() == 'scissors' and comp_choice == 'rock':
            print(f'Computer chose: {comp_choice}')
            print('You lose')
        elif player_choice.lower() =='quit':
            print('Thank you for playing')
            break
        else:
            print('Please type rock, paper, or scissors')
            

playRockPaperScissors()

        


