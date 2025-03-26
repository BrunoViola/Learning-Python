from math import pi, pow, floor
from random import choice as ch

def get_planet():
   planets = [
   'Mercury',
   'Venus',
   'Earth',
   'Mars',
   'Saturn'
   ]

   random_planet = ch(planets)

   return random_planet

def get_planet_radius(random_planet):
   if random_planet == 'Mercury':
      r = 2440
   elif random_planet == 'Venus':
      r = 6052
   elif random_planet == 'Earth':
      r = 6371
   elif random_planet == 'Mars':
      r = 3390
   elif random_planet == 'Saturn':
      r = 58232
   else:
      print('Oops! An error occurred.')
   
   return r

def main():
   random_planet = get_planet()
   r = get_planet_radius(random_planet)

   area = 4*pi*pow(r, 2)
   area = floor(area)

   print(f'Planet {random_planet} has {area} km^2')


if __name__ == '__main__':
   main()