import math

def calculate_circle_area(radius):
   return radius**2 * math.pi

def main():
   radius = int(input('Inform the radius: '))
   area = calculate_circle_area(radius)
   print(f'Area = {area:.5f}')

if __name__ == "__main__":
   main()