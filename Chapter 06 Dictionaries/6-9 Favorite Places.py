favorite_places = {

    'mike': {
        'first favorite place': 'home',
        'second favorite place': 'range',
        'third favorite place': 'hawaii',
    },
    'michaela': {
        'first favorite place': 'home',
        'second favorite place': 'ohio',
        'third favorite place': 'couch',
    },
    'andy': {
        'first favorite place': 'ice rink',
        'second favorite place': 'shopping',
        'third favorite place': 'texas',
    }
}

for name, info in favorite_places.items():
    print(f"\n Name: {name.title()}")
    location0 = info['first favorite place']
    location1 = info['second favorite place']
    location2 = info['third favorite place']
    print(
        f"\tFavorite Places: {location0.title()} \n\t{location1.title()} \n\t{location2.title()}")

##############################################################################################
# Answer:

# favorite_places = {
#     'eric': ['bear mountain', 'death valley', 'tierra del fuego'],
#     'erin': ['hawaii', 'iceland'],
#     'willie': ['mt. verstovia', 'the playground', 'new hampshire']
#     }

# for name, places in favorite_places.items():
#     print(f"\n{name.title()} likes the following places:")
#     for place in places:
#         print(f"- {place.title()}")
