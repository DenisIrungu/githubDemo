
#argument optional
def get_name (fname, lname, mname= ""):
    if mname:
        full_name = f"{fname} {lname} {mname}"
    else:
        full_name = f"{fname} {lname}"
    return full_name.title()
my_name = get_name("denis", "irungu", "kihara")
print(my_name)

#return dictionary
def building_person (fname, lname):
     person = {"first":fname, "last": lname}
     return person
builder = building_person("toh", "liam")
print(builder)
#de
def describe_city (city_name, country= "Kenya"):
    print(f"{city_name} is in {country}")

describe_city ("Nairobi")
describe_city("Adis", "Tanzania")
describe_city("Kampala", "Uganda")
    