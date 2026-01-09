import  numpy as np

l1 = [1,2,3,4,5,6,7,8,9]
# print(l1[0:5])

a1 = np.array([1,2,3,4,5,6,7,8,9])
# print(a1[0:5])
# print(a1[-2])

a2 = np.array([[1,2,3,10,11], [4,5,6,12,13], [7,8,9,14,15]])
# print(a2[1:3, 4])
# print(a2[1,1])
# print(a2[-1,0:2])
# print(a2[0, 2:4])
# print(a2[1,3:5])

# print(a2[:, 0:3])

b1 = a2 > 5
# print(b1)
a3 = a2[b1]
# print(a3)

# print(b1[1,1])

# Iterate
# l2 = [1,2,3,4,5,6,7,8,9]
# for i in l2:
#     print(i)

# for e in a1:
#     print(e)
#
# for r in a2:
#     print(r)

# for e in a2.flat:
#     print(e)

s1  = np.arange(20).reshape(4,5)
# print(s1)
s2 = np.arange(20).reshape(4,5)

s4 = np.vstack((s1,s2))
# print(s4)

s5 =np.hstack((s1,s2))
# print(s5)

s6 = np.arange(30).reshape(2,15)
# print(s6)
# s7 = np.hsplit(s6,3)
# print(s7)
s8 = np.vsplit(s6,2)
print(s8)