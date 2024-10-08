# Numpy数组属性
import numpy as np
# Numpy数组的属性
arr1 = np.array([
    [1, 3, 5, 10],
    [10, 30, 50, 100],
    [100, 300, 500, 1000],
    [1000, 3000, 5000, 10000],
    [10000, 30000, 50000, 100000],
])
print(arr1)
print(f'{arr1.shape}: {arr1.shape[0]} X {arr1.shape[1]}')   # 数据行列数
print(arr1.dtype)   # 数据类型
print(arr1.ndim)    # 数据维度
print(arr1.size)    # 数据个数
print('-' * 80)
# 数组转置 - 行列变换
rev_arr = arr1.T
print(rev_arr, type(rev_arr))
print(f'{rev_arr.shape}: {rev_arr.shape[0]} X {rev_arr.shape[1]}')   # 数据行列数
print(rev_arr.dtype)
print(rev_arr.ndim)
print(rev_arr.size)
print('-'*80)
arr = np.zeros((5, 10, 3), dtype='int32')
print(arr)
print(f'Array shape {arr.shape}, data type {arr.dtype}, dimension {arr.ndim}, size {arr.size}')
print('-' * 80)
tags = [['1308', '1308', '1308', '1', '2', '5'],
        ['01101', '1', '2', '5', '9101', '9101'],
        ['', '1', '2', '5', '1308', '8202', '2202'],
        ['', '1', '2', '5', '4201', '1303', '1204']
    ]
numbers = [['1             ', '1             ', '1             ', '1             ', '2    ', '6'],
           ['1             ', '1             ', '22', '55', '1             ', '1             '],
           ['1             ', '1             ', '60', '90', '0', '1             ', '1             '],
           ['1             ', '255', '90', '60', '1             ', '1             ', '1             ']
    ]
dicts = [dict(zip(tags[i], numbers[i])) for i, tag in enumerate(tags)]
for i, tag in enumerate(tags):
    print(f'Index is {i}, tag is {tag}')
print('Dictionaries :', dicts)
print('-' * 80)
for index, value in enumerate(dicts):
    print(f'Index is {index}, values {value}')
    column = 'num' + str(index+1)
    for tag, num in value.items():
        sql = f'''
            update aaa
            set {column} = {num}
            where tag = {tag}
        '''
        print(sql)
        print('~' * 30)
    print('=' * 80)