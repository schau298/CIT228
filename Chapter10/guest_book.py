"""guest=input("What is your name (q to quit)?")
with open("Chapter10/guest.txt","a") as guestFile:
    while guest!='q':
        guest+="\n"
        print("Welcome", guest)
        guestFile.write(guest)
        guest=input("What is your name (q to quit)?") """

import random
import os
filename="Chapter10/guest.txt"

if os.path.exists(filename):
    os.remove(filename)

rooms=[]
with open(filename,"w") as guestsFile:
    guest=input("Please enter your name(q to quit)?")
    while guest != 'q':
        number=random.randint(1,50)
        while number in rooms:
            number=random.randint(1,50)
        print(f"{guest} you will be in room # {number}")
        rooms.append(number)
        guest+=", room # " + str (number) + "\n"
        guestsFile.write(guest)
        guest=input("Please enter your name (q to quit)?")

with open(filename) as guestsFile:
    print("----------Room # Assigned------------")
    for line in guestsFile:
        print(line)