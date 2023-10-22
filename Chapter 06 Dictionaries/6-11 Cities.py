cities = {
    'suffolk': {
        'country': 'usa',
        'population': 94324,
        'fact': 'largest city by land mass in va'
    },
    'san diego': {
        'country': 'usa',
        'population': 1386932,
        'fact': 'my birth place'
    },
    'virginia beach': {
        'country': 'usa',
        'population': 459470,
        'fact': 'where i grew up'
    }
}

for city, infos in cities.items():
    print(f"\n{city.title()} info:")
    for cityinfo, datas in infos.items():
        print(f"\t{cityinfo.title}: {datas}")

###############################################################################
# Answer:

# cities = {
#     'santiago': {
#         'country': 'chile',
#         'population': 6_310_000,
#         'nearby mountains': 'andes',
#         },
#     'talkeetna': {
#         'country': 'united states',
#         'population': 876,
#         'nearby mountains': 'alaska range',
#         },
#     'kathmandu': {
#         'country': 'nepal',
#         'population': 975_453,
#         'nearby mountains': 'himilaya',
#         }
#     }

# for city, city_info in cities.items():
#     country = city_info['country'].title()
#     population = city_info['population']
#     mountains = city_info['nearby mountains'].title()

#     print(f"\n{city.title()} is in {country}.")
#     print(f"  It has a population of about {population}.")
#     print(f"  The {mountains} mounats are nearby.")
