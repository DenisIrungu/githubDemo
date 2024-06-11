
#Method 1 of importing
from restaurant import Restaurant, Ice_cream_Stand

my_restaurant = Restaurant("Hidaya", "Fast Foods")
my_restaurant.describe_restaurant()
print(my_restaurant.restaurant_name)

ice_cream_flavors = Ice_cream_Stand("Hunters Paradise", "Junks", ["Vanilla", "Strawbelly", "Sherbet"])
ice_cream_flavors.describe_restaurant()
ice_cream_flavors.available_flavors()

#method 2 of importing

import restaurant

my_restaurant = restaurant.Restaurant("Hidaya", "Fast Foods")
my_restaurant.describe_restaurant()
print(my_restaurant.restaurant_name)
