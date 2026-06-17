import numpy as np

a = np.arange(6)   # Creating an array with the range from 0 - 6
# print(a)
# print(a.shape)  # show the shape of array

a2 = a[np.newaxis, : ]  # Adding new dimention in the array change 1D to 2D
# print(a2)
# print(a2.shape)

a3 = a[  :, np.newaxis ]
# print(a3)
# print(a3.shape)

a4 = a2[np.newaxis, : ]  # change 2D to 3D
# print(a4)
# print(a4.shape)

arr = np.array([1,2,3,4,5,6])  #1D Array
brr = np.array([(1,2,3,4,5,6), (2,4,6,8,10,12)])  #2D Array
# print(arr)
# print(arr.shape)
# print(brr)
# print(brr.shape)

crr = np.zeros((3,5))  # Creating an array of 3x5 with all 0 values
# print(crr)

drr = np.ones((5, 7))  # Creating an array of 5x7 with all 1 values
# print(drr)

err = np.full((3,4), 5) # Creating an array of 3x4 with all 5 values
# print(err)

idn = np.eye(5,5)  # Create an identity matrix
# print(idn)
