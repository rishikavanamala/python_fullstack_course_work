"""
=========================================
PYTHON STRINGS - COMPLETE BASIC GUIDE
All Important String Concepts in One File
=========================================
"""

# =========================================
# 1. CREATING STRINGS
# =========================================
print("---- Creating Strings ----")

s1 = "Hello"
s2 = 'World'
s3 = """This is
a multi-line
string"""

print(s1)
print(s2)
print(s3)


# =========================================
# 2. STRING INDEXING
# =========================================
print("\n---- String Indexing ----")

text = "Python"

print(text[0])   # First character
print(text[3])   # Character at index 3
print(text[-1])  # Last character


# =========================================
# 3. STRING SLICING
# =========================================
print("\n---- String Slicing ----")

print(text[0:4])   # From index 0 to 3
print(text[:3])    # Start to index 2
print(text[2:])    # Index 2 to end
print(text[::-1])  # Reverse string


# =========================================
# 4. STRING LENGTH
# =========================================
print("\n---- Length of String ----")

print(len(text))


# =========================================
# 5. STRING CONCATENATION
# =========================================
print("\n---- Concatenation ----")

a = "Hello"
b = "World"

print(a + " " + b)


# =========================================
# 6. STRING REPETITION
# =========================================
print("\n---- Repetition ----")

print("Hi " * 3)


# =========================================
# 7. STRING METHODS - CASE CONVERSION
# =========================================
print("\n---- Case Conversion ----")

name = "python programming"

print(name.upper())     # Uppercase
print(name.lower())     # Lowercase
print(name.title())     # Title case
print(name.capitalize())# First letter capital


# =========================================
# 8. STRING SEARCHING
# =========================================
print("\n---- Searching ----")

print(name.find("python"))   # Returns index
print(name.count("m"))       # Count occurrences
print("pro" in name)         # Membership check


# =========================================
# 9. STRING REPLACE
# =========================================
print("\n---- Replace ----")

print(name.replace("python", "Java"))


# =========================================
# 10. STRIP (REMOVE SPACES)
# =========================================
print("\n---- Strip ----")

text2 = "   hello   "

print(text2.strip())   # Remove both sides spaces
print(text2.lstrip())  # Remove left spaces
print(text2.rstrip())  # Remove right spaces


# =========================================
# 11. SPLIT AND JOIN
# =========================================
print("\n---- Split and Join ----")

sentence = "I love Python"

words = sentence.split()  # Convert to list
print(words)

joined = "-".join(words)  # Join with -
print(joined)


# =========================================
# 12. STRING CHECK METHODS
# =========================================
print("\n---- Check Methods ----")

print("abc".isalpha())     # Only letters
print("123".isdigit())     # Only numbers
print("abc123".isalnum())  # Letters + numbers
print("HELLO".isupper())   # Uppercase check
print("hello".islower())   # Lowercase check


# =========================================
# 13. STRING FORMATTING
# =========================================
print("\n---- String Formatting ----")

name = "Rishika"
age = 21

# Method 1: Concatenation
print("My name is " + name + " and I am " + str(age))

# Method 2: format()
print("My name is {} and I am {}".format(name, age))

# Method 3: f-string (Best method)
print(f"My name is {name} and I am {age}")


# =========================================
# 14. ESCAPE CHARACTERS
# =========================================
print("\n---- Escape Characters ----")

print("Hello\nWorld")  # New line
print("Hello\tWorld")  # Tab space
print("She said \"Hi\"")  # Double quotes inside string


print("\n---- END OF STRING FILE ----")
