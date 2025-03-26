import csv

data = [
   ['Name', 'Age', 'Grade'],
   ['Ana', 19, 'A'],
   ['Bianca', 25, 'A+'],
   ['Bob', 18, 'B']
]

def main():
   with open('output.csv', 'w', newline='') as file:
      csv_writer = csv.writer(file)

      csv_writer.writerows(data)

if __name__ == "__main__":
   main()