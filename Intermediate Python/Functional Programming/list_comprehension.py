numbers = [57, 10, 82, 36, 89, 46, 13, 23, 92, 48]

even_numbers = [number for number in numbers if number%2==0]
odd_numbers = [number for number in numbers if number%2!=0]

print(numbers)
print(even_numbers)
print(odd_numbers)