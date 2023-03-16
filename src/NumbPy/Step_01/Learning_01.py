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
