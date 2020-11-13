import random

class_list = ["Sebastian", "Kaja", "Emma", "Torjus", "Teodor", "Sander", "Benjamin", "Mattias", "Morris", "Maqzood", "Abdi"]

print()
number = 1
while len(class_list) != 0:
    i = random.randint(0, len(class_list) - 1)
    print(number, class_list.pop(i))
    number += 1