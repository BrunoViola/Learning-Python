import csv

def main():
   max_sales_in_million = 0
   bestseller = None

   with open("Bestseller - Sheet1.csv", "r", encoding="utf-8") as file:
      csv_reader = csv.reader(file)

      file.readline() #skip the top row (contains the descriptions)

      for row in csv_reader:
         current_sales_in_million = float(row[4])
         if current_sales_in_million > max_sales_in_million:
            max_sales_in_million = current_sales_in_million
            bestseller = row

   print(bestseller)
   
   with open("bestseller.csv", "w", newline='') as output:
      csv_writer = csv.writer(output)
      csv_writer.writerow(['Book', ' Author', ' Sales in Millions'])
      csv_writer.writerow([bestseller[0], bestseller[1], bestseller[4]])

   file.close()
if __name__ == "__main__":
   main()