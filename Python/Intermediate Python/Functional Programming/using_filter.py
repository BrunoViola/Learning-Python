def filter_odd(number):
   return number%2 > 0

number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

result = filter(filter_odd, number_list)

print(list(result))