# def combine_city(city, country):
#     """Combine a city and country in a statement"""
#     full_loc = f"{city}, {country}"
#     return full_loc.title()

##########################################################
# Providing the population too.

def combine_city(city, country, population=''):
    """Combine a city and country in a statement"""
    if population:
        full_loc = f"{city}, {country} - population {population}"
    else:
        full_loc = f"{city}, {country}"
    return full_loc.title()
