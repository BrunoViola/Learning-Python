import random

game_card_start = """
      ___________________________________
     |     🎮 Terminal Adventure 🕹️       |
     |                                   |
     |                                   |
     |                                   |
      ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾    
"""

game_card_died = """
      ___________________________________
     |     🎮 Terminal Adventure 🕹️       |
     |             GAME OVER             |
     |        Better luck next time      |
     |                                   |
      ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾    
"""

print(game_card_start)

start = int(input('Would you like to start the game?\n1 - Yes\t0 - No\nYour option: '))

if start == 1:
   print('Welcome to the Terminal Adventure, sir xxxxx')
   player_name = input('How should I call you? ')
   print(f'\nOkay, I\'ll call you as {player_name}.\n I\'m redirecting you to another game dimension...')
elif start == 0:
   print('You pressed 0, bye...')
   exit(0)
else:
   print('You didn\'t informed a valid choice, bye...')

class_choice = int(input(f'\n{player_name}, you have to decide your class\n(1) - Warrior\n(2) - Archer\n(3) - Tank\nWhat are you going to be? '))

if class_choice not in [1, 2, 3]:
   print('You informed a different number, you should need to read the instruction carefully!\n Now I will choose a class for you')
   class_choice = random.randint(1,3)

if class_choice == 1:
   print('Great! You decided to be a Warrior')
   life_point = random.randint(80, 105)
   damage = random.randint(10, 20)
   print(f'Based on this, you have {life_point} life point and cause a damage of {damage}')
elif class_choice == 2:
   print('Great! You decided to be an Archer')
   life_point = random.randint(60, 80)
   damage = random.randint(15, 30)
   print(f'Based on this, you have {life_point} life point and cause a damage of {damage}')
else:
   print('Great! You decided to be a Tank')
   life_point = random.randint(110, 150)
   damage = random.randint(5, 15)
   print(f'Based on this, you have {life_point} life point and cause a damage of {damage}')