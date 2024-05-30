tempeture = 11
if tempeture >30 :
    print("it's a hot day")
elif tempeture <10 :
    print ("it's a cold day")
else:
    print("It's neither cold nor Hot")

#2
name = "hj"
if len(name) <3 :
    print("Name must be atleast 3 characters")
elif len(name) >50:
    print("Name must not be 50 characters")
else:
    print("Name looks good")

#bb
number = int(input("enter the number  "))
for count in range(1,101):
   sum = number + count
   print (number, "+" , count, "=", sum )