import unittest
from city_functions import get_formatted_city

class CitiesTestCase(unittest.TestCase):
    def test_formatted_city(self):
        city_test = get_formatted_city('Santiago', 'Chile')
        self.assertEqual(city_test, 'Santiago, Chile')

    def test_formatted_population(self):
        city_test = get_formatted_city('Santiago','Chile','5,000,000')
        self.assertEqual(city_test, 'Santiago, Chile - Population: 5,000,000')

if __name__=='__main__':
    unittest.main()