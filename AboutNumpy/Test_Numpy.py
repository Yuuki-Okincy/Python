import numpy as np

my_array_a =np.array([[1,2],[3,4]])
my_array_b =np.array([[5,6],[7,8]])

# 这种方法产生的结果与使用np.hstack((my_array_a,my_array_b))方法产生的结果相同
my_array_new_a = np.concatenate((my_array_a,my_array_b),axis=1)
# 这种方法产生的结果与使用np.vstack((my_array_a,my_array_b))方法产生的结果相同
my_array_new_b = np.concatenate((my_array_b,my_array_a),axis=0)

# 将原数组垂直分割为俩个数组
my_array_new_c = np.split(my_array_a,2,axis=1)
# 将原数组水平分割为俩个数组
my_array_new_d = np.split(my_array_a,2,axis=0)
print(my_array_new_d)

