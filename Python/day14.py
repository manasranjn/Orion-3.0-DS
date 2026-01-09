# List inbuilt methods

a = [1,2,3,4,5,5,5,5, True, False, "Hello", "World"]
b = a
# print(a,b)
# b[6]= "Python"
# print(a,b)

# c = a.copy()
# print(c,a)
# c[6] = "Python"
# print(c,a)

# a.append("Python")
# print(a)

# a.insert(2,"Python")
# print(a)

# a.remove(5)
# print(a)

# d = [1,2,3,4,5]
# a.extend(d)
# print(a)

# a.pop(10)
# print(a)

# a.clear()
# print(a)

# print(a.count(5))
# print(a.index(False))

lst = [5,1,8,1,4,8,9,5,3,4,6,7,9]
# lst.sort()
# print(lst)

lst.reverse()
# print(lst)

# Modules in python

# import math
# print(math.pi)
# print(math.sqrt(16))
# print(math.pow(2,3))
# print(math.factorial(5))
#
# print(dir(math))

import function as f

a = f.sum(10,20)
b = f.sub(100,20)
print(a,b)
f.sayHello()