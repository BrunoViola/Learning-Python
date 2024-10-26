from functools import reduce

# List of songs with their durations (in minutes)
playlist = [('What Was I Made For?', 3.42), ('Just Like That', 5.05), ('Song 3', 6.8), ('Leave The Door Open', 4.02), ('I Can\'t Breath', 4.47), ('Bad Guy', 3.14)]

# Filtering songs that are longer than 5 minutes
def longer_than_five_minutes(song):
   return song[1]>5.00

# Converting all the durations from minutes to seconds
def minutes_to_seconds(song):
   duration = song[1]
   minutes = int(duration)
   seconds = (minutes*60) + ((song[1]-minutes)*100)
   return round(seconds)

# Summing all the durations
def add_durations(total, song):
   duration = song[1]
   return total + duration

def main():
   result_5_minutes = filter(longer_than_five_minutes, playlist)
   print(list(result_5_minutes))

   result_minutes_to_seconds = map(minutes_to_seconds, playlist)
   print(list(result_minutes_to_seconds))

   result_total_duration = reduce(add_durations, playlist, 0)
   print(result_total_duration)

if __name__ == "__main__":
   main()