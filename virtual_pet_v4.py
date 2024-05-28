"""
title- Virtual bunny
by- Kaitlyn Montado
date- 28/05/24
version- 4
"""

import menu.py


def eat(name, weight):
  #test function
  weight = weight + 1
  print(f"{name} now weighs {weight}")
  return weight


def exercise(name, weight):
  #test function
  weight = weight - 1
  print(f"{name} now weighs {weight}")
  return weight


# enter name
name = input('Enter a name: ')
print('what a nice name: ', name)

validate = True
while validate == True:
  try:
    # enter weight
    weight = int(input('Enter a weight\n'))
    x = weight  #Testing its a number
    x = int(x) + 1
    print(f"Hey {name} you have entered : {weight}")
    validate = False
  except:
    print("Invalid input")
    weight = input('Enter a weight\n')

# choice menu
#"choose: 1.feed 2.Exerice"

choice = input("choose: \n1 feed\n or \n2 exercise\n")
if choice == "1":
  print("you choose 1")
  weight = eat(name, weight)
elif choice == "2":
  print("you choose 2")
  weight = exercise(name, weight)
else:
  choice = input("choose: \n1 feed\n or \n2 exercise\n")

#feed menu
#"choose what to feed: A) apple B) brocolli C) Carrot"

#exerice menu:
#"choose how to play: R) RUN J) Jump P) Pat "
