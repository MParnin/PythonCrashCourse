def city_country(city, country):
    return f"{city.title()}, {country.title()}"


city = city_country('suffolk', 'usa')
print(city)
city = city_country('virginia beach', 'usa')
print(city)
city = city_country('norfolk', 'usa')
print(city)

######################################################################
# Answer:

# def city_country(city, country):
#     """Return a string like 'Santiago, Chile'."""
#     return f"{city.title()}, {country.title()}"

# city = city_country('santiago', 'chile')
# print(city)

# city = city_country('ushuaia', 'argentina')
# print(city)

# city = city_country('longyearbyen', 'svalbard')
# print(city)
