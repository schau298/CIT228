cities = ["New York, Chicago, Los Angeles, Tokyo, London"]
print("Original List:", cities)

cities.append("Orlando")
cities.insert(0,"Denver")
print("Added Cities:", cities)

cities.sort()
print ("Sorted List:", cities)

print("Temp Sorted List:", sorted(cities))

cities.reverse()
print ("reverse Sort:", cities)

cities.sort()
print(cities)
del cities[1]
cities.pop(0)

print("Delted Cities:", cities)

print("The final list contains this many cities:", len(cities))
