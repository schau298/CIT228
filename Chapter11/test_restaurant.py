import unittest
from restaurant import Restaurant

class TestRestaurant(unittest.TestCase):
    """Unit Tests for the Store class """

def setUp(self):
    restaurant_name="Taco Bell"
    cuisine_type="Mexican"
    number_served=150
    self.store = Restaurant(restaurant_name, cuisine_type,number_served)

def test_set_number_served(self):
    number_served=100
    self.number_served(number_served)
    self.assertEqual(self.restaurant.number_served,100)

def test_increment_daily_sales_float(self):
    number_served=50
    self.increment_number_served(number_served)
    self.assertEqual(self.increment_number_served,15)  

if __name__ == '__main__':
    unittest.main()
    