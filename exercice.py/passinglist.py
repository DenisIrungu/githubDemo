#Modifying a List in a Function
def print_models (unprinted, completeds):
    while unprinted:
        current_design = unprinted.pop()
        print(f"The printed deisign is: {current_design}")
        completeds.append(current_design)
def show_complited_designs(completeds):
    print("\nThe following deigns have been printed")
    for completed in completeds:
        print(f"The name of the compliteds is: {completed} ")
unprinted = ["Case", "Customized", "Black"]
completeds = []

print_models(unprinted, completeds)
show_complited_designs(completeds)

# 8-12. Sandwiches: Write a function that accepts a list of items a person wants on a sandwich. 
# The function should have one parameter that collects as many items as the function call provides, 
# and it should print a summary of the sand- wich that’s being ordered. 
# Call the function three times, using a different number of arguments each time.

def sandwitches_toppings (*toppings):
    for topping in toppings:
        print(f"\nThe sandwitch toppings are: {topping}")
sandwitches_toppings('Corronation')
sandwitches_toppings('Corronation','club')
sandwitches_toppings('Corronation','club', 'crub')
