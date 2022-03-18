import numpy
# https://pynative.com/python-numpy-exercise/

# Slicing - array of odd rows and even columns
arr = numpy.array([[3 ,6, 9, 12], [15 ,18, 21, 24],
[27 ,30, 33, 36], [39 ,42, 45, 48], [51 ,54, 57, 60]])
print("Printing Input Array")
print(arr)
# Printing Input Array
# [[ 3  6  9 12]
#  [15 18 21 24]
#  [27 30 33 36]
#  [39 42 45 48]
#  [51 54 57 60]]
#
# Printing array of odd rows and even columns
# [[ 6 12]
#  [30 36]
#  [54 60]]
#
# Select columns 0 and 3
# [[ 3 12]
#  [15 24]
#  [27 36]
#  [39 48]
#  [51 60]]


# Sort - Sort based on 2nd row
arr2 = numpy.array([[34,43,73],[82,22,12],[53,94,66]])
# [[34 43 73]
#  [82 22 12]
#  [53 94 66]]
ans = numpy.sort(arr2, axis= 1, kind=None, order=None)
# [[73 43 34]
#  [12 22 82]
#  [66 94 53]]
ans2 = numpy.argsort(arr2, axis= 1, kind=None, order=None)


