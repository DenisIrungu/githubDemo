#multipleline string
x = """my name is denis,
denis has a family,
he is a determined father"""
print(x)
#Acceessing an element in a string
y = "my name is denis"
print(y[3])

#looping in string
w = "Denis"
for w in "Denis":
    print(w)

#checking length of a string
z ="my name is denis"
print(len(z))

#Checking whether a phrase is in as string
txt = "my name is denis"
print ("Irungu" in txt)

#if... else in string
k = "my name is denis"
if "irungu" in k:
    print("YES, Irungu is present")
else:
    print("No, Irungu is absent")

#not
txt = "my name is denis"
print ("Irungu" not in txt)

#if not
k = "my name is denis"
if "irungu" not in k:
    print("absent")
#Concatination 
x = 2
y = 4
z = x+y
print(z)
#f-String
x = 29
txt = f"I have {x} books"
print(txt)
#placeholders and modifiers
age = 20
txt = f"Toh is currently {age:.2f} old" 
print(txt)
#you can also add values directly
txt = f"Toh is {34/2} old"
print (txt)
#if...else inside placeholder
price = 30
txt = f"It's very{"expensive" if price>35 else "cheap"}"
print(txt)