import numpy as np
# Numpy常用函数
'''
ravel和flatten区别：
两者的区别在于ravel方法生成的是原数组的视图，无需占有内存空间，但视图的改变会影响到原数组的变化。
而flatten方法返回的是真实值，其值的改变并不会影响原数组的更改。
'''
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
# 多维转一维数组 - ravel()
arr1_1 = arr1.ravel()
print(arr1_1)
arr1_1[:6] = 0
print(arr1_1)
print(arr1)
print('-'*80)
arr2 = np.array([
    [1, 3, 5, 10],
    [10, 30, 50, 100],
    [100, 300, 500, 1000],
    [1000, 3000, 5000, 10000],
    [10000, 30000, 50000, 100000],
])
print(arr2)
print(arr2.shape)    # 数据行列数
print(arr2.dtype)    # 数据类型
# 多维转一维数组 - flatten()
arr2_1 = arr2.flatten()
print(arr2_1)
arr2_1[:6] = 0
print(arr2_1)
print(arr2)
print(f'Data rows {len(arr2)}')     # 数据行数
print('-'*80)
# 横向拼接两个数组-前提是两个数组的行数要相同hstack()或者column_stack()
arr1 = np.array([
    [1, 2, 3, 4, 5],
    [10, 20, 30, 40, 50],
    [100, 200, 300, 400, 500],
    [1000, 2000, 3000, 4000, 5000],
])
arr2 = np.array([
    [6, 7, 8, 9],
    [60, 70, 80, 90],
    [600, 700, 800, 900],
    [6000, 7000, 8000, 9000],
])
print('Array 1:\n', arr1)
print('Array 2:\n', arr2)
arr3_1 = np.hstack([arr1, arr2])
arr3_2 = np.column_stack([arr1, arr2])
print('Array3-1:\n', arr3_1)
print('Array3-2:\n', arr3_2)
print('-'*80)
# 纵向拼接-前提是列数必须相同
arr1 = np.array([
    ['a', 'b', 'c'],
    ['d', 'e', 'f'],
    ['g', 'h', 'i'],
    ['j', 'k', 'l'],
])
arr2 = np.array([
    ['1', '2', '3'],
    ['4', '5', '6'],
    ['7', '8', '9'],
])
arr_t1 = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90],
])
arr_t2 = np.array([
    [100, 200, 300],
    [400, 500, 600],
    [700, 800, 900],
])
print('Array 1:\n', arr1)
print('Array 2:\n', arr2)
arr3_1 = np.vstack([arr1, arr2])
arr3_2 = np.row_stack([arr1, arr2])
# print('Array 3:\n', arr3_1)
# arr_t3 = np.vstack([arr_t1, arr_t2])
print('Array temp 3-1:\n', arr3_1)
print('Array temp 3-2:\n', arr3_2)