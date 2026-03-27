import numpy as np
from numpy.ma.core import cumprod

my_array = np.array([[0,1,2,3],
                     [4,5,6,7],
                     [8,9,10,11],
                     [12,13,14,15]])
print("数组求和结果为:",np.sum(my_array))
print("平均值为:",np.mean(my_array))
print("中位数:",np.median(my_array))
print("方差为:",np.var(my_array))
print("标准差为:",np.std(my_array))
print("数组所有元素的积累积:",cumprod(my_array))