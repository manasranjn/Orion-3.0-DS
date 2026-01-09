import numpy as np
import time

# size = 10000000
# l1 = range(size)
# l2 = range(size)
#
# a1 = np.arange(size)
# a2 = np.arange(size)
#
# start = time.time()
# result = [(x + y) for x, y in zip(l1, l2)]
# print("Python list took: ", (time.time() - start) * 1000)

# start = time.time()
# result = a1 + a2
# print("Numpy array took: ", (time.time() - start) * 1000)

a = np.array([1,2,3,4,5])
# print(a.dtype)

b = np.array([[1,2,3, 5], [4,5,6, 2], [1,2,3,4]])

# print(b)
print(a[2])
print(b[0,3])
print(a[1])
print(b[2,2])
print(b.size)
print(a.size)
print(b.shape)