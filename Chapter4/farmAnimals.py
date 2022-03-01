myAnimals = ["cow", "pig", "chicken", "goat", "lamb", "sheep"]
yourAnimals = myAnimals[:]
yourAnimals.append("horse")
yourAnimals.append("alpaca")
yourAnimals.append("duck")
yourAnimals.append("rabbit")
yourAnimals.sort()
myAnimals.sort()

print("----------------------Original List---------------------")
for item in myAnimals:
    print(item)

print("---------------------New List--------------------")

for item in yourAnimals:
    print(item)

print("The first three animals are: ", yourAnimals[:3])
print("The middle three are ", yourAnimals[3:6])
print("The last three animals are: ", yourAnimals[7:10])