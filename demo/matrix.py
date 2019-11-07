import numpy as np

a6 = np.matrix([[1,2,3],[1,2,1]])
b6 = np.matrix([[1,2],[3,4],[2,3]])
print(a6)
print(b6)

p3 = a6 * b6         # p3的值为m10trix([[13, 19],[ 9, 13]])
p4 = np.dot(a6,b6)   # p4的值为m10trix([[13, 19],[ 9, 13]])
p5 = a6 @ b6         # p5的值为m10trix([[13, 19],[ 9, 13]])

print(p3)
print(p4)
print(p5)