print("---------------------------------Exercise 3-4---------------------------")
guestList=["Jill","Mom","Jeanie"]
print(guestList[0], ", can you make it to dinner this Sunday?")
print(guestList[1], ", can you make it to dinner this Sunday?")
print(guestList[2], ", can you make it to dinner this Sunday?")

print("---------------------------------Exercise 3-5---------------------------")
print(guestList[1], ", can't make it to dinner.")
guestList[1] = "Marty"
print(guestList[0], ", can you make it to dinner this Sunday?")
print(guestList[1], ", can you make it to dinner this Sunday?")
print(guestList[2], ", can you make it to dinner this Sunday?")

print("---------------------------------Exercise 3-6---------------------------")
print("Oh Yeah! Found a bigger table!")
guestList.insert(0, "Dad")
guestList.insert(3, "Jackie")
guestList.append("Mom")
print("The number of guests I am inviting now is:", len(guestList))


print(guestList[0], ", can you make it to dinner this Sunday?")
print(guestList[1], ", can you make it to dinner this Sunday?")
print(guestList[2], ", can you make it to dinner this Sunday?")
print(guestList[3], ", can you make it to dinner this Sunday?")
print(guestList[4], ", can you make it to dinner this Sunday?")
print(guestList[5], ", can you make it to dinner this Sunday?")

print("---------------------------------Exercise 3-7---------------------------")
print("Bad news, table too small stil, only room for two guests :(")


guestList.pop(1)
print("Uninvited, sorry", guestList[1])
guestList.pop(1)
print("Uninvited, sorry", guestList[1])
guestList.pop(1)
print("Uninvited, sorry", guestList[1])
guestList.pop(1)
print("Uninvited, sorry", guestList[1])

print(guestList[0], ", do not worry you are still invited.")
print(guestList[1], ", do not worry you are still invited.")

del guestList[0]
del guestList[0]

print("New Guest List:", guestList)
