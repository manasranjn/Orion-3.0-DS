import numpy as np

# str = input("Enter string ")
#
# length = len(str)
# mid = length//2
#
# if length%2 == 0:
#     middle = str[mid-1: mid+1]
# else:
#     middle = str[mid]
#
# revStr = str[::-1]
# print(middle)
# print(revStr)



a = np.array([1,2,3,4,5])
b = np.array([[1,2,3, 5], [4,5,6, 2], [1,2,3,4]])
c = np.zeros(50)
# print(c)
d = np.ones(50)
# print(d)
e = b.reshape(2,6)
# print(b)
# print(e)
x = np.arange(10)
# print(x)
y = np.arange(10, 20)
# print(y)
p = np.arange(1,10,3)
# print(p)
linearArr = np.linspace(1,5, 10)
# print(linearArr)
z = np.array([[1,2,3,4,5], [6,7,8,9,10], [11,12,13,14,15]])
# print(z.min())
# print(z.max())
oneD = z.ravel()
# print(oneD)
# print(b.sum())
# print(b)
# print(b.sum(axis=0))
# print(b.sum(axis=1))
one = np.array([[1,2,3],[2,3,4],[2,5,7]])
two = np.array([[4,2,3],[2,36,4],[9,5,7]])
# print(one + two)
sum = one.dot(two)
# print(sum)
print(np.std(one))