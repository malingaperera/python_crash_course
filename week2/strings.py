# string is a char sequence
a = 'apple'
a[0]
a[1:3]
a[::-1]

# checks str.isalpha(), str.isdecimal(), str.isdigit()
a.isalnum()

# there are many string functions that I will not go through, but below are some frequently used ones
a.split()
a.strip()

# check for substrings
'ap' in a
a.startswith('ap')
a.index('le')
