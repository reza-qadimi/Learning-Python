#--------------------------------------------------
#--------------------------------------------------
#--------------------------------------------------

#from numpy import random

#randomInteger = random.randint(100)
##randomInteger = random.randint(low = 1, high = 100)
##randomInteger = random.randint() #Runtime Error: randint() takes at least 1 positional argument (0 given)

#print(randomInteger)

#--------------------------------------------------

#from numpy import random

#randomFloat = random.rand()

#print(randomFloat)

#--------------------------------------------------

##Generate Random Array

#from numpy import random

#randomArray = random.randint(low=1, high=100, size=(5))
##randomArray = random.randint(low=1, high=100, size=(2, 5)) #2D array with 5 Item

#print(randomArray)

#--------------------------------------------------

#from numpy import random

#randomArray = random.rand(5)
##randomArray = random.rand(2, 5) #2D array with 5 item

#print(randomArray)

#--------------------------------------------------

##Generate Random Number From Array:
##	The choice() method allows you to generate a random value based on an array of values.
##	The choice() method takes an array as a parameter and randomly returns one of the values.

#from numpy import random

#randomItem = random.choice([10, 20, 3, 15])
##randomItem = random.choice([10, 20, 3, 15], size=(2,5)) #2D array with 5 Item

#print(randomItem)

#--------------------------------------------------
#--------------------------------------------------
#--------------------------------------------------

#--------------------------------------------------
#--------------------------------------------------
#--------------------------------------------------

##What is Data Distribution?
##Data Distribution is a list of all possible values, and how often each value occurs.

##Random Distribution
##A random distribution is a set of random numbers that follow a certain probability density function.

##Probability Density Function:
##A function that describes a continuous probability. i.e. probability of all values in an array.

#from numpy import random

##Note: The sum of all probability numbers should be 1.
#randomArray = random.choice([10, 20, 3, 15, 1000, 60, 16],p=[1, 0, 0, 0, 0, 0, 0], size=(2, 4))
##randomArray = random.choice([10, 20, 3, 15, 1000, 60, 16],p=[0.3, 0.2, 0.1, 0.1, 0.1, 0.1, 0.1], size=(2, 4))

#print(randomArray)

#--------------------------------------------------
#--------------------------------------------------
#--------------------------------------------------
##Random Permutations of Elements
##	A permutation refers to an arrangement of elements. e.g. [3, 2, 1] is a permutation of [1, 2, 3] and vice-versa.
##	The NumPy Random module provides two methods for this: shuffle() and permutation().
#--------------------------------------------------

##Shuffling Arrays:
##The shuffle() method makes changes to the original array.
##Shuffle means changing arrangement of elements in-place. i.e. in the array itself.

#import numpy
#from numpy import random

#myArray = numpy.array([10, 20, 3, 15])

#random.shuffle(myArray)

#print(myArray)

#--------------------------------------------------

##Generating Permutation of Arrays
##The permutation() method returns a re-arranged array (and leaves the original array un-changed).

#import numpy
#from numpy import random

#myArray = numpy.array([10, 20, 3, 15])

#print("Array:", myArray)

#random.permutation(myArray)
#print("After Permutation:", myArray)

#myArrayPermutation = random.permutation(myArray)
#print("Permutation Output:", myArrayPermutation)

#--------------------------------------------------
#--------------------------------------------------
#--------------------------------------------------
