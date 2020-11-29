#Numpy tester

import numpy as np

a=[[24,48,13], [21,15,23], [31,32,95]]
A=np.array(a)
print(A)

print ("This is the number of dimensions in the array:", A.ndim)
print("This is the height and width of the array:", A.shape)
print("This is the total number of elements in the array:", A.size)
print("Here is a selected element of the array in row 2, position 2:", A[1][1])
print("Here is a selected element of the array, in row 3, position 3:", A[2][2])