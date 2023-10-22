# from car import Car, ElectricCar

# my_beetle = Car('volkswagen', 'beetle', 2019)
# print(my_beetle.get_descriptive_name())

# my_tesla = ElectricCar('tesla', 'roadster', '2019')
# print(my_tesla.get_descriptive_name())

################################################################
# Importing an entire module and using dot notation to access specific classes.

# import car

# my_beetle = car.Car('volkswagen', 'beetle', 2019)
# print(my_beetle.get_descriptive_name())

# my_tesla = car.ElectricCar('tesla', 'roadster', '2019')
# print(my_tesla.get_descriptive_name())

#################################################################
# Changed electric_car.py to import Car from differnt module

from car import Car
from electric_car import ElectricCar

my_beetle = Car('volkswagen', 'beetle', 2019)
print(my_beetle.get_descriptive_name())

my_tesla = ElectricCar('tesla', 'roadster', '2019')
print(my_tesla.get_descriptive_name())
