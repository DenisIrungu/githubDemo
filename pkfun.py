#consider a function that displays information about petsThe function tells us what kind of animal each pet is and the pet’s name
def my_pet(type, name):
    print(f"I have a {type}")
    print(f"My {type},is called {name}")
my_pet("dog", "Bosco")

#keyword arguments
def my_pet(type, name):
    print(f"I have a {type}")
    print(f"My {type},is called {name}")
my_pet(name= "Bosko", type= "dog")

#Default
def my_pet(name, type= "Cat",):
    print(f"I have a {type}")
    print(f"My {type},is called {name}")
my_pet(name="Jed")

def make_shirt (size, message):
    print(f"The size of the shirt is {size}, print '{message.title()}' at the fron and back of the shirt!")
make_shirt(message="Go hard or go home", size="Medium")

def make_tshirts(message= "I love python", size = "Large"):
    print(f"The size of the shirts is : {size}, Print {message.title()} on the shirts")
make_tshirts(message= "i love python")
make_tshirts(size= "Large")
 