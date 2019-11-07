# matrix是array的分支，matrix和array在很多时候都是通用的，你用哪一个都一样。但这时候，官方建议大家如果两个可以通用，
# 那就选择array，因为array更灵活，速度更快，很多人把二维的array也翻译成矩阵。
#
# 但是matrix的优势就是相对简单的运算符号，比如两个矩阵相乘，就是用符号*，但是array相乘不能这么用，得用方法.dot()
# array的优势就是不仅仅表示二维，还能表示3、4、5…维，而且在大部分Python程序里，array也是更常用的。

# *：               根据数据类型的不同，可能是做点乘运算，也可能做矩阵乘法运算
# @：               只做矩阵乘法运算
# .dot：            只做矩阵乘法运算
# np.mutiply：      只做点乘运算

import numpy as np

mylist = [[1, 2, 3], [4, 5, 6]]  # 列表
print(type(mylist))
print(mylist, end='\n\n')

myarray = np.array(mylist)  # 列表转数组
print(type(myarray))
print(myarray, end="\n\n")

mymatrix = np.mat(mylist)  # 列表转矩阵
print(type(mymatrix))
print(mymatrix, end='\n\n')

MatToArray = np.array(mymatrix)  # 矩阵转数组
print(type(MatToArray))
print(MatToArray, end='\n\n')

ArrayToMat = np.mat(myarray)  # 数组转矩阵
print(type(ArrayToMat))
print(ArrayToMat, end='\n\n')

MatToList1 = mymatrix.tolist()  # 矩阵转列表
print(type(MatToList1))
print(MatToList1)
MatToList2 = list(mymatrix)  # 注意点1
print(type(MatToList2))
print(MatToList2, end='\n\n')

ArrayToList1 = myarray.tolist()  # 矩阵转列表
print(type(ArrayToList1))
print(ArrayToList1)
ArrayToList2 = list(myarray)  # 注意点2
print(type(ArrayToList2))
print(ArrayToList2)