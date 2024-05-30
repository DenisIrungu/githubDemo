counter = 0
maximum = int(input("Enter your maximum number:"))
while counter < maximum:
    squere_maximum = counter**2
    print(f"The squere of {counter} is {squere_maximum}")
    counter+=1

print ("DONE!!")

#Let the user decide when to quite/end the program
user_input = "\nTell me something, and i will repeat it to you."
user_input+= "\nPress 'q' then enter to end the program  "
active = True
while  active:
    message = input(user_input)
    if message == 'q':
        active = False
    else:
         print(message)

# current_number = 0
# while current_number < 10: 
#     current_number += 1
#     if current_number % 2 == 1: 
#         continue
#     print(current_number)

# TRY IT YOURSELF
# Pizza Toppings: Write a loop that prompts the user to enter a series of pizza toppings until they enter a 'quit' value.
# As they enter each topping, print a message saying you’ll add that topping to their pizza.
prompt = "\n Enter the pizza topping,"
prompt+= "\n(Press 'q' to exit the program) "

message = ""
while message != 'q':
    message = input(prompt)
    if message != 'q':
        print (f"I will add {message} to your pizza")

prom = "Please enter your age to confirm your ticket"
prom+= "(\nPress 'q' to exit the program)"
while True:
    age = input(prom)
    if age == 'q':
      break
    if not age:
        print("Enter a valid age")
        continue
    age = int(age)
    if age < 3:
        ticket_price = "Free"
    elif age < 10:
        ticket_price = "$10"
    else:
        ticket_price = "$12"
    print(f"Your ticket price is {ticket_price}")


#POLLING EXAMPLE
responses ={}
polling_active = True

while polling_active:
    name = input("\nWhat is your name? ")
    response = input("Which mountain would you like to climb? ")

    responses [name] = response

    repeat = input ("Would you like anyone els to take a poll? (Yes/ No)")
    if repeat == 'No':
        polling_active = False
print ("\n---Polling Results---")
print (responses)


