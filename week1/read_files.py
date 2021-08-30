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
with open("in.txt", "r") as f:
    lines = f.readlines()
    for line in lines:
        print(line)

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
