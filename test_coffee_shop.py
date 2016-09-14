__author__ = 'kathiria'

import unittest
from coffee_shop import *


class TestCoffeeShop(unittest.TestCase):

    def setUp(self):
        self.fixture_file = 'C:\Users\kathiria\PycharmProjects\pydev\CoffeeShops.csv'
        self.fixture_not_file = 'C:\Users\kathiria\PycharmProjects\pydev\Coffee'
        self.fixture_distance1 = 168.8707197829156
        self.fixture_distance2 = 77.43203471432221
        self.fixture_list = [['Starbucks Seattle', '47.5809', '-122.3160'], ['Starbucks SF', '37.5209', '-122.3340'], ['Starbucks Moscow', '55.752047', '37.595242'], ['Starbucks Seattle2', '47.5869', '-122.3368'], ['Starbucks Rio De Janeiro', '-22.923489', '-43.234418'], ['Starbucks Sydney', '-33.871843', '151.206767'], ['Starbucks Rio De Janeiro 2', '-22.923489', '-43.234418']]
        self.fixture_x_coordinate = 364
        self.fixture_y_coordinate = -47.54
        self.fixture_dict = {'Starbucks Moscow': 28436.439360230106, 'Starbucks Seattle2': 28596.084679253647, 'Starbucks SF': 28595.80769501019, 'Starbucks Rio De Janeiro 2': 28515.160845709845, 'Starbucks Sydney': 28320.5072570883, 'Starbucks Rio De Janeiro': 28515.160845709845, 'Starbucks Seattle': 28596.063722584127}

    def tearDown(self):
        del self.fixture_file
        del self.fixture_list
        del self.fixture_distance1
        del self.fixture_not_file
        del self.fixture_x_coordinate
        del self.fixture_y_coordinate
        del self.fixture_dict

    def test_compute_distance_positive_negative_numbers_case(self):
        self.assertAlmostEquals(self.fixture_distance1, compute_distance(47.6, -122.4, 35, 46))

    def test_compute_distance_all_positive_numbers_case(self):
        self.assertAlmostEquals(self.fixture_distance2, compute_distance(47.6, 122.4, 35, 46))

    def test_compute_distance_all_negative_numbers_case(self):
        self.assertEqual(self.fixture_distance2, compute_distance(-47.6, -122.4, -35, -46))

    def test_compute_distance_val_missing_error_case(self):
        self.failIfEqual(self.fixture_distance2, lambda: compute_distance("", -122.4, 35, 46))

    def test_compute_distance_string_error_case(self):
        self.assertRaises(TypeError, lambda: compute_distance("yrh", -122.4, 35, 46))

    def test_get_distance_list_details_positive_case(self):
        self.assertListEqual(self.fixture_list, get_distance_list_details(self.fixture_file))

    def test_get_distance_list_details_no_file_case(self):
        self.assertRaises(IOError, lambda: get_distance_list_details(self.fixture_not_file))

    def test_gather_and_validate_input_positive_case(self):
        self.assertIsNone(gather_and_validate_input(self.fixture_y_coordinate, self.fixture_x_coordinate, self.fixture_file))

    def test_gather_and_validate_input_negative_case(self):
        self.failIfEqual(IOError, lambda: gather_and_validate_input(self.fixture_y_coordinate, self.fixture_x_coordinate, self.fixture_not_file))

    def test_get_coffee_shops_positive_case(self):
        self.assertDictEqual(self.fixture_dict, get_coffee_shops(-736.364, 28463, self.fixture_list))

    def test_get_coffee_shops_negative_case(self):
        self.assertRaises(TypeError, lambda: get_coffee_shops("", 28463, self.fixture_list))

if __name__ == '__main__':
    unittest.main()