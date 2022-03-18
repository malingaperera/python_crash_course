import numpy

arr = numpy.array([[3 ,6, 9, 12], [15 ,18, 21, 24],
[27 ,30, 33, 36], [39 ,42, 45, 48], [51 ,54, 57, 60]])
print("Printing Input Array")
print(arr)

print("\n Printing array of odd rows and even columns")
ans1 = arr[::2, 1::2]
print(ans1)

ans2 = arr[:,[0, 3]]













arr2 = numpy.array([[34,43,73],[82,22,12],[53,94,66]])
# [[34 43 73]
#  [82 22 12]
#  [53 94 66]]
ans = numpy.sort(arr2, axis= 1, kind=None, order=None)
# [[73 43 34]
#  [12 22 82]
#  [66 94 53]]
ans2 = numpy.argsort(arr2, axis= 1, kind=None, order=None)

ans3 = arr2[:, numpy.argsort(arr2, axis= 1, kind=None, order=None)[1]]