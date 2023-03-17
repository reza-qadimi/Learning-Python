#--------------------------------------------------
#--------------------------------------------------
#--------------------------------------------------
#Normal (Gaussian) Distribution
#--------------------------------------------------
#--------------------------------------------------
#--------------------------------------------------

#The Normal Distribution is one of the most important distributions.

#It is also called the Gaussian Distribution after the German mathematician Carl Friedrich Gauss.

#It fits the probability distribution of many events, eg. IQ Scores, Heartbeat etc.

#Use the random.normal() method to get a Normal Data Distribution.

#It has three parameters:

#loc - (Mean) where the peak of the bell exists.

#scale - (Standard Deviation) how flat the graph distribution should be.

#size - The shape of the returned array.

#--------------------------------------------------

#from numpy import random

#result = random.normal(size=(2, 5))

#print(result)

#--------------------------------------------------

#from numpy import random

##Generate a random normal distribution of:
##	size 2x5 with mean at 1 and standard deviation of 2:
#result = random.normal(loc=1, scale=2, size=(2, 5))

#print(result)

#--------------------------------------------------

#from numpy import random

#import seaborn
#import matplotlib.pyplot as pyplot

#result = random.normal(size=(1000))

##seaborn.histplot(result)
#seaborn.distplot(result, hist=False)

#pyplot.show()

#--------------------------------------------------

#from numpy import random

#import seaborn
#import matplotlib.pyplot as pyplot

##Generate a random normal distribution of:
##	size 2x5 with mean at 1 and standard deviation of 2:
#result = random.normal(loc=1, scale=2, size=(2, 5))

##seaborn.histplot(result)
#seaborn.distplot(result, hist=False)

#pyplot.show()

#--------------------------------------------------
#--------------------------------------------------
#--------------------------------------------------

#--------------------------------------------------
#--------------------------------------------------
#--------------------------------------------------
