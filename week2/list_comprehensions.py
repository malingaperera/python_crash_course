a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
b = [x*2 for x in a]
c = [x*2 for x in a if x%2==0]

with open("in.txt", "r") as f:
    lines = f.readlines()
    print(lines)
    lines = [int(l) for l in lines]
    print(lines)

def my_func(x):
    x = x**2
    x = x +2
    x = x/3
    return x

b = [my_func(x) for x in a]