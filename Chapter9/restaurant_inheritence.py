class Restaurant:
    def __init__(self, restaurant_name, cuisine_type, number_served=0):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served=number_served

    def describe_restaurant(self):
        print(f"The name of the restaurant is {self.restaurant_name}.")
        print(f"The type of cuisine servered there is {self.cuisine_type}.")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is open.")

    def set_number_served(self, served):
        self.number_served=int(served)
    
    def increment_number_served(self,served):
        self.number_served += int(served)

class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type, number_served=0, flavors=[]):
        super().__init__(restaurant_name, cuisine_type, number_served=0)
        self.flavors = flavors

    def displayFlavors(self):
        print("IceCream flavors are:")
        for f in self.flavors:
            print(f.title())

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