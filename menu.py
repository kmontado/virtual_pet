def eat_2(name, weight, food):
  #test function
  if food == "apple":
    weight = weight + 5
  elif food == "blueberry":
    weight = weight + 2
  elif food == "carrot":
    weight = weight + 6

  print(f"{name} now weighs {weight}")
  return weight


def eat_menu(name, weight):
  #test function
  #weight = weight + 1
  print(f"{name} now weighs {weight}")

  feed_menu = input("choose: \nA Apple\n or \nB Blueberry\n or \nC Carrot \n")
  if feed_menu.upper() == "A":
    print("you choose A")
    weight = eat_2(name, weight, "apple")
  elif feed_menu == "B":
    print("you choose B")
    weight = eat_2(name, weight, "blueberry")
  elif feed_menu == "C":
    print("you choose C")
    weight = eat_2(name, weight, "carrot")
  else:
    feed_menu = input(
        "choose: \nA Apple\n or \nB Blueberry\n or \nC Carrot \n")

  return weight


# test menu
name = "fluffy"
weight = 5
weight = eat_menu(name, weight)
