def name (fname, lname,mname=""):
    full_name = f"{fname} {lname} {mname}"
    return {full_name.upper()}


print(name("Deno", "Toh"))

#dic
student= {"name": "Denis"}
student["age"]= 23
student["course"]= "BIT"
print(student)

employee= {}
employee["salary"]= 700000
employee["job"] = "dev"
#print(employee)

employee["salary"]= 90000
#print(employee)
del employee["job"]
print(employee)

games = {
    "John": "football",
    "Denis": "netball",
    "Toh": "hockey"
}
c=games["Toh"]
print(f"my name is Toh i love {c}")

