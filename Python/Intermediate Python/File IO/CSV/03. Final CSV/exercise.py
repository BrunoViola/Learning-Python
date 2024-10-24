import csv

data = [
  ['Item', 'Quantity'],
  ['Blender', 2],
  ['Posters', 30],
  ['Shoes', 2]
]

def main():
  try:
    with open("packing_list.csv", "r") as file:
      csv_reader = csv.reader(file)
      print("Items: \n")
      for item in csv_reader:
        print(item)
  except FileNotFoundError:
    print("Packing list file not found. Creating a new one.")
    with open("packing_list.csv", "w", newline='') as file:
      csv_writer = csv.writer(file)
      for item in data:
        csv_writer.writerow(item)
if __name__ == "__main__":
   main()