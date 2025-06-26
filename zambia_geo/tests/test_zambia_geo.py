import unittest
from zambia_geo import (
    get_all_provinces,
    get_province_cities,
    get_city_details,
    validate_province,
    validate_city,
    Province,
    City
)

class TestZambiaGeo(unittest.TestCase):
    def test_get_all_provinces(self):
        provinces = get_all_provinces()
        self.assertEqual(len(provinces), 10)
        self.assertIsInstance(provinces[0], Province)
        
    def test_get_province_cities(self):
        cities = get_province_cities("Lusaka")
        self.assertGreater(len(cities), 0)
        self.assertIsInstance(cities[0], City)
        
    def test_get_city_details(self):
        city = get_city_details("Lusaka")
        self.assertIsNotNone(city)
        self.assertEqual(city.name, "Lusaka")
        self.assertEqual(city.province, "Lusaka")
        self.assertEqual(city.is_capital, True)
        
    def test_validate_province(self):
        self.assertTrue(validate_province("Lusaka"))
        self.assertTrue(validate_province("lusaka"))  # case insensitive
        self.assertFalse(validate_province("Nonexistent"))
        
    def test_validate_city(self):
        self.assertTrue(validate_city("Lusaka"))
        self.assertTrue(validate_city("lusaka"))  # case insensitive
        self.assertFalse(validate_city("Nonexistent"))

if __name__ == "__main__":
    unittest.main()