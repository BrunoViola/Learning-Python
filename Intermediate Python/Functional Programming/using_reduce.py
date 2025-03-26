from functools import reduce

def sum(x, y):
   return x+y

number_list = list(range(1, 101))

result = reduce(sum, number_list)

print(result)