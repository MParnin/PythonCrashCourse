from distutils.log import info


def car_info(make, model, **options):
    car_dict = {'manufacturer': make,
                'model': model}
    for option, value in options.items():
        car_dict[option] = value
    return car_dict


car_profile = car_info("vw", "gti", price='free')

print(car_profile)

###################################################################
# Answer:

# def make_car(manufacturer, model, **options):
#     """Make a dictionary representing a car."""
#     car_dict = {
#         'manufacturer': manufacturer.title(),
#         'model': model.title(),
#         }
#     for option, value in options.items():
#         car_dict[option] = value

#     return car_dict

# my_outback = make_car('subaru', 'outback', color='blue', tow_package=True)
# print(my_outback)

# my_old_accord = make_car('honda', 'accord', year=1991, color='white',
#         headlights='popup')
# print(my_old_accord)
