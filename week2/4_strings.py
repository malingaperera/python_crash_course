# string is a char sequence
# See the similarity with lists, most of the things you did with a list can be done using a string
a = 'appledsasdfsle'
print(a[0])
print(a[1:3])
print(a[::-1])

# checks str.isalpha(), str.isdecimal(), str.isdigit()
a.isalnum()

# there are many string functions that I will not go through, but below are some frequently used ones
a.split()
a.strip()

# check for substrings
print('ap' in a)
a.startswith('ap')
a.index('le')
