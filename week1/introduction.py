# Introduction to Python (What is different in Python?)

# One of the most common programming languages used in industry today (Specially in ML), faster development speed
# Easy to learn, and to therefor used when teaching concepts

# Whats different in Python?
# Indentation - brackets
# Very close to english
# interpreted language

# Data Types and Variables

# An integer is a whole number, without a fraction, while a float is a real number that can contain a fractional part.
# For example, 1, 7, 342 are all integers, while 5.3, 3.14159 and 6.0 are all floats.
# (complex not covered)

a = 5       # int
b = 5.4     # float

# In Python, text in between quotes -- either single or double quotes -- is a string data type.
c = "test 1"
d = 'text 2'
e = """
    t
    e
    x
    t
    3
    """

# Binary types, boolean types not needed right now
# We will get back to lists, sets, dict in next sessions

# Variable names can be arbitrarily long. They can contain both letters and digits,
# but they have to begin with a letter or an underscore (private variables)
# case matters. Good practice never to use CAPs
A = 15

# Type
type(23)
type(a)


# Type converter functions
# When attempting to mix incompatible data types, you may encounter a TypeError.
# You can always check the data type of something using the type() function.
str_a = "5"
type(str_a)
f = str_a + a # TypeError
f = int(str_a) + a

# Other useful str(), float()
print("Answer is " + a)
print("Answer is " + str(a))

# More about strings later

# ValueError
int("23 bottles")

# Expressions
a = 5
b = 3
a + b # a + b = Adds a and b
a - b # a - b = Subtracts b from a
a * b # a * b = Multiplies a and b
a / b # a / b = Divides a by b
a ** b # a ** b = Elevates a to the power of b. For non integer values of b, this becomes a root
# (i.e. a**(1/2) is the square root of a)
a // b # a // b = The integer part of the integer division of a by b
a % b # a % b = The remainder part of the integer division of a by b

# Short hand
a += 1 # same as a = a + 1
# can be similarly with any other operand above Ex: a **= 5 is same as a = a ** 2 (ie a^2)


# Defining Functions, Returning Values (Notice, no brackets)
# Allows us to reuse the code

def my_function():
  print("Hello from a function")


def add(in_1, in_2):
    return in_1 + in_2


def sub(in_1, in_2):
    return in_1 - in_2


# Normal arguments
sub1 = sub(2, 1)
# Keyword Arguments
sub2 = sub(in_2=2, in_1=1)


# Passing functions and default parameters
def operate(in_1, in_2, operator=add):
    return operator(in_1, in_2)


print(operate(3, 2, sub))
print(operate(3, 2))

# Comparing Things (logical expressions)
c1 = 3
c2 = 4
c1 == c2               # c1 is equal to c2
c1 != c2               # c1 is not equal to c2
c1 > c2                # c1 is greater than c2
c1 < c2                # c1 is less than c2
c1 >= c2               # c1 is greater than or equal to c2
c1 <= c2               # c1 is less than or equal to c2

# What does this mean for stings ?
# checks the alphabetical order
"aa" > "ab" # false
"ac" > "ab" # true


# Logical operators and, or, not
c1 == 3 and c2 == 4
c1 == 3 or "ac" > "ab"


# Branching with if Statements
if c1 == 3 or "ac" > "ab":
    print("passed the test")

a = '' # empty string, False
# same goes for empty array, 0 int, None
if a:
    print("passed the test")
