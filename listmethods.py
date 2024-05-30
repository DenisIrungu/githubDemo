# names =["toh", "liam", "layne"]
# print (names)
# second_born = names.pop(1)
# print(f"my first born is called: {second_born}")

# #remove()
# cars = ["toyota", "nissan", "benz", "bmw", "volkswagen"]
# print(cars)
# #cars.remove("benz")
# too_expensive = "benz"
# cars.remove(too_expensive)
# print(f"\n {too_expensive} is too expensive to manage")

#try it yourself
# 3-4. Guest List: If you could invite anyone, living or deceased, to dinner, who
# would you invite? Make a list that includes at least three people you’d like to
# invite to dinner. Then use your list to print a message to each person, inviting
# them to dinner
names = ["Toh", "Liam", "Layne"]
for name in names:
 print (f"Hello,{name} your are invited for dinner")
# 3-5. Changing Guest List: You just heard that one of your guests can’t make the
# dinner, so you need to send out a new set of invitations. You’ll have to think of
# someone else to invite.
# •	 Start with your program from Exercise 3-4. Add a print() call at the end
# of your program stating the name of the guest who can’t make it.
# •	 Modify your list, replacing the name of the guest who can’t make it with
# the name of the new person you are inviting.
# •	 Print a second set of invitation messages, one for each person who is still
# in your list.

names = ["Toh", "Liam", "Layne"]
for name in names:
  print (f"\nHello,{name} your are invited for dinner")
  print(f"Apologies,{names[1]} won't make it")

names[1] = "Gitonga"
print (names)
for name in names:
  print(f"\nHello, {name} you are invited for a dinner")

# More Guests: You just found a bigger dinner table, so now more space is
# available. Think of three more guests to invite to dinner.
# •	 Start with your program from Exercise 3-4 or Exercise 3-5. Add a print()
# call to the end of your program informing people that you found a bigger
# dinner table.
# •	 Use insert() to add one new guest to the beginning of your list.
# •	 Use insert() to add one new guest to the middle of your list.
# •	 Use append() to add one new guest to the end of your list.
# •	 Print a new set of invitation messages, one for each person in your list.
names = ["Toh", "Liam", "Layne"]
msg = f"\Apologies,{names[1].upper()} won't make it"
print (msg.title())
names[1] = "Gitonga"
print (names)
for name in names:
  print(f"\n Hello,{names} you are invited for dinner")


msg = "\nHello guys, i found a bigger table"
print(msg.upper())
names.insert(0, "Masika")
names.insert(1, "Irungu")
names.append("Gitonga")
print(names)
for new_names in names:
  print(f"\n Hello {new_names}, you are invited for a dinner")
msg = "\n Sincere apologies, the new dinner table won't arrive on time and therefore i can only manage to accomodate two people"
print(msg.title())
last_name = names.pop()
print(f"\n I'm really sorry {last_name} i can't invite you for a dinnr due to unavoidable circumstances")
last_name = names.pop()
print(f"\n I'm really sorry {last_name} i can't invite you for a dinnr due to unavoidable circumstances")
last_name = names.pop()
print(f"\n I'm really sorry {last_name} i can't invite you for a dinnr due to unavoidable circumstances")
last_name = names.pop()
print(f"\n I'm really sorry {last_name} i can't invite you for a dinnr due to unavoidable circumstances")
print (names)

for name in names:
  msg = f"\n hello {name} I'm happy to let you know that you're still invited for a dinner"
  print(msg.title())

del names[0]
del names[0]

print (names)

#Arranging lists temporarly using sorted () function
cars = ["Bmw", "Audi", "Benz", "Range"]
sorted_cars = sorted(cars)
print(sorted_cars)

# Do it yourself
# Try It Yourself
# 3-8. Seeing the World: Think of at least five places in the world you’d like to
# visit.
# •	 Store the locations in a list. Make sure the list is not in alphabetical order.
# •	 Print your list in its original order. Don’t worry about printing the list neatly,
# just print it as a raw Python list.
# •	 Use sorted() to print your list in alphabetical order without modifying the
# actual list.
# •	 Show that your list is still in its original order by printing it.
# •	 Use sorted() to print your list in reverse alphabetical order without changing the order of the original list.
# •	 Show that your list is still in its original order by printing it again.
# •	 Use reverse() to change the order of your list. Print the list to show that its
# order has changed.
# •	 Use reverse() to change the order of your list again. Print the list to show
# it’s back to its original order.
# •	 Use sort() to change your list so it’s stored in alphabetical order. Print the
# list to show that its order has been changed.
# •	 Use sort() to change your list so it’s stored in reverse alphabetical order.
# Print the list to show that its order has changed.

countries = ["singapore","italy", "spain", "singapore", "china","dubai"]
print ("\n", countries)
sorted_countries = sorted(countries)
print("\n", sorted_countries)
print("\n", countries)

sorted_countries = sorted(countries, reverse= True)
print ("\n", sorted_countries)
print ("\n", countries)

countries.reverse()
print("\n", countries)
countries.reverse()
print("\n", countries)

countries.sort()
print("\n", countries)
countries.sort(reverse=True)
print("\n", countries)

# 3-9. Dinner Guests: Working with one of the programs from Exercises 3-4
# through 3-7 (page 42), use len() to print a message indicating the number
# of people you are inviting to dinner.

names = ["Toh", "Liam", "Layne"]
length = len(names)
print (length)
print (f"\n, I'm inviting {length} people only for a dinner")
print (f"\n, I'm inviting {len(names)} people only for a dinner")








