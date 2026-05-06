                         #Practice Questions of NumPy

#Create a NumPy array from a list of integers from 10 to 20.
import numpy as np 
list=[10,11,12,13,14,15,16,17,18,19,20]
arr=np.array(list) #Numpy array
print(arr)

#Create a NumPy array from a list of floating-point numbers (1.5, 2.5, 3.5, etc)
import numpy as np
list=[1.5,2.4,3.6,4.5,5.2,6.7]
arr=np.array(list)
print(arr) 

#Perform element-wise addition of two arrays: [5, 10, 15] and [1, 2, 3].
import numpy as np
arr1=np.array([5,10,15])
arr2=np.array([1,2,3])
result=(arr1+arr2)
print(result)

#Perform element-wise subtraction between two arrays: [100, 200, 300] and [50, 100, 150].
import numpy as np
arr1=np.array([100,200,300])
arr2=np.array([50,100,150])
result=(arr1-arr2)
print(result)

#Create a 2D array (matrix) of shape (3, 3) and initialize it with values from 1 to 9.
import numpy as np
arr_2d=np.array([[1,2,3],
                 [4,5,6],
                 [7,8,9]])
print(arr_2d)

#Use slicing to extract elements from index 2 to 5 from the array [10, 20, 30, 40, 50, 60, 70].
import numpy as np
arr=np.array([10, 20, 30, 40, 50, 60, 70])
print(arr[2:5])

#Find the sum of all elements in the array [1, 2, 3, 4, 5, 6].
import numpy as np
arr=np.array([1,2,3,4,5,6])
print(np.sum(arr))

#Calculate the mean of the array [10, 20, 30, 40, 50].
import numpy as np
arr=np.array([10, 20, 30, 40, 50])
print(np.mean(arr))

#Create an array of 10 zeros using NumPy.
import numpy as np
arr=np.zeros(10)
print(arr)

#Access the first element and the last element from the array [10, 20, 30, 40, 50] using indexing.
import numpy as np
arr=np.array([10, 20, 30, 40, 50])
print(arr[0])
print(arr[4])

#Create a 1D array of size 5 filled with the value 7.
import numpy as np
arr_1d=np.full(5, 7) 
print(arr_1d)

#Reshape a 1D array of size 6 to a 2D array with shape (2, 3).
import numpy as np
arr_1d=np.array([1,2,3,4,5,6])
arr_2d=arr_1d.reshape(2,3)
print(arr_2d)

#Concatenate two arrays [1, 2, 3] and [4, 5, 6] to form a single array.
import numpy as np
arr1=np.array([1,2,3])
arr2=np.array([4,5,6])
result=np.concatenate((arr1,arr2))
print(result)

#Split an array [10, 20, 30, 40, 50, 60] into two equal halves.
import numpy as np
arr1=np.array([10,20,30,40,50,60])
result=np.split(arr1,2)
print(result)

#Create an array of shape (4, 4) and initialize it with random integers between 1 and 50.
import numpy as np
random_array = np.random.randint(0, 50, size=(4, 4))
print(random_array)

#Flatten a 2D array [[1, 2], [3, 4], [5, 6]] into a 1D array.
import numpy as np
arr_2d=np.array([[1, 2], [3, 4], [5, 6]])
arr_1d=arr_2d.flatten()
print(arr_1d)

#Create a 3x3 identity matrix.
import numpy as np
arr=np.eye(3,3)
print(arr)

#Stack two arrays [1, 2] and [3, 4] vertically.
import numpy as np
arr1=np.array([1,2])
arr2=np.array([3,4])
result=np.vstack((arr1,arr2))
print(result)

#Stack two arrays [1, 2] and [3, 4] horizontally.
import numpy as np
arr1=np.array([1,2])
arr2=np.array([3,4])
result=np.hstack((arr1,arr2))
print(result)

#Create a 3x3 matrix of ones and then subtract 2 from each element.
import numpy as np
matrix = np.ones((3, 3)) 
result = matrix - 2      
print(result)

#Find the median of the array [12, 14, 11, 18, 15].
import numpy as np
arr=np.array([12, 14, 11, 18, 15])
print(np.median(arr))

#Find the standard deviation of the array [5, 10, 15, 20, 25].
import numpy as np
arr=np.array([5, 10, 15, 20, 25])
print(np.std(arr))

#Calculate the variance of the array [7, 9, 11, 13, 15].
import numpy as np
arr=np.array([7, 9, 11, 13, 15])
print(np.var(arr))

#Create an array [1, 2, 3, 4, 5] and find the cumulative sum.
import numpy as np
arr=np.array([1, 2, 3, 4, 5])
print(np.cumsum(arr))

#Find the minimum and maximum values of the array [20, 30, 10, 40, 50].
import numpy as np
arr=np.array([20, 30, 10, 40, 50])
print(np.min(arr))
print(np.max(arr))

#Calculate the sum of all elements in the array [1, 1, 1, 1, 1] using np.sum().
import numpy as np
arr=np.array([1, 1, 1, 1, 1])
print(np.sum(arr))

#Create an array of random numbers of size 10 and calculate the mean.
import numpy as np
arr=np.array([1,2,3,4,5,6,7,8,9,10])
print(np.mean(arr))

import numpy as np
arr = np.random.randint(1,100,10)
print(np.mean(arr))  

#Find the percentile of the number 20 in the array [10, 20, 30, 40, 50] using np.percentile().
import numpy as np
arr=np.array([10, 20, 30, 40, 50])
print(np.percentile(arr,20))

#Compute the correlation coefficient between the arrays [1, 2, 3, 4] and [10, 20, 30, 40].
import numpy as np
arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([10, 20, 30, 40])
result= np.corrcoef(arr1, arr2)
print(result)

#Create a 5x5 matrix with random values and find the sum of the diagonal elements.
import numpy as np
arr = np.random.randint(1, 25, (5, 5)) 
print(arr)
diagonal_sum = np.trace(arr)
print("Sum of diagonal elements:", diagonal_sum)

#Compute the dot product of two arrays: [1, 2, 3] and [4, 5, 6].
import numpy as np 
arr1=np.array([1,2,3])
arr2=np.array([4,5,6])
print(np.dot(arr1,arr2))

#Perform matrix multiplication between two 2D arrays: [[1, 2], [3, 4]] and [[5, 6], [7, 8]].
import numpy as np 
arr1=np.array([[1, 2], 
               [3, 4]])
arr2=np.array([[5, 6], 
               [7, 8]])
print(np.dot(arr1,arr2))
print((arr1@arr2))   #Another Method 

#Find the determinant of a 2x2 matrix [[1, 2], [3, 4]].
import numpy as np 
matrix=np.array([[1, 2], 
               [3, 4]])
print(np.linalg.det(matrix))

#Compute the inverse of a matrix [[1, 2], [3, 4]].
import numpy as np 
matrix=np.array([[1, 2], 
               [3, 4]])
print(np.linalg.inv(matrix))

#Create a 3x3 matrix and calculate its rank.
import numpy as np
matrix=([[1,2,3],
         [4,5,6],
         [7,8,9]])
print(np.linalg.matrix_rank(matrix))