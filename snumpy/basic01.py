# Numpy创建数据的方式
import numpy as np
# 创建数组 - Python: range()
l = range(10)
print(list(l))
# 创建数组 - Numpy: arange()
al = np.arange(10)
print(type(al), al)
# 普通创建，传入列表或元组即可(数据类型必须一致)
arr1 = np.array((1, 30, 32, 45, 100, 290))
print(f'{type(arr1)}, {arr1}')
arr1 = np.array([1, 30, 32, 45, 100, 290])
print(f'{type(arr1)}, {arr1}')
print('-'*80)
# 二维数组
arr = np.array([
    [1, 3, 5, 10],
    [10, 30, 50, 100],
    [100, 300, 500, 1000],
    [1000, 3000, 5000, 10000],
    [10000, 30000, 50000, 100000],
])
print(arr)
print('-'*80)
arr = np.array([
    (1, 3, 5, 10),
    (10, 30, 50, 100),
    (100, 300, 500, 1000),
    (1000, 3000, 5000, 10000),
    (10000, 30000, 50000, 100000),
])
print(arr)
print('-'*80)
arr = np.array((
    [1, 3, 5, 10],
    [10, 30, 50, 100],
    [100, 300, 500, 1000],
    [1000, 3000, 5000, 10000],
    [10000, 30000, 50000, 100000],
))
print(arr)
print('-'*80)
arr = np.array((
    (1, 3, 5, 10),
    (10, 30, 50, 100),
    (100, 300, 500, 1000),
    (1000, 3000, 5000, 10000),
    (10000, 30000, 50000, 100000),
))
print(arr)
print('-'*80)
# Numpy函数创建数组
arr = np.ones(4)    # 创建值均为1的个数为4的一维数组
print(arr)
print('-'*80)
arr = np.ones([3, 4])   # 创建值均为1的3X4(3行4列)的二维数据
print(arr)
print('-'*80)
arr = np.zeros(4)
print(arr)
print('-'*80)
arr = np.zeros([3, 4])
print(arr)
print('-'*80)
arr = np.empty(4)
print(arr)
print('-'*80)
arr = np.empty((3, 4))
print(arr)
print('-'*80)
arr = np.zeros((2, 4, 3))
print(arr)
print('-'*80)
# Numpy数组的属性
arr1 = np.array([
    [1, 3, 5, 10],
    [10, 30, 50, 100],
    [100, 300, 500, 1000],
    [1000, 3000, 5000, 10000],
    [10000, 30000, 50000, 100000],
])
print(arr1)
print(arr1.shape)    # 数据行列数
print(arr1.dtype)    # 数据类型