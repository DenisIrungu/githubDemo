# list = ["#23", "#19", "#5", "#45","#63324","#5674", "#657"]
# def sorting (string):
#     return int(string[1:])
# sorted_list = sorted(list, key= sorting)
# print("sorted_list:", sorted_list)

# def add_num (NUm1, Num2):
#     sum = NUm1 + Num2
#     print("Sum: ", sum)
# add_num(5,4)

names = ["toh","liam", "layne","deno"]
print(names[1])
msg = f"My second born is called {names[1].title()}"
print(f"My first born is called {names[1].title()}")
print (msg)

# Think of your favorite mode of transportation, such as a
# motorcycle or a car, and make a list that stores several examples. Use your list
# to print a series of statements about these items, such as “I would like to own a
# Honda motorcycle.”
motocycles = ["kawasaki", "honda", "tvs", "boxer"]
for motocycle in motocycles:
  print(f"i would like to own a {motocycle.title()}")

#changing the value of elements.Eg. changing the value of tvs to nduthi,then;
motocycles = ["kawasaki", "honda", "tvs", "boxer"]
print (motocycles)
motocycles [2]= "nduthi"
print(motocycles)

motocycles = ["kawasaki", "honda", "tvs", "boxer"]
print (motocycles)
cheap_motocycle = "tvs"
motocycles.remove(cheap_motocycle)
print(f"the cheapest motocycle is {cheap_motocycle}")
