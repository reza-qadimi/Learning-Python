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
#Binomial Distribution:
#--------------------------------------------------

#Binomial Distribution is a Discrete Distribution.

#It describes the outcome of binary scenarios, e.g. toss of a coin, it will either be head or tails.

#It has three parameters:

#n - number of trials.

#p - probability of occurence of each trial (e.g. for toss of a coin 0.5 each).

#size - The shape of the returned array.

#Difference Between Normal and Binomial Distribution:
#The main difference is that normal distribution is continous whereas binomial is discrete, but if there are enough data points it will be quite similar to normal distribution with certain loc and scale.

#--------------------------------------------------

#from numpy import random

#result = random.binomial(n=10, p=0.5, size=10)

#print(result)

#--------------------------------------------------

#from numpy import random

#import seaborn
#import matplotlib.pyplot as pyplot

#result = random.binomial(n=10, p=0.5, size=1000)

#seaborn.histplot(result)
##seaborn.distplot(result, hist=True, kde=False)

#pyplot.show()

#--------------------------------------------------
#--------------------------------------------------
#--------------------------------------------------

#--------------------------------------------------
#--------------------------------------------------
#Poisson Distribution
#--------------------------------------------------

#Poisson Distribution is a Discrete Distribution.

#It estimates how many times an event can happen in a specified time.
#e.g. If someone eats twice a day what is the probability he will eat thrice?

#It has two parameters:

#lam - rate or known number of occurrences e.g. 2 for above problem.

#size - The shape of the returned array.


#Difference Between Normal and Poisson Distribution:
#	Normal distribution is continuous whereas poisson is discrete.
#	But we can see that similar to binomial for a large enough poisson distribution it will become similar to normal distribution with certain std dev and mean.

#Difference Between Binomial and Poisson Distribution:
#	Binomial distribution only has two possible outcomes, whereas poisson distribution can have unlimited possible outcomes.
#	But for very large n and near-zero p binomial distribution is near identical to poisson distribution such that n * p is nearly equal to lam.
#--------------------------------------------------

#from numpy import random

#result = random.poisson(lam=2, size=10)

#print(result)

#--------------------------------------------------

#from numpy import random

#import seaborn
#import matplotlib.pyplot as pyplot

#result = random.poisson(lam=2, size=10)

#seaborn.histplot(result, kde=False)
##seaborn.distplot(result, kde=False)

#pyplot.show()

#--------------------------------------------------
#--------------------------------------------------
#--------------------------------------------------

#--------------------------------------------------
#--------------------------------------------------
#Uniform Distribution:
#--------------------------------------------------

#Used to describe probability where every event has equal chances of occuring.

#E.g. Generation of random numbers.

#It has three parameters:

#a - lower bound - default 0 .0.

#b - upper bound - default 1.0.

#size - The shape of the returned array.

#--------------------------------------------------

#from numpy import random

#result = random.uniform(size=(2,3))

#print(result)

#--------------------------------------------------

#from numpy import random

#import seaborn
#import matplotlib.pyplot as pyplot

#result = random.uniform(size=1000)

##seaborn.histplot(result)
#seaborn.distplot(result, hist=False)

#pyplot.show()

#--------------------------------------------------
#--------------------------------------------------
#--------------------------------------------------
