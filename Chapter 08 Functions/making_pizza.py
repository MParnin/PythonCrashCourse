# import pizza

# pizza.make_pizza(16, 'pepperoni')

# pizza.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

##############################################################################
# Importing a specific function of the called module

# from pizza import make_pizza

# make_pizza(16, 'pepperoni')

# make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

###############################################################################
# Giving the imported function an alias

from pizza import make_pizza as mp

mp(16, 'pepperoni')

mp(12, 'mushrooms', 'green peppers', 'extra cheese')
