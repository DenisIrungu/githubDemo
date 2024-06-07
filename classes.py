# #Restaurant: Make a class called Restaurant.
# The __init__() method for Restaurant should store two attributes: a restaurant_name and a cuisine_type.
# Make a method called describe_restaurant() that prints these two pieces of information, and a method called open_restaurant() that prints a message indi- cating that the restaurant is open.
# Make an instance called restaurant from your class. Print the two attri- butes individually, and then call both methods.

class Restaurant:
    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant (self):
        print (f"\nThe restaurant name is {self.name} and the cuisane type is {self.cuisine_type}")
    def open_restaurant (self):
        print(f"{self.name} is open")
    def number_served (self):
        print(f"The number served is {self.number_served}")


restaurant = Restaurant("Jedalica", "First casual")

restaurant.describe_restaurant()
restaurant.open_restaurant()

print ("\n",restaurant.name)
print ("\n",restaurant.cuisine_type)

# Three Restaurants: Start with your class from Exercise 9-1. Create three different instances from the class. 
# Call describe_restaurant() for each instance.
restaurant2 = Restaurant ("Canivore", "First Food")
restaurant3 = Restaurant ("Thyme", "Casual dining")
restaurant4 = Restaurant ("Inca", "Contemporary")

restaurant2.describe_restaurant()
restaurant3.describe_restaurant()
restaurant4.describe_restaurant()


# Users: Make a class called User. 
# Create two attributes called first_name and last_name, and then create several other attributes that are typically stored in a user profile. 
#Make a method called describe_user() that prints a summary of the user’s information. 
#Make another method called greet_user() that prints a personalized greeting to the user.
# Create several instances representing different users, and call both methods for each user.

class User:
    def __init__(self, first_name, last_name, age, height):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.height = height
        
    def describe_user (self):
        print (f"\nThe user's name is {self.first_name} {self.last_name}")
        print (f"\nHe is {self.age} years old and {self.height}Fts tall")
    def greet_user (self):
        print (f"\nHello {self.first_name} {self.last_name}. How are you?")
user1 = User ("Denis", "irungu", 28, 5.7 )
user2 = User ("Toh", "Konki", 25, 5)
user3 = User ("Shem", "Mandela", 27, 5.4)



user1.describe_user()
user2.describe_user()
user3.describe_user()

user1.greet_user()
user2.greet_user()
user3.greet_user()

# Working with Classes and Instances
# Setting a Default Value for an Attribute
# Modifying Attribute Values

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
#Setting default value
        self.mileage = 0

    def describe_car(self):
        own_car = f"{self.make} {self.model} {self.year}"
        return own_car.title()
#Default value method
    def read_mileage(self):
        print(f"This car has {self.mileage} mileage")

#update method   
    def update_mileage(self, new_mileage):
#Added some spice to the code to avoid interfearnce on the mileage
        if new_mileage >= self.mileage:
            self.mileage = new_mileage
        else:
            print("You can't change the adometer")
#Modifying through an increament method        
    def increase_mileage (self, miles):
        self.mileage += miles

my_used_car = Car ("subaru", "forester", 2019)
print(my_used_car.describe_car())

my_used_car.update_mileage (20300)
my_used_car.read_mileage()

my_used_car.increase_mileage(200)
my_used_car.read_mileage()




my_car = Car("Audi", "A3", 2020) 

print (my_car.describe_car())
#Modifying attribute value directly
my_car.mileage =34
my_car.read_mileage ()
#Modifying through update method
my_car.update_mileage(40)
my_car.read_mileage()



        #TRY IT YOURSELF
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


restaurant = Restaurant("Hunter Paradise", "FastFood")
restaurant.describe_restaurant()
restaurant.open_restaurant()
# restaurant.surved_food = 90
restaurant.set_surved_food()











    

    

        