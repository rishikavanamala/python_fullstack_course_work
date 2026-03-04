"""
=========================================
PYTHON OPERATORS & TYPE CONVERSIONS
Very Basic - All in One File
=========================================
"""

# =========================================
# 1. ARITHMETIC OPERATORS
# =========================================
print("---- Arithmetic Operators ----")
a = 10
b = 3

print("Addition:", a + b)        # +
print("Subtraction:", a - b)     # -
print("Multiplication:", a * b)  # *
print("Division:", a / b)        # /
print("Floor Division:", a // b) # //
print("Modulus:", a % b)         # %
print("Power:", a ** b)          # **


# =========================================
# 2. COMPARISON OPERATORS
# =========================================
print("\n---- Comparison Operators ----")
x = 5
y = 10

print("Equal:", x == y)          # ==
print("Not Equal:", x != y)      # !=
print("Greater Than:", x > y)    # >
print("Less Than:", x < y)       # <
print("Greater Equal:", x >= y)  # >=
print("Less Equal:", x <= y)     # <=


# =========================================
# 3. LOGICAL OPERATORS
# =========================================
print("\n---- Logical Operators ----")
p = True
q = False

print("AND:", p and q)  # and
print("OR:", p or q)    # or
print("NOT:", not p)    # not


# =========================================
# 4. ASSIGNMENT OPERATORS
# =========================================
print("\n---- Assignment Operators ----")
num = 10

num += 5
print("+= :", num)

num -= 3
print("-= :", num)

num *= 2
print("*= :", num)

num /= 4
print("/= :", num)


# =========================================
# 5. BITWISE OPERATORS
# =========================================
print("\n---- Bitwise Operators ----")
a = 5  # 101 in binary
b = 3  # 011 in binary

print("AND:", a & b)       # &
print("OR:", a | b)        # |
print("XOR:", a ^ b)       # ^
print("NOT:", ~a)          # ~
print("Left Shift:", a << 1)   # <<
print("Right Shift:", a >> 1)  # >>


# =========================================
# 6. MEMBERSHIP OPERATORS
# =========================================
print("\n---- Membership Operators ----")
my_list = [1, 2, 3, 4]

print("2 in list:", 2 in my_list)        # in
print("5 not in list:", 5 not in my_list) # not in


# =========================================
# 7. IDENTITY OPERATORS
# =========================================
print("\n---- Identity Operators ----")
a = [1, 2]
b = [1, 2]
c = a

print("a is b:", a is b)          # is
print("a is c:", a is c)          # same object
print("a is not b:", a is not b)  # is not


# =========================================
# 8. TYPE CONVERSIONS
# =========================================
print("\n---- Type Conversions ----")

# int()
print("int('10'):", int("10"))
print("int(3.9):", int(3.9))

# float()
print("float('5.5'):", float("5.5"))
print("float(10):", float(10))

# str()
print("str(100):", str(100))
print("str(3.14):", str(3.14))

# bool()
print("bool(1):", bool(1))
print("bool(0):", bool(0))
print("bool('Hello'):", bool("Hello"))
print("bool(''):", bool(""))

# list()
print("list('hello'):", list("hello"))

# tuple()
print("tuple([1,2,3]):", tuple([1, 2, 3]))

# set()
print("set([1,2,2,3]):", set([1, 2, 2, 3]))


print("\n---- END OF FILE ----")
