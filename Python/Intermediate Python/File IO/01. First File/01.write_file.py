file = open('example.txt', 'w')
file.write('Hello World!')
lines = ['\nWriting a new line!', '\nThird line.']
file.writelines(lines)
file.close()