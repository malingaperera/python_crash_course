# File IO
f = open("in.txt", "r")
print(f.read())

f.close()

# Using with
with open("in.txt", "r") as f:
    print(f.read())

# Readline
with open("in.txt", "r") as f:
    print(f.readline())
    print(f.readline())

# Reading lines
# we will cover loops later
with open("in.txt", "r") as f:
    lines = f.readlines()
    for line in lines:
        print(line)

# looping will be covered again in next week
with open("in.txt", "r") as f:
    line = f.readline()
    while line:
        print(line)
        line = f.readline()

with open("in.txt", "r") as f:
    for line in f:
        print(line)

with open("in.txt", "r") as f:
    a = int(f.readline())
    for i in range(a):
        print(f.readline())

# more than one value in a line
with open("in2.txt", "r") as f:
    a = int(f.readline())
    for i in range(a):
        line = f.readline().strip()
        values = line.split()
        print(values[0] + ' got ' + str(int(values[1]) + int(values[2])) + ' marks')
        print(f"{values[0]} got {int(values[1]) + int(values[2])} marks")


# Writing and other modes (skipping x)
# r 	Open the file for reading (default).
# w 	Open the file for writing.
# a 	Open the file in append mode i.e add new data to the end of the file.
# r+ 	Open the file for reading and writing both

with open("out.txt", "w") as f:
    f.write('line1')
    f.write('line2')

with open("out.txt", "w") as f:
    f.write('line1' + '\n')
    f.write('line2' + '\n')

with open("out.txt", "a") as f:
    f.write('line1' + '\n')
    f.write('line2' + '\n')

with open("in.txt", "r") as f1, open("out.txt", "w") as f2:
    for line in f1:
        f2.write(line)

with open("in.txt", "r") as f1, open("out.txt", "w") as f2:
    f2.write(f1.read())
