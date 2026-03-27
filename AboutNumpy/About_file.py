import numpy as np

arr = np.array([[0.,0.,1.,1.,2.,2.],
                [3.,3.,4.,4.,5.,5.],
                [6.,6.,7.,7.,8.,8.],
                [9.,9.,10.,10.,11.,11.]])
np.savetxt("arr.csv",arr,fmt="%d",delimiter=',33')

load_data = np.loadtxt("arr.csv",delimiter=',')
print(load_data)