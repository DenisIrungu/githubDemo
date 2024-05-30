x = "variables"
y = 78
z = 43.98

def myfunc():
    global j 
    j = "welcome"
    print(y)
    
def funcfunc():
 print(j)
 print(x)

myfunc()
funcfunc()

def display_message (everone):
   print(f"Hello, {everone}, I'm learning python!")
display_message("Everyone")

def favourite_book(favourite):
    print(f"My favourite book is, {favourite.upper()}, I love!")
favourite_book("the river between")

