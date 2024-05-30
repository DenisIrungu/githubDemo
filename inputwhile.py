#Determining a number is even or odd
number = input("Enter a number: ")
number = int(number)
if number %2==0:
    print(f"{number} is an even number")
else:
    print( f"{number} is an odd number")
#Rental Car: Write a program that asks the user what kind of rental car they would like. Print a message about that car, such as “Let me see if I can find you a Subaru.”

car = input("what kind of rental car would you like? ")
message = f"Let me see if i can find you a {car}"
print(message)

# Restaurant Seating:
# Write a program that asks the user how many people are in their dinner group.
# If the answer is more than eight, print a message say- ing they’ll have to wait for a table. 
# Otherwise, report that their table is ready.

user = input("Please enter your name: ")
number = input ("How many people are in your dinner group? ")

number = int(number)
if number > 8:
    print ("Kindly wait for a table")
else:
    print ("The table is available. Welcome and enjoy")

# 3. Multiples of Ten:
# Ask the user for a number, and then report whether the number is a multiple of 10 or not.
number = input("Enter a number: ")
number = int(number)
if number %10==0:
    print(f"{number} is a multiple of 10")
else:
    print( f"{number} is not a multiple of 10")

