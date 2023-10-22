import unittest
from city_functions import combine_city


class NamesTestCase(unittest.TestCase):

    def test_city_country(self):
        formatted_loc = combine_city('alberta', 'canada')
        self.assertEqual(formatted_loc, 'Alberta, Canada')

    def test_population(self):
        formatted_pop = combine_city('alberta', 'canada', '500000000')
        self.assertEqual(
            formatted_pop, 'Alberta, Canada - Population 500000000')


if __name__ == '__main__':
    unittest.main()


##################################################################################
# Answer:
# city_functions.py:

# """A collection of functions for working with cities."""

# def city_country(city, country, population=0):
#     """Return a string representing a city-country pair."""

#     output_string = f"{city.title()}, {country.title()}"
#     if population:
#         output_string += f" - population {population}"
#     return output_string

# #test_cities.py

# import unittest

# from city_functions import city_country

# class CitiesTestCase(unittest.TestCase):
#     """Tests for 'city_functions.py'."""

#     def test_city_country(self):
#         """Does a simple city and country pair work?"""
#         santiago_chile = city_country('santiago', 'chile')
#         self.assertEqual(santiago_chile, 'Santiago, Chile')

#     def test_city_country_population(self):
#         """Can I include a population argument?"""
#         santiago_chile = city_country('santiago', 'chile', population=5_000_000)
#         self.assertEqual(santiago_chile, 'Santiago, Chile - population 5000000')

# if __name__ == '__main__':
#     unittest.main()
