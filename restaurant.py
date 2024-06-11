
class Restaurant:
    def __init__(self, restaurant_name, cuisane_type):
        self.restaurant_name = restaurant_name
        self.cuisane_type = cuisane_type
        self.surved_food = 0

    def describe_restaurant (self):
        print (f"\nThe name of the restaurant is {self.restaurant_name} and the type of cuisane is {self.cuisane_type}")
    
    def open_restaurant (self):
        print(f"{self.restaurant_name} is open")
    
    def set_surved_food (self):
        print(f"The number of surved food is {self.surved_food}")

    def update_number_set_surved_food(self, set_food):
        self.surved_food = set_food

    def increament_number_surved (self, increased_number):
        self.surved_food += increased_number

class Ice_cream_Stand (Restaurant):
    def __init__(self, restaurant_name, cuisane_type, flavors):
        super().__init__(restaurant_name, cuisane_type)
        self.flavors = flavors

    def available_flavors (self):
        print ("\nAvailable flavors:")
        for flavor in self.flavors:
            print(f"        *{flavor}")

# ice_cream_flavors = Ice_cream_Stand("Hunters Paradise", "Junks", ["Vanilla", "Strawbelly", "Sherbet"])
# ice_cream_flavors.describe_restaurant()
# ice_cream_flavors.available_flavors()