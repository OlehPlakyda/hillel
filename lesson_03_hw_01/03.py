b = input('Enter a string variable in snake_case format: ')

b = b.title()
b = b.split('_')
b = ''.join(b)

print(b)
