magicians = ["tom","ken", "liam", "abel"]
for magician in magicians:
    print(f"Hello {magician.title()}, that was a grat trick ")
    print(f"I can't wait to see you again nexttime {magician.title()}. \n")

print("Thank you for your perfomance")

# Do it yourself
# Think of at least three kinds of your favorite pizza. Store these
# pizza names in a list, and then use a for loop to print the name of each pizza.
#  Modify your for loop to print a sentence using the name of the pizza
# instead of printing just the name of the pizza. For each pizza you should
# have one line of output containing a simple statement like I like pepperoni
# pizza.
# Add a line at the end of your program, outside the for loop, that states
# how much you like pizza. The output should consist of three or more lines
# about the kinds of pizza you like and then an additional sentence, such as
# I really love pizza!
pizzas = ["Margherita", "Pepperoni", "Hawaiian", "Veggie","Supreme", "Pesto"]
for pizza in pizzas:
    print(pizza)
    print (f"I like {pizza}")
print("I really love pizza, they are sweet")

#Using range() to Make a List of Numbers
numbers= list(range(1,6))
print (numbers)

# making a list of the first 10
# square numbers (that is, the square of each integer from 1 through 10)
squares = []
for value in range(1,11):
    square = value **2
    squares.append(square)
print (squares)

#or
squares = []
for value in range (1,11):
    squares.append(value**2)
print (squares)
print (min(squares))
print (max(squares))
print (sum(squares))

#list comprehensions 
squares = [value**2 for value in range(1,11)]
print(squares)

#DO IT YOURSELF
# 4-3. Counting to Twenty: Use a for loop to print the numbers from 1 to 20,
# inclusive.
# 4-4. One Million: Make a list of the numbers from one to one million, and then
# use a for loop to print the numbers. (If the output is taking too long, stop it by
# pressing ctrl-C or by closing the output window.)
# 4-5. Summing a Million: Make a list of the numbers from one to one million,
# and then use min() and max() to make sure your list actually starts at one and
# ends at one million. Also, use the sum() function to see how quickly Python can
# add a million numbers.
# 4-6. Odd Numbers: Use the third argument of the range() function to make a
# list of the odd numbers from 1 to 20. Use a for loop to print each number.
# 4-7. Threes: Make a list of the multiples of 3 from 3 to 30. Use a for loop to
# print the numbers in your list.
# 4-8. Cubes: A number raised to the third power is called a cube. For example,
# the cube of 2 is written as 2**3 in Python. Make a list of the first 10 cubes (that
# is, the cube of each integer from 1 through 10), and use a for loop to print out
# the value of each cube
# Cube Comprehension: Use a list comprehension to generate a list of the
# first 10 cubes.
# for number in range(1,21,1): 
#     print (number)
# numbers =[]
# for number in range(10000001):
#     numbers.append(number)
# #print (numbers)
# print(min (numbers))
# print(max (numbers))
# print(sum (numbers))

# odd_numbers =[odd_number for odd_number in range(1,21,2)]
# print(odd_numbers)
# multiple_of_three =[number for number in range (3,31,3)]
# print(multiple_of_three)

# cubes = []
# for number in range(1,11):
#     cube = number**3 
#     cubes.append(cube)
# print(cubes)

# cubes = [number **3 for number in range(1,11)]
# print(cube)

#Slicing a list

cars = ["bmw", "subaru", "benz", "toyota","nissan", "honda", "mazda"]
print("\n")
print(cars[1:4])
print(cars[:3])
print(cars[2:])

for car in cars[1:4]:
    print("\n", car, "\n")

# copying a list
new_cars = cars[:]
print ("\n", new_cars)
new_cars.append("tesla")
print("\n",cars, "\n")
print (new_cars)

#Try It Yourself
# 4-10. Slices: Using one of the programs you wrote in this chapter, add several
# lines to the end of the program that do the following:
# •	 Print the message The first three items in the list are:. Then use a slice to
# print the first three items from that program’s list.
# •	 Print the message Three items from the middle of the list are:. Use a slice to
# print three items from the middle of the list.
# •	 Print the message The last three items in the list are:. Use a slice to print the
# last three items in the list.
# 4-11. My Pizzas, Your Pizzas: Start with your program from Exercise 4-1
# (page 56). Make a copy of the list of pizzas, and call it friend_pizzas.
# Then, do the following:
# •	 Add a new pizza to the original list.
# •	 Add a different pizza to the list friend_pizzas.
# •	 Prove that you have two separate lists. Print the message My favorite
# pizzas are:, and then use a for loop to print the first list. Print the message
# My friend’s favorite pizzas are:, and then use a for loop to print the second list. Make sure each new pizza is stored in the appropriate list.
magicians = ["tom","ken", "liam", "abel"]
print(f"The first three items are: {magicians[:3]}")
print(f"The last three items are: {magicians[1:]}")
#print(f"The two items form the middle are: {magicians[1:]}")

pizzas = ["Margherita", "Pepperoni", "Hawaiian", "Veggie","Supreme", "Pesto"]
friend_pizzas = pizzas[:]
print(friend_pizzas)
friend_pizzas.append("Chicken")
print("\n", friend_pizzas)
print ("\nMy favourite pizzaz are:")
for pizza in pizzas:
    print (pizza)
print("\nMy friends favourite pizzas are:")
for friends_pizza in friend_pizzas:
    print(friends_pizza)


# Try It Yourself
# 4-13. Buffet: A buffet-style restaurant offers only five basic foods. Think of five
# simple foods, and store them in a tuple.
# •	 Use a for loop to print each food the restaurant offers.
# •	 Try to modify one of the items, and make sure that Python rejects the
# change.
# •	 The restaurant changes its menu, replacing two of the items with different
# foods. Add a line that rewrites the tuple, and then use a for loop to print
# each of the items on the revised menu.

foods = ("Pilau", "Sembe", "Matoke", "Rice", "Arosto")
print (foods)
#foods [3]= "chapo"
#print(foods)
new_foods = ("Dondo", "Sembe", "Uji", "Rice", "Arosto")
print(new_foods)
for new_food in new_foods:
    print(new_food)

