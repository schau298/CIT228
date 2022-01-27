foods = ["pizza", "sausage", "tacos","spaghetti", "chicken", "bannana" ]
numbers=[2,4,6,8,10,12]
movies = ["Star Wars", "Pirates of Carribean", "Die Hard" ]
combo = [ "pizza", "sausage",2,4,"Star Wars, Pirates of Carribean"]
print("------------------------Hands On #1 -------------------------------")
print(foods)
print(numbers)
print(movies)
print(combo)

print(foods[-1])
print("2nd =", numbers[1])
print("4th =", numbers[3])
print("6th =", numbers[5])

print("1st movie=",movies[0])
print("2nd movie=",movies[1])
print("3rd movie=",movies[2])

print("First Food, fist number, first movie =", combo[0], combo[2], combo[4])

print("------------------------Hands On #2 -------------------------------")

movies.append("Guardians of the Galaxy")
print("Movie added to end", movies)

numbers.insert(4,18)
print("Number added to position 4",numbers)

foods.insert(4, "CheeseBurger")
print("Food added to position 4", foods)

numbers.pop()
print("Deleted a number from the end",numbers)

numbers.pop(2)
print("Deleted subscript 2", numbers)

print("------------------------Hands On #3 -------------------------------")

movies.sort()
print("Sorted List", movies)

foods.sort()
print("sorted List", foods)

print("Temp sorted list", sorted(numbers))
print("original", numbers)

movies.reverse()
print("sorted in reverse", movies)