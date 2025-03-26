def multiplied_by_3(number):
   return number * 3

number_list = [1, 2, 3, 4, 5]

result = map(multiplied_by_3, number_list)

print(list(result))

