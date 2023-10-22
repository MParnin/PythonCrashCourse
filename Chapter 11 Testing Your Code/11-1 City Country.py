import unittest
from city_functions import combine_city


class NamesTestCase(unittest.TestCase):

    def test_city_country(self):
        formatted_loc = combine_city('alberta', 'canada')
        self.assertEqual(formatted_loc, 'Alberta, Canada')


if __name__ == '__main__':
    unittest.main()


#############################################################################
# Answer:
# city_function.py:

# """A collection of functions for working with cities."""

# def city_country(city, country):
#     """Return a string like 'Santiago, Chile'."""
#     return f"{city.title()}, {country.title()}"

# test_cities.py:

# import unittest

# from city_functions import city_country

# class CitiesTestCase(unittest.TestCase):
#     """Tests for 'city_functions.py'."""

#     def test_city_country(self):
#         """Does a simple city and country pair work?"""
#         santiago_chile = city_country('santiago', 'chile')
#         self.assertEqual(santiago_chile, 'Santiago, Chile')

# if __name__ == '__main__':
#     unittest.main()
