student = {'Name': 'Denis', 'Age': '28', 'Course': 'IT' }
print(student)
age = student ['Age']
print(age)
student ['Department'] = 'Information Tech'
student ['School'] = 'Of Science'
print(student)
student ['Name']= 'Toh'
print(student)
del student['School']
print(student)
names = {'Toh':2, 'Deno':3, 'Liam': 4, 'Layne':5, 'Irungu': 6}
for name, number in names.items():
    print(f"{name} your favourite number is {number}") 
for values in student.values():
    print(values)

# Rivers: Make a dictionary containing three major rivers and the country
# each river runs through. One key-value pair might be 'nile': 'egypt'.
# •	 Use a loop to print a sentence about each river, such as The Nile runs
# through Egypt.
# •	 Use a loop to print the name of each river included in the dictionary.
# •	 Use a loop to print the name of each country included in the dictionary.
rivers = {"Tana": "Kenya",
          "Nile": "Egypt",
          "Congo River": "Congo"}
for river , country in rivers.items():
    print(f"River {river} runs through {country}")
for river in rivers.keys():
    print(river)

for country in rivers.values():
    print(country)


# Polling: Use the code in favorite_languages.py (page 97).
# •	 Make a list of people who should take the favorite languages poll. Include
# some names that are already in the dictionary and some that are not.
# •	 Loop through the list of people who should take the poll. If they have
# already taken the poll, print a message thanking them for responding.
# If they have not yet taken the poll, print a message inviting them to take
# the poll.

favorite_languages = {
 'jen': 'python',
 'sarah': 'c',
 'edward': 'ruby',
 'phil': 'python',
 }
people_to_poll = ['phil', 'sarah','toh', 'edward','liam']
for person in people_to_poll:
    if person in favorite_languages:
        print(f"Thank you {person.title()} for taking part in the polling")
    else:
        print (f"{person.title()} you are invited to take the poll")
#NESTING
student_1 = {'Name': 'Denis', 'Age': '28', 'Course': 'IT' }
student_2 = {'Name': 'Ken', 'Age': '23', 'Course': 'Education' }
student_3 = {'Name': 'Toh', 'Age': '26', 'Course': 'COM' }

Students = [student_1, student_2, student_3]
for student in Students:
    print ("\n",student)


studs = []
for stud in range(30):
    new_stud = student_1 = {'Name': 'Denis', 'Age': '28', 'Course': 'IT' }
    studs.append(new_stud)

for stud in studs[:5]:
    print(studs)
print("...")
print (f"The total number of students is: {len(studs)}")

