"""
=========================================
PYTHON DICTIONARY - COMPLETE BASIC GUIDE
All Important Dictionary Concepts in One File
=========================================
"""

# =========================================
# 1. CREATING A DICTIONARY
# =========================================
print("---- Creating Dictionary ----")

student = {
    "name": "Rishika",
    "age": 21,
    "course": "BTech"
}

print(student)


# =========================================
# 2. ACCESSING VALUES
# =========================================
print("\n---- Accessing Values ----")

print(student["name"])          # Access using key
print(student.get("age"))       # Using get() method


# =========================================
# 3. ADDING / UPDATING VALUES
# =========================================
print("\n---- Adding & Updating ----")

student["college"] = "ABC University"   # Add new key
student["age"] = 22                     # Update value

print(student)


# =========================================
# 4. REMOVING ITEMS
# =========================================
print("\n---- Removing Items ----")

student.pop("course")    # Remove by key
print(student)

# Remove last inserted item
student.popitem()
print(student)

# Delete using del
del student["age"]
print(student)


# =========================================
# 5. TAKING INPUT FROM USER
# =========================================
print("\n---- Taking Input ----")

person = {}

name = input("Enter name: ")
age = int(input("Enter age: "))
city = input("Enter city: ")

person["name"] = name
person["age"] = age
person["city"] = city

print("User Dictionary:", person)


# =========================================
# 6. LOOPING THROUGH DICTIONARY
# =========================================
print("\n---- Looping ----")

for key in person:
    print(key, ":", person[key])

print("\nKeys Only:")
for key in person.keys():
    print(key)

print("\nValues Only:")
for value in person.values():
    print(value)

print("\nKey-Value Pairs:")
for key, value in person.items():
    print(key, "=>", value)


# =========================================
# 7. DICTIONARY METHODS
# =========================================
print("\n---- Dictionary Methods ----")

print("Keys:", person.keys())
print("Values:", person.values())
print("Items:", person.items())
print("Length:", len(person))


# =========================================
# 8. CHECKING KEY EXISTENCE
# =========================================
print("\n---- Checking Key ----")

if "name" in person:
    print("Name exists")


# =========================================
# 9. CLEAR DICTIONARY
# =========================================
print("\n---- Clear Dictionary ----")

temp = {"a": 1, "b": 2}
print("Before clear:", temp)

temp.clear()
print("After clear:", temp)


# =========================================
# 10. NESTED DICTIONARY
# =========================================
print("\n---- Nested Dictionary ----")

students = {
    "student1": {"name": "A", "age": 20},
    "student2": {"name": "B", "age": 21}
}

print(students)

print("Access Nested Value:")
print(students["student1"]["name"])


# =========================================
# 11. COPYING DICTIONARY
# =========================================
print("\n---- Copy Dictionary ----")

original = {"x": 1, "y": 2}
copy_dict = original.copy()

print("Original:", original)
print("Copy:", copy_dict)


print("\n---- END OF DICTIONARY FILE ----")
