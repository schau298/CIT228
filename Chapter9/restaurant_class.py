class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"The name of the restaurant is {self.restaurant_name}.")
        print(f"The type of cuisine servered there is {self.cuisine_type}.")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is open.")

print("---------------- Try it Yourself 9-1 --------------")
restaurant = Restaurant("Thatsa Pizza","Pizza")

print(f"The restaurant name is {restaurant.restaurant_name}")
print(f"The restaurant cuisine is {restaurant.cuisine_type}")

restaurant.open_restaurant()
restaurant.describe_restaurant()

print("---------------- Try it Yourself 9-2 --------------")
restaurant1 = Restaurant("Qdoba","Mexican")
restaurant2 = Restaurant("Fu Hua","Chinese")
restaurant3 = Restaurant("Culvers","American")

restaurant1.describe_restaurant()

restaurant2.describe_restaurant()

restaurant3.describe_restaurant()