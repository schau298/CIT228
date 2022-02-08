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


print("---------------- Try it Yourself 9-4 --------------")
restaurant = Restaurant("Thatsa Pizza","Pizza", 3)

restaurant.open_restaurant()
restaurant.describe_restaurant()
# printing number served
print("The number of customers initally served is", restaurant.number_served)
#changed value
restaurant.number_served= 15
print("The updated number of customers served is", restaurant.number_served)
#using set_number method to changed customers served
served = input("How many customers have been served?")
restaurant.set_number_served(served)
print("The updated number of customers served is", restaurant.number_served)
#adding customers served using increment method
served = input("how many additional customers have been served?")
restaurant.increment_number_served(served)
print("The total number of customers served is", restaurant.number_served)