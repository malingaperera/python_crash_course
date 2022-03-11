a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# get the squares
b = [x*2 for x in a]
# get the squares in even
c = [x*2 for x in a if x%2==0]
# get the squares in even if they are divisible by 8, 1 if not
d = [x*2 if (x*2 % 8 == 0) else 1 for x in a if x%2==0]

# will be handy when you want to convert all lines to ints
with open("in.txt", "r") as f:
    lines = f.readlines()
    print(lines)
    lines = [int(l) for l in lines]
    print(lines)

# or you can apply a whole function on a list
def my_func(x):
    x = x**2
    x = x +2
    x = x/3
    return x

b = [my_func(x) for x in a]