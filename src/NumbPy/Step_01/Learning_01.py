#--------------------------------------------------

#import numpy
##import numpy as numpy

#myArray = numpy.array([10, 20, 3, 15])

#print(myArray)

#myArrayType = type(myArray)

#print(myArrayType)

#myArrayShape = myArray.shape

#print(myArrayShape)

#--------------------------------------------------

#import numpy

#numpyVersion = numpy.__version__

#print(numpyVersion)

#--------------------------------------------------

##Dimensions in Arrays
##A dimension in arrays is one level of array depth (nested arrays).

#import numpy

##Runtime Error:
## setting an array element with a sequence.
## The requested array has an inhomogeneous shape after 1 dimensions. The detected shape was (4,) + inhomogeneous part.
##myArray = numpy.array([[10, 10], [20, 20], [3, 3], 15])

#myArray = numpy.array([[10, 10], [20, 20], [3, 3], [15, 15]])

#print(myArray)

#myArrayDimension = myArray.ndim

#print(myArrayDimension)

#--------------------------------------------------

##An array can have any number of dimensions.

##When the array is created, you can define the number of dimensions by using the ndmin argument.

#import numpy

#myArray = numpy.array([10, 20, 3, 15], ndmin = 5)

#print(myArray)

#myArrayDimension = myArray.ndim

#print(myArrayDimension)

#--------------------------------------------------

#import numpy

#myArray = numpy.array([[10, 20], [3, 15], [1000, 60], [16, 0]])

#print(myArray[0])
#print(myArray[0, 1])	#Second Item
#print(myArray[0, -1])	#Last Item

#--------------------------------------------------

##Slicing arrays
##Slicing in python means taking elements from one given index to another given index.

##We pass slice instead of index like this: [start:end].

##We can also define the step, like this: [start:end:step].

##If we don't pass start its considered 0

##If we don't pass end its considered length of array in that dimension

##If we don't pass step its considered 1

#import numpy

#myArray = numpy.array([[10, 20], [3, 15], [1000, 60], [16, 0]])

#print(myArray[0 : 3])
#print(myArray[0 : -1])
#print(myArray[-4 : -1])

#--------------------------------------------------

#import numpy

#myArray = numpy.array([10, 20, 3, 15])

#selectedItems1 = myArray[0:4:2]
#selectedItems2 = myArray[0::2]
#selectedItems3 = myArray[::2]

#print(selectedItems1)
#print(selectedItems2)
#print(selectedItems3)

#--------------------------------------------------

#import numpy

## String
## Size: 2
#myArray = numpy.array([10, 20, 3, 153], dtype="S2")

#print(myArray)

#myArrayDataType = myArray.dtype

#print(myArrayDataType)

##NOTE: If a type is given in which elements can't be casted then NumPy will raise a ValueError.

#--------------------------------------------------

##The best way to change the data type of an existing array, is to make a copy of the array with the astype() method.

#import numpy

#myArray = numpy.array([10.1, 20.2, 3.3, 15.15])

#print(myArray)

#myArrayAsUnassignInteger = myArray.astype(int)

#print(myArrayAsUnassignInteger)

#--------------------------------------------------

##The Difference Between Copy and View:
##	The main difference between a copy and a view of an array is that the copy is a new array, and the view is just a view of the original array.
##	The copy owns the data and any changes made to the copy will not affect original array, and any changes made to the original array will not affect the copy.
##	The view does not own the data and any changes made to the view will affect the original array, and any changes made to the original array will affect the view.

#import numpy

#myArray = numpy.array([10.1, 20.2, 3.3, 15.15])
#copyOfMyArray = myArray.copy()

#copyOfMyArray[0] = 0.1

#print(myArray)
#print(copyOfMyArray)
#print(copyOfMyArray.base) #Check if Array Owns its Data


#import numpy

#myArray = numpy.array([10.1, 20.2, 3.3, 15.15])
#viewOfMyArray = myArray.view()

#viewOfMyArray[0] = 0.1

#print(myArray)
#print(viewOfMyArray)
#print(viewOfMyArray.base) #Check if Array Owns its Data

#--------------------------------------------------

##Reshaping arrays:
##	Reshaping means changing the shape of an array.

##	The shape of an array is the number of elements in each dimension.

##	By reshaping we can add or remove dimensions or change number of elements in each dimension.

#import numpy

#my1DArray = numpy.array([10, 20, 3, 15, 1000, 60])

#my2DArray = my1DArray.reshape(2, 3)
##my2DArray = my1DArray.reshape(2, 2) #Runtime Error: cannot reshape array of size 6 into shape (2,2)


#print("1D Array:", my1DArray)
#print("2D Array:", my2DArray)

#--------------------------------------------------

#import numpy

#my2DArray = numpy.array([[10, 20], [3, 15], [1000, 60]])

#my1DArray = my2DArray.reshape(-1)

#print("2D Array:", my2DArray)
#print("1D Array:", my1DArray)
#print("1D Array:", my1DArray.base)

#--------------------------------------------------

#import numpy

#myArray = numpy.array([[10, 20], [3, 15], [1000, 60]])

#for items in myArray:
#	for item in items:
#		print(item)

#--------------------------------------------------

#import numpy

#myArray = numpy.array([[10, 20, 3], [3, 15, 6], [1000, 60, 12]])

##Iterating on Each Scalar Element
#for item in numpy.nditer(myArray):
#	print(item)

#--------------------------------------------------

#We can use op_dtypes argument and pass it the expected datatype to change the datatype of elements while iterating.
#NumPy does not change the data type of the element in-place (where the element is in array) so it needs some other space to perform this action, that extra space is called buffer, and in order to enable it in nditer() we pass flags=['buffered'].

#import numpy

#myArray = numpy.array([[10, 20, 3], [3, 15, 6], [1000, 60, 12]])

#for item in numpy.nditer(myArray, flags=['buffered'], op_dtypes=['S']):
#	print(item)

#--------------------------------------------------

#import numpy

#myArray = numpy.array([[10, 20, 3], [3, 15, 6], [1000, 60, 12]])

#for item in numpy.nditer(myArray[:,::2]):
#	print(item)

#--------------------------------------------------

##Enumerated Iteration Using ndenumerate()
##Enumeration means mentioning sequence number of somethings one by one.
##Sometimes we require corresponding index of the element while iterating, the ndenumerate() method can be used for those usecases.

#import numpy

#myArray = numpy.array([[10, 20, 3], [3, 15, 6], [1000, 60, 12]])

#for index, item in numpy.ndenumerate(myArray):
#	print(f"{index}:", item)

#--------------------------------------------------

#import numpy

#myArray1 = numpy.array([[10, 20], [3, 15], [1000, 60]])
#myArray2 = numpy.array([[20, 30], [4, 25], [2000, 70]])

#result = numpy.concatenate((myArray1, myArray2))

#print(result)

#--------------------------------------------------

#import numpy

#myArray1 = numpy.array([[10, 20], [3, 15], [1000, 60]])
#myArray2 = numpy.array([[20, 30], [4, 25], [2000, 70]])

#result = numpy.concatenate((myArray1, myArray2), axis=1)

#print(result)

#--------------------------------------------------

##Stacking is same as concatenation, the only difference is that stacking is done along a new axis.

#import numpy

#myArray1 = numpy.array([[10, 20], [3, 15], [1000, 60]])
#myArray2 = numpy.array([[20, 30], [4, 25], [2000, 70]])

#result = numpy.stack((myArray1, myArray2), axis=1)

#print(result)

#--------------------------------------------------

##Stacking is same as concatenation, the only difference is that stacking is done along a new axis.

#import numpy

#myArray1 = numpy.array([[10, 20], [3, 15], [1000, 60]])
#myArray2 = numpy.array([[20, 30], [4, 25], [2000, 70]])

#result = numpy.stack((myArray1, myArray2))

#print(result)

#--------------------------------------------------

##NumPy provides a helper function: hstack() to stack along rows.

#import numpy

#myArray1 = numpy.array([[10, 20], [3, 15], [1000, 60]])
#myArray2 = numpy.array([[20, 30], [4, 25], [2000, 70]])

#result = numpy.hstack((myArray1, myArray2))

#print(result)

#--------------------------------------------------

##NumPy provides a helper function: vstack()  to stack along columns.

#import numpy

#myArray1 = numpy.array([[10, 20], [3, 15], [1000, 60]])
#myArray2 = numpy.array([[20, 30], [4, 25], [2000, 70]])

#result = numpy.vstack((myArray1, myArray2))

#print(result)

#--------------------------------------------------

##NumPy provides a helper function: dstack() to stack along height, which is the same as depth.

#import numpy

#myArray1 = numpy.array([[10, 20], [3, 15], [1000, 60]])
#myArray2 = numpy.array([[20, 30], [4, 25], [2000, 70]])

#result = numpy.dstack((myArray1, myArray2))

#print(result)

#--------------------------------------------------
##Splitting NumPy Arrays:
##	Splitting is reverse operation of Joining.
##	Joining merges multiple arrays into one and Splitting breaks one array into multiple.
##	We use array_split() for splitting arrays, we pass it the array we want to split and the number of splits.

#import numpy

#myArray = numpy.array([10, 20, 3, 15, 1000, 60, 16])

#result = numpy.array_split(myArray, 5)

#print(result)

#--------------------------------------------------

#import numpy

#myArray = numpy.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])

#result = numpy.array_split(myArray, 2, axis=1)

#print(result)

#--------------------------------------------------

#import numpy

#myArray = numpy.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])

#result = numpy.array_split(myArray, 2, axis=0)

#print(result)

#--------------------------------------------------

#import numpy

#myArray = numpy.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])

#result = numpy.array_split(myArray, 3, axis=1)

#print(result)

#--------------------------------------------------

#import numpy

#myArray = numpy.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])

#result = numpy.array_split(myArray, 3, axis=0)

#print(result)

#--------------------------------------------------

#import numpy

#myArray = numpy.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])

#result = numpy.hsplit(myArray, 3)

#print(result)

#--------------------------------------------------

#import numpy

#myArray = numpy.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])

#result = numpy.vsplit(myArray, 3)

#print(result)

#--------------------------------------------------

#import numpy

#myArray =  numpy.array([10, 20, 3, 15, 1000, 60, 16])

#result = numpy.where(myArray != 1000)

#print(result)

#--------------------------------------------------

##Search Sorted:
##	There is a method called searchsorted() which performs a binary search in the array, and returns the index where the specified value would be inserted to maintain the search order.
##	The searchsorted() method is assumed to be used on sorted arrays.

#import numpy

#myArray =  numpy.array([3, 10, 20, 30, 40, 60])

#result = numpy.searchsorted(myArray, 4)

#print(result)

#--------------------------------------------------

#import numpy

#myArray =  numpy.array([3, 10, 20, 30, 40, 60])

##Find the indexes where the values [4, 2, 8, 19, 99] should be inserted
#result = numpy.searchsorted(myArray, [4, 2, 8, 19, 99])

#print(result)

#--------------------------------------------------

#import numpy

#myArray = numpy.array([10, 20, 3, 15, 1000, 60, 16])

#print(numpy.sort(myArray))

#--------------------------------------------------

#import numpy

#myArray = numpy.array([10, 20, 3, 15, 1000, 60, 16])

#for item in myArray:
#	if item % 2 == 0:
#		print(item)


#myFilter = myArray % 2 == 0

#print(myArray[myFilter])

#--------------------------------------------------
