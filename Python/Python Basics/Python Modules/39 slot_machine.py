import random

def play():
   symbols=['🍒','🍇', '🍉', '7️⃣']
   results = random.choices(symbols, k=3)
   print(f"{results[0]} | {results[1]} | {results[2]}")
   return results

def main():
   keep_playing = 'Y';
   while keep_playing.upper() == 'Y':
      results = play()
      if results == ['7️⃣','7️⃣','7️⃣']:
         print('Jackpot! 💰')
      else:
         print('Thanks for playing!')
      keep_playing = input('Do you want to play again? \n(Y) - Yes \t(any key) - No: ')


if __name__ == "__main__":
   main()
