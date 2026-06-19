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

# print(drr.dtype)  # data type of array elements
# print(arr.dtype)
# print(crr.dtype)
# print(idn.dtype) 

# print(type(idn))  # type of array

# print("Length of brr: " , len(brr)) # give no. of rows

# print("Dimentions of arr: " , arr.ndim) # give dimentions of array
# print("Dimentions of idn: " , idn.ndim)

# print("Size of brr: ", brr.size) # give total numbers of array

# Basic Operation

ar1 = np.arange(5)
ar2 = np.array([(1,2,3,4,5), (10,20,30,40,50)])

print("ar1: ", ar1)
print("ar2: ", ar2)

# sum = ar1 + ar2  # Addition of two array / matrixes
# print("ar1 + ar2 : ",sum)

sum = np.add(ar1,ar2)   # Addition Method by numpy
print("sum: ",sum)

# sub = ar2 - ar1  # Subtraction of two array / matrixes
sub = np.subtract(ar2, ar1)  # Subtraction Method by numpy
print(sub)

# mul = ar1 * ar2   # multiplication of two array / matrixes
mul = np.multiply(ar1, ar2)  # multiplication Method by numpy
print(mul)

# div = ar1 / ar2   # division of two array / matrixes
div = np.divide(ar1, ar2)  # division Method by numpy
print(div) 

sq = ar1 ** 2  # square of matrix
print(sq)

cube = ar2 ** 3  # cube of matrix
print(cube)
