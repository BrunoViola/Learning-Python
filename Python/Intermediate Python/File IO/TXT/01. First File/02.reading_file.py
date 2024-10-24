file = open('example.txt', 'r')

first_line = file.readline()
print(f'First line content: {first_line}')

content = file.read()
print(f'Second and third lines:\n{content}')

file.close()