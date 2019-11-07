import numpy as np

# axis=0的时候，表示以外面的括号为准，将括号里面的元素相加，那么就是[1, 2] + [3, 4],
# 而axis=1的时候，表示以里面的括号为准，将括号里面的元素相加，那么就是[1 + 2][3 + 4]。
x = np.array([[1, 2], [3, 4]])
# print('x is %s' % x)
sum0 = np.sum(x, axis=0, keepdims=True)
# print('sum0 is %s' % sum0)
sum1 = np.sum(x, axis=1, keepdims=True)
# print('sum1 is %s' % sum1)

x = np.array([[1, 2], [3, 4]])
# print(x.shape)
# print(x.ndim)

x = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
# print(x.shape)
# print(x.ndim)

x = np.array([
    [
        [1, 2],
        [3, 4]
    ],
    [
        [5, 6],
        [7, 8]
    ],
    [
        [9, 10],
        [11, 12]
    ]
])
print(x.shape)
print(x.ndim)
# print(x[0, 1, 0])
# 选取axis为0的第一个元素
# print(x[0, :, :])
# 选取axis为0的第二个元素
# print(x[1, :, :])
# 选取axis为0的第三个元素
# print(x[2, :, :])
# 两个元素的和
print(np.sum(x, axis=0, keepdims=True))
print(np.sum(x, axis=0))

# print(np.sum(x, axis=1, keepdims=True))
# print(np.sum(x, axis=1))

# print(np.sum(x, axis=2, keepdims=True))
# print(np.sum(x, axis=2))

# print(np.sum(x, axis=-1, keepdims=True))
# print(np.sum(x, axis=-1))