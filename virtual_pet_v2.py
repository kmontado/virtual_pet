"""
title- Virtual bunny
by- Kaitlyn Montado
date- 9/05/24
version- 2
"""
# enter name
name = input('Enter a name: ')
print('what a nice name: ', name)

# enter weight
weight = input('Enter a weight\n')
print(f"Hey {name} you have entered " + weight)

try:
  x = input("Enter number: ")
  x = int(x) + 1 
  print(x)
except:
  print("Invalid input")

# choice menu

