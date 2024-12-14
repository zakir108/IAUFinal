import matplotlib.pyplot as pt
import numpy as np



X1=np.array([1, 2, 3, 4,4.5,8]) # 800
X2 = X1.copy()
X3_view = X1.view()
x4 = X2
x4[0] = 500


arr = np.array([[1, 2, 3, 4,1], [5, 6, 7, 8,3],[5, 6, 7, 8,3]])
print(arr.shape)
print(arr)
print()
newarr = arr.reshape(5, 3)
print(newarr)

#pt.plot(numpyArryFrom_AR, numpyArryFrom_AR)  # Plot the chart
#pt.show()  # display
