def main():
   avg_touchdowns = 0
   avg_yards_gained = 0

   player_stats = [{'name': 'Tyreek Hill', 'position': 'Wide Receiver', 'jersey_number': 10, 'yards_gained': 150, 'touchdowns': 2},
                  {'name': 'Cousins', 'position': 'Quarterback', 'jersey_number': 11, 'yards_gained': 200, 'touchdowns': 3},
                  {'name':'Mayfield', 'position': 'Tight End', 'jersey_number': 20, 'yards_gained': 250, 'touchdowns': 1}
                  ]

   # Printing only the name, followed by only the positions
   names = [player["name"] for player in player_stats]
   print(f'Names: {names}')
   positions = [player["position"] for player in player_stats]
   print(f'Positions: {positions}')

   # Updating statistics
   print(f'Printing old stats: {player_stats[1]}')
   player_stats[1]["yards_gained"] += 10
   player_stats[1]["touchdowns"] += 1
   print(f'Printing new stats: {player_stats[1]}')

   # Average statistics
   for player in player_stats:
      avg_touchdowns += player["touchdowns"]
      avg_yards_gained += player["yards_gained"]

   avg_touchdowns = avg_touchdowns/len(player_stats)
   avg_yards_gained = avg_yards_gained/len(player_stats)

   print(f'Average touchdowns: {avg_touchdowns:.2f}')
   print(f'Average yards_gained: {avg_yards_gained:.2f}')

if __name__ == "__main__":
   main()