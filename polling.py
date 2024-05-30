# #POLLING EXAMPLE
# responses ={}
# polling_active = True

# while polling_active:
#     name = input("\nWhat is your name? ")
#     response = input("Which mountain would you like to climb? ")

#     responses [name] = response

#     repeat = input ("Would you like anyone els to take a poll?\n (Yes/ No) ")
#     if repeat == 'No':
#         polling_active = False
# print ("\n---Polling Results---")

# for name, response in responses.items():

#     print(f"{name} would like to climb {response}")

sandwich_orders = ["Chicken","Pastrami", "Eggs", "Pastrami","Beef", "Ham", "Sea Food","Pastrami"]
print ("We are out of 'Pastram' ")
while 'Pastrami' in sandwich_orders:
    sandwich_orders.remove('Pastrami')
finished_sandwiches = []
while sandwich_orders:
    new_sandwich = sandwich_orders.pop()
    print(f"\n, I made you {new_sandwich} ")
    finished_sandwiches.append(new_sandwich)
print ("Here are the finished sundwiches: ")
for  finsihed_sandwich in finished_sandwiches:
    print(finsihed_sandwich.title())
print (finished_sandwiches)



