import random

print('Welcome, user!')
print('writer tree names')
names = input('Write three names, with space between:')
list = {names}
random.shuffle(list)
print(f'Your list {list}')
