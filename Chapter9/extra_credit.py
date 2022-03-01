from random import randint

print("\n-------------Each dice gets rolled 10 times!-------------")
class Die():
    
    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        return randint(1, self.sides)


die6 = Die()
results = []
for roll_num in range(10):
    result = die6.roll_die()
    results.append(result)
print("\nRolls of 6-sided dice:")
print(results)


die10 = Die(sides=10)
results = []
for roll_num in range(10):
    result = die10.roll_die()
    results.append(result)
print("\n\nRolls of a 10-sided dice:")
print(results)



die20 = Die(sides=20)
results = []
for roll_num in range(10):
    result = die20.roll_die()
    results.append(result)
print("\n\nRolls of a 20-sided dice:")
print(results)