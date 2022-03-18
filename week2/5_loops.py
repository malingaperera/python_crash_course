# A simple loop can be run on any iterable, like ranges, lists, dictionaries
for i in range(2, 10, 2):
    print(i)

a = ["a", "b", "c"]
for i in a:
    print(i)

# While loop is bit different as, it won't take care of variable definition and increment
# mostly used when the variable increment is not simple
i = 0
while i < 6:
    print(i)
    i += 1


# nested loops
for i in range(9):
    for j in range(10):
        print(i*10 + j)

# continue and break
for i in range(10):
    if i == 3:
        continue
    elif i == 8:
        break
    print(i)

# Breaks to stop infinite loops
i = 0
while True:
    print(i)
    i += 1
    if i == 6:
        break
