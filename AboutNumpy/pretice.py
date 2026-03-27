import random

import numpy as np
random_low = random.randint(0,5)

random_high = random.randint(random_low+1,random_low+100)

my_array = np.random.randint(random_low,random_high,(5,5))
print(my_array)

max_args = np.max(my_array)
print("最大值为:",max_args)
min_args = np.min(my_array)
print("最小值为:",min_args)
print("获取最大值的索引:",np.where(my_array == max_args))
print("获取最小值的索引:",np.where(my_array == min_args))
my_array[np.where(my_array == max_args)]=1
my_array[np.where(my_array == min_args)]=0
my_array_new = my_array.astype(float)
# print("获取除去最大和最小值的其他值的索引:",middle_nums = np.where( (my_array<max_args)  & (my_array>min_args)))

middle_nums = np.where( (my_array<max_args)  & (my_array>min_args))
my_array[middle_nums] = np.random.random(np.sum(middle_nums))
print(my_array_new)