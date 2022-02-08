from restaurant import Restaurant
print("--------------Exercise 9-6--------------")
flavors = []
flavor = ""
flavor = input("First Flavor of the Day: ")
flavors.append(flavor)
flavor = input("Second Flavor of the Day: ")
flavors.append(flavor)
flavor = input("Third Flavor of the Day: ")
flavors.append(flavor)

stand = IceCreamStand("Culvers", "fast food", 0, flavors)

print(f"The restaurant is called {stand.restaurant_name} and it serves yummy {stand.cuisine_type}")

stand.displayFlavors()