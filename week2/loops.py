for i in range(10):
    print(i)

a = ["a", "b", "c"]
for i in a:
    print(i)

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

i = 0
while True:
    print(i)
    i += 1
    if i == 6:
        break
