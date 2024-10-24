def write_liked_songs_to_file(liked_songs, file):
   for song, artist in liked_songs.items():
      file.write(f"{song} by {artist}\n")

def main():
   file = open('liked_songs.txt', 'w')

   liked_songs = {
      'Bad Habits' : 'Ed Sheeran',
      'I\'m Just Ken': 'Ryan Goslin',
      'Mastermind' : 'Taylor Swift'
   }
   
   write_liked_songs_to_file(liked_songs, file)
   file.close()

if __name__ == "__main__":
   main()