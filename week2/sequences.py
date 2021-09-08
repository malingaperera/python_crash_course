# Lists, Tuples and Range

# collection of items (ordered)
a = [1, 2, 3, 4, 5]
b = (1, 2, 3, 4, 5)  # fixed size
c = range(1, 6)  # generator -> memory efficient, but not everything falls into a pattern


# list can be heterogeneous
d = [1, 1.23, "a", b]

# Operators
# in / not in
print(2 in a)

# concat
ab = a + list(b)

# multiply
a5 = a * 5


# getting items
print(a[2])
print(a[1:3])
print(a[0:5:2])

# Other
len(a)
min(a)
max(a)

# count
a.count(1)

# Data addition = only for mutable i.e. list
a[1] = 5
a[0:5:2] = [8, 8, 8]
a.append(6)

# delete
del a[1:3]  # a[1:3] = []

# adding all the elements of a seq to a list
a.extend(b)
a.extend(range(10))

# advance functions
a.reverse()
a.sort()

# sets
s1 = {1, 2, 3, 4}
s2 = {1, 2}

s1.add(5)
s2.remove(5)

s1.issubset(s2)
s1.issuperset(s2)

# intersection, union, etc.
len(s1)
3 in s1

