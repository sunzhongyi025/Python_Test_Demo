## numpy & pandas
import np as np
import pandas as pd
import numpy as np

print('------------------')
# array = np.array([[1, 2, 3],
#                  [4, 5, 6],
#                  [5, 8, 9],
#                  [2, 5, 9]],
#                 dtype=np.float32)
# print(array.dtype)
# print('number of dem:', array.ndim)
# print('shape of dem:', array.shape)
# print('size:', array.size)

# a = np.empty((5, 6), dtype=np.int)
# print(a)

# a = np.arange(10, 26, 3).reshape((2, 3))
# a = np.linspace(0, 11, 20).reshape((10, 2))
# print(a)
print('------------------')
# a = np.array([[10, 20, 30, 40], [1, 2, 3, 4],
#              [5, 6, 7, 8], [11, 22, 33, 44]])
# b = np.arange(16).reshape((4, 4))

# d = np.dot(a, b)  # 矩阵运算
# d = a * b  # 普通运算
# print(d < 20)
# print(d)
print('------------------')
# a = np.random.random((2, 4))
# print(np.sum(a, axis=1))
# print(np.min(a, axis=0))

print('------------------')
# a = np.arange(2, 14).reshape((3, 4))

# print(np.argmin(a))
# print(np.mean(a, axis=0))
# print(np.median(a))
# print(np.cumsum(a))
# print(np.diff(a, axis=0))
# print(np.nonzero(a))

# print(a.T)  # 行列变换
# print(np.clip(a, 10, 11)) # 小于10的全是10，大于10的全是11

# print('Index')
# A = np.arange(3,15).reshape(3,4)
# print(A)
# print(A[2])# 索引出行数
# print(A[1,:])# ：代表所有数
# print('------')
# for row in A:
#    print(row)
# print('------')
# for col in A.T:
#    print(col)
# A.flattern()# 把矩阵A变成一行数
# for item in A.flat:   #
#    print(item)
# print('------------------')


print('--------------合并-------------')

# A = np.linspace(0, 1, 10).reshape((2, 5))
# B = np.array([[1, 1, 1, 1, 1],
#              [2, 2, 2, 2, 2]])

# 上下合并
# print(np.vstack((A, B)))

print('---------------')
# 左右合并
# print(np.hstack((B,A)))

#A = np.array([1, 1, 1])
# 行变列
#print(A[np.newaxis, :])  # 列上加维度
#print(A.shape)
#A = np.array([1, 1, 1])
#print(A[:, np.newaxis])  # 行上加维度
#print(A.shape)

#C = np.concatenate((A, B, B, A), axis=0) # 自己定义如何合并
