import numpy as np

a = np.arange(8)
# print('原始数组：')
# print(a)
# print('\n')

b = a.reshape(4, 2)
# print('修改后的数组：')
# print(b)

# 一维数组的加减乘除：
a1 = np.array([1, 2, 3, 4])
b1 = np.array([4, 3, 2, 1])

s1 = a1 + b1  # s1的值为array([5, 5, 5, 5])
# print(s1)
d1 = a1 - b1  # d1的值为array([-3, -1,  1,  3])
# print(d1)
p1 = a1 * b1  # p1的值为array([4, 6, 6, 4])
# print(p1)
q1 = a1 / b1  # q1的值为array([0.25,0.66666667,1.5 ,4.])
# print(q1)

# 二维数组的加减乘除：
a2 = np.array([[2, 3, 4], [1, 2, 5]])
# print(a2)
b2 = np.array([[1, 2, 3], [2, 3, 4]])
# print(b2)

s2 = a2 + b2  # s2的值为array([[3, 5, 7],[3, 5, 9]])
# print(s2)
d2 = a2 - b2  # d2的值为array([[ 1,  1,  1],[-1, -1,  1]])
# print(d2)
p2 = a2 * b2  # p2的值为array([[ 2,  6, 12],[ 2,  6, 20]])
# print(p2)
q2 = a2 / b2  # q2的值为array([[2.,1.5,1.33333333],[0.5 ,0.66666667,1.25]])
# print(q2)

# 一维数组的点积：
a3 = np.array([1, 2, 3, 4])
b3 = np.array([2, 3, 4, 5])
dp1 = np.dot(a3, b3)  # dp1的值为40
# print(dp1)
dp2 = a3 @ b3  # dp2的值为40
# 运算符@等价于点积运算函数np.dot
# print(dp2)

# 二维数组的点积：
a4 = np.array([[1, 2, 3], [2, 3, 4]])
b4 = np.array([[1, 2], [2, 5], [0, 1]])
dp3 = np.dot(a4, b4)  # dp3的值为array([[ 5, 15],[ 8, 23]])
# print(dp3)
dp4 = a4 @ b4  # dp4的值为array([[ 5, 15],[ 8, 23]])
# 运算符@等价于点积运算函数np.dot
# print(dp4)

# 二维数组与一维数组的点积：
a5 = np.array([[1, 2, 3], [2, 3, 4]])
# b5 = np.array([1, 2, 3])
b5 = np.array([1, 2, 3])
# dp5 = np.dot(a5, b5)  # dp5的值为array([14, 20])
dp6 = a5 @ b5  # dp6的值为array([14, 20])
# print(dp6)
dp7 = a5 * b5
print(dp7)