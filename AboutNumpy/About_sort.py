import numpy as np

from AboutNumpy.About_random import my_array

my_array = np.array([[3,7],[9,1]])
print(my_array)
print("调用sort()函数:\n",np.sort(my_array))
print("按列排序:\n",np.sort(my_array,axis=0))
print(my_array[np.where(my_array > 3)])
