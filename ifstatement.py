age_1 = 34
age_2 = 20
if age_1 >= 21 or age_2 >=21:
    print("True")
else:
    print("False")

foods = ["Pilau", "Sembe", "Matoke", "Rice", "Arosto"]
best_meal = "githeri"
if best_meal in foods:
    print(f"{best_meal.upper()} is avilable in the Menu")
else:
    print(f"{best_meal.upper()} is not avaibale in the Menu")

car="subaru"
car = "honda"
#print("Is car== 'subaru'? I predict True")
print(car== "bmw")
print(car=="subaru")
print(car=="Subaru")
print(car=="honda")

#DO IT YOURSELF
# Alien Colors #1: Imagine an alien was just shot down in a game. Create a
# variable called alien_color and assign it a value of 'green', 'yellow', or 'red'.
# •	 Write an if statement to test whether the alien’s color is green. If it is, print
# a message that the player just earned 5 points.
# •	 Write one version of this program that passes the if test and another that
# fails. (The version that fails will have no output.)
alien_color = "Green"
if alien_color=="Green":
    print("You just earned 5 points")

alien_color = "Red"
if alien_color=="Green":
    print("You just earned 5 points")

# Alien Colors #2: Choose a color for an alien as you did in Exercise 5-3, and
# write an if-else chain.
# •	 If the alien’s color is green, print a statement that the player just earned
# 5 points for shooting the alien.
# •	 If the alien’s color isn’t green, print a statement that the player just earned
# 10 points.
# •	 Write one version of this program that runs the if block and another that
# runs the else block.
alien_color = "Green"
if alien_color=="Green":
    print("You just earned 5 points")
else:
    print("You just earned 10 points\n")

# Alien Colors #3: Turn your if-else chain from Exercise 5-4 into an if-elifelse chain.
# •	 If the alien is green, print a message that the player earned 5 points.
# •	 If the alien is yellow, print a message that the player earned 10 points.
# •	 If the alien is red, print a message that the player earned 15 points.
# •	 Write three versions of this program, making sure each message is printed
# for the appropriate color alien.
alien_color = "Yellow"
if alien_color=="Green":
    print("You just earned 5 points")
elif alien_color=="Yellow":
    print("You just earned 10 points")
elif alien_color=="Red":
    print("You just earned 15 points\n")

alien_color = "Green"
if alien_color=="Green":
    print("You just earned 5 points")
elif alien_color=="Yellow":
    print("You just earned 10 points")
elif alien_color=="Red":
    print("You just earned 15 points\n")

alien_color = "Red"
if alien_color=="Green":
    print("You just earned 5 points")
elif alien_color=="Yellow":
    print("You just earned 10 points")
elif alien_color=="Red":
    print("You just earned 15 points\n")
    

age = 100
if age <2:
    print ("The person is a baby")
elif age<4:
    print("The person is a toddler")
elif age < 13:
    print("The person is a kid")
elif age <20:
    print("The person is a teenager")
elif age <65:
    print("The person is an aldult")
elif age >=65:
    print("The person is an elder\n")
# 5-7. Favorite Fruit: Make a list of your favorite fruits, and then write a series of
# independent if statements that check for certain fruits in your list.
# •	 Make a list of your three favorite fruits and call it favorite_fruits.
# •	 Write five if statements. Each should check whether a certain kind of fruit
# is in your list. If the fruit is in your list, the if block should print a statement,
# such as You really like bananas!
favourite_fruits =["Apple", "Pineapple", "Mango" ]
if "Apple" in favourite_fruits:
    print("You really like Apples")
if "Pineapple" in favourite_fruits:
    print("You really like Pineapples")
if "Mango" in favourite_fruits:
    print("You really like Mango")
if "Watermelon" in favourite_fruits:
    print("You really like Watermelon")
if "Banana" in favourite_fruits:
    print("You really like Banana")


# 5-8. Hello Admin: Make a list of five or more usernames, including the name
# 'admin'. Imagine you are writing code that will print a greeting to each user
# after they log in to a website. Loop through the list, and print a greeting to
# each user:
# •	 If the username is 'admin', print a special greeting, such as Hello admin,
# would you like to see a status report?
# •	 Otherwise, print a generic greeting, such as Hello Jaden, thank you for
# logging in again
# usernames = ["Admin", "Denis","Toh","Liam","Layne"]
# for username in usernames:
#     if username=="Admin":
#         print(f"Hello {username}, would you like to see a status report")
#     else:
#         print( f"Hello {username}, thank you for logging in again")



# usernames = []
# if not usernames:
#     print("We need to find some users!")
# else:
#     for username in usernames:
#         if username=="Admin":
#             print(f"Hello {username}, would you like to see a status report")
#         else:
#             print( f"Hello {username}, thank you for logging in again")

current_users = ["Toh", "Liam","Layne","Deno", "Wickie"]
new_users = ["Toh", "Liam", "Kagusi", "Mark", "Irungu"]
for new_user in new_users:
    if new_user in current_users:
        print(f"Username {new_user} already taken. Please enter new username")
    else:
        print (f"Username '{new_user}' is available")
# Ordinal Numbers: Ordinal numbers indicate their position in a list, such
# as 1st or 2nd. Most ordinal numbers end in th, except 1, 2, and 3.
# •	 Store the numbers 1 through 9 in a list.
# •	 Loop through the list.
# •	 Use an if-elif-else chain inside the loop to print the proper ordinal ending for each number. Your output should read "1st 2nd 3rd 4th 5th 6th
# 7th 8th 9th", and each result should be on a separate line.
numbers = list(range(1,10))
for number in numbers:
    if number==1:
        print(f"{number}st")
    elif number ==2:
        print(f"{number}nd")
    elif number==3:
        print(f"{number}rd")
    else:
        print(f"{number}th")
    
    


















# #if it's hot, it's a hot day. drink alot of water. otherwise if it's cold, it's a cold day, wear warm clothes. otherwise it's a lovely day
# is_hot_day = False
# is_cold_day = False
# if is_hot_day:
#     print("It's a hot day")
#     print("Drink alot of water")
# elif is_cold_day:
#     print("It's a cold day")
#     print("Wear warm clothes")
# else:
#     print("It's a lovely day")

# #The price of a house is $1M. If a buyer has a good credit, they need to put a down payment 10% otherwise they need to put a down payment of 20%. Then down payment.
# price = 1000000
# has_good_credit = False
# if has_good_credit:
#     down_payment =0.1 * price
# else:
#     down_payment = 0.2 *price
# print(f"Down Payment: ${down_payment}")
