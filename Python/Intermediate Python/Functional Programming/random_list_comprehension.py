import random
from functools import reduce

prefixes = ['Mystic', 'Golden', 'Dark', 'Shadow', 'Silver']
suffixes = ['storm', 'song', 'fire', 'blade', 'whisper']

def capitalize_suffix(name):
  name = name.capitalize()
  return name

def create_fantasy_name(list_1, list_2):
  return random.choice(list_1) + ' ' + random.choice(list_2)

def fire_in_name(name): #verify if the name has the suffix 'fire'
  if 'Fire' in name:
    return True
  else:
    return False
  
def concatenate_names(name1, name2):
  return name1 + name2

def display_name_info(random_names, result_fire, concatenate_fire):
  print("Random names: ", end=' ')
  [print(name, end=' ') for name in random_names] # Prints the generated fantasy names with a for loop
  print("\nNames with \'fire\': ", end=' ')
  [print(name, end=' ') for name in result_fire] # Prints the filtered names that include 'fire'
  print("\nReduced names with \'fire\': ", end=' ')
  [print(name, end='') for name in concatenate_fire] # Prints the reduced names that have 'fire.

def main():
  result = list(map(capitalize_suffix, suffixes))

  random_names = [create_fantasy_name(prefixes, result) for name in range(10)] #create ten different fantasy names
  print(f"Fantasy names: {random_names}")

  result_fire = list(filter(fire_in_name, random_names)) #verify what is the names with suffix 'fire'
  print(f"Names with 'fire': {result_fire}")

  if result_fire != None:
    concatenate_fire = reduce(concatenate_names, result_fire, '') #concatenate the names with the suffix 'fire'
    print(f'Fire concatenation: {concatenate_fire}')
  else:
    print("There isn't a name with the suffix 'fire', then I cannot use the reduce function")

  print("\n\nUsing the display_name_info()")
  display_name_info(random_names, result_fire, concatenate_fire)

if __name__ == "__main__":
  main()