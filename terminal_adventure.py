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

game_card_win = """
      ___________________________________
     |     🎮 Terminal Adventure 🕹️       |
     |             You won               |
     |                                   |
     |                                   |
      ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾    
"""

def print_div():
   print('----------------------------')

def main():
   print(game_card_start)

   start = int(input('Would you like to start the game?\n1 - Yes\t0 - No\nYour option: '))

   print_div()
   if start == 1:
      print('Welcome to the Terminal Adventure, sir xxxxx')
      player_name = input('How should I call you? ')
      print(f'\nOkay, I\'ll call you as {player_name}.\n I\'m redirecting you to another game dimension...')
   elif start == 0:
      print('You pressed 0, bye...')
      exit(0)
   else:
      print('You didn\'t informed a valid choice, bye...')

   print_div()
   print('Our world has been invaded by some dangerous createrous, then we need your help')
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
   print_div()

   way_choose = int(input(f'{player_name}, we are suffering a direct attack on our village, you need to go there. But, you need to decide the way, are going by the river or by the forest?\n Type 1 to choose the river and type 2 if you prefer the forest: '))
   print_div()

   if way_choose not in [1, 2]:
      print('You informed a different number, you should need to read the instruction carefully!\n Now I will choose for you')
      way_choose = random.randint(1,2)
   print_div

   if way_choose == 1: #River
      print('You\'re entering the river and suddenly a aquatic creature appears, let\'s fight')
      creature_life = random.randint(50, 70)
      creature_damage = random.randint(5, 30)
      print(f'The aquatic creature has {creature_life} and cause {creature_damage} points of damage')
      while creature_life>0 and life_point > 0:
         print('You made an attack')
         creature_life -= damage
         if creature_life <= 0:
            print('You killed the creature')
            break
         print(f'The creature has now {creature_life} life points')
         print('The creature made an attack')
         life_point -= creature_damage
         print(f'You have now {life_point} life points')
         if life_point <= 0:
            print(game_card_died)
            exit(0)
         else:
            superpower_choose = int(input('Do you want to use a superpower? (1) - Yes    (any key) - No'))
            if superpower_choose == 1:
               creature_life = creature_life - random.randint(30, 40)
         print_div()
   
   if way_choose == 2: #Forest
      print('You\'re entering the forest and suddenly a creature appears, let\'s fight')
      creature_life = random.randint(60, 75)
      creature_damage = random.randint(10, 25)
      print(f'The creature has {creature_life} and cause {creature_damage} points of damage')
      while creature_life>0 and life_point > 0:
         print('You made an attack')
         creature_life -= damage
         if creature_life <= 0:
            print('You killed the creature')
            break
         print(f'The creature has now {creature_life} life points')
         print('The creature made an attack')
         life_point -= creature_damage
         print(f'You have now {life_point} life points')
         if life_point <= 0:
            print(game_card_died)
            exit(0)
         else:
            superpower_choose = int(input('Do you want to use a superpower? (1) - Yes    (any key) - No'))
            if superpower_choose == 1:
               creature_life = creature_life - random.randint(30, 40)
         print_div()
   
   print(game_card_win)

if __name__ == "__main__":
    main()