# A list of key value pairs
# Key - any immutable (Strings, Ints, Tuples with stings and ints)
tel = {'jack': 4098, 'sape': 4139}
tel['guido'] = 4127


print(tel['jack'])
del tel['sape']

# returns list of keys (only)
list(tel)
tel.keys()
list(tel.keys())

tel.values()
list(tel.values())

# list of keys sorted
sorted(tel)

# check membership
if 'guido' in tel:
    print('Yes')

# Loops
for k in tel:
    print(tel[k])

for k, v in tel.items():
    print(k, v)


# Dictionary Comprehension
squares = {x: x*x for x in range(6)}

squares = {}
for i in range(6):
    squares[i] = i*i

# Dictionary Comprehension with if conditional
odd_squares = {x: x*x for x in range(11) if x % 2 == 1}
