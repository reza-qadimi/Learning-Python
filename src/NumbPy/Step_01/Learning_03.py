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

#--------------------------------------------------
#--------------------------------------------------
#Logistic Distribution:
#--------------------------------------------------

#Logistic Distribution is used to describe growth.

#Used extensively in machine learning in logistic regression, neural networks etc.

#It has three parameters:

#loc - mean, where the peak is. Default 0.

#scale - standard deviation, the flatness of distribution. Default 1.

#size - The shape of the returned array.


#Difference Between Logistic and Normal Distribution:
#	Both distributions are near identical, but logistic distribution has more area under the tails
#	meaning it represents more possibility of occurrence of an event further away from mean.
#	For higher value of scale (standard deviation) the normal and logistic distributions are near identical apart from the peak.

#--------------------------------------------------

#from numpy import random

#result = random.logistic(loc=1, scale=2, size=(2,3))

#print(result)

#--------------------------------------------------

#from numpy import random

#import seaborn
#import matplotlib.pyplot as pyplot

#result = random.logistic(loc=1, scale=2, size=(2,3), label="Logistic")

##seaborn.histplot(result)
#seaborn.distplot(result, hist=False)

#pyplot.show()

#--------------------------------------------------
#--------------------------------------------------
#--------------------------------------------------

#--------------------------------------------------
#--------------------------------------------------
#Multinomial Distribution
#--------------------------------------------------

#Multinomial distribution is a generalization of binomial distribution.

#It describes outcomes of multi-nomial scenarios unlike binomial where scenarios must be only one of two. e.g. Blood type of a population, dice roll outcome.

#It has three parameters:

#n - number of possible outcomes (e.g. 6 for dice roll).

#pvals - list of probabilties of outcomes (e.g. [1/6, 1/6, 1/6, 1/6, 1/6, 1/6] for dice roll).

#size - The shape of the returned array.

#--------------------------------------------------

#from numpy import random

#result = random.multinomial(n=6, pvals=[1/6,1/6,1/6,1/6,1/6,1/6])

#print(result)

##Note: Multinomial samples will NOT produce a single value! They will produce one value for each pval.

##Note: As they are generalization of binomial distribution their visual representation and similarity of normal distribution is same as that of multiple binomial distributions.

#--------------------------------------------------
#--------------------------------------------------
#--------------------------------------------------

#--------------------------------------------------
#--------------------------------------------------
#Exponential Distribution:
#--------------------------------------------------

#Exponential distribution is used for describing time till next event e.g. failure/success etc.

#It has two parameters:

#scale - inverse of rate ( see lam in poisson distribution ) defaults to 1.0.

#size - The shape of the returned array.

#--------------------------------------------------

#from numpy import random

#result = random.exponential(scale=2, size=(2,3))

#print(result)

#--------------------------------------------------

#from numpy import random

#import seaborn
#import matplotlib.pyplot as pyplot

#result = random.exponential(size=1000)

##seaborn.histplot(result)
#seaborn.distplot(result, hist=False)

#pyplot.show()

#--------------------------------------------------

#Relation Between Poisson and Exponential Distribution:
# Poisson distribution deals with number of occurences of an event in a time period
# whereas exponential distribution deals with the time between these events.

#--------------------------------------------------
#--------------------------------------------------
#--------------------------------------------------

#--------------------------------------------------
#--------------------------------------------------
#Chi Square Distribution:
#--------------------------------------------------

#Chi Square distribution is used as a basis to verify the hypothesis.

#It has two parameters:
#	df - (degree of freedom).
#	size - The shape of the returned array.

#--------------------------------------------------

#from numpy import random

#result = random.chisquare(df=2, size=(2, 3))

#print(result)

#--------------------------------------------------

#from numpy import random

#import seaborn
#import matplotlib.pyplot as pyplot

#result = random.chisquare(df=1, size=1000)

#seaborn.histplot(result)
#seaborn.distplot(result, hist=False)

#pyplot.show()

#--------------------------------------------------
#--------------------------------------------------
#--------------------------------------------------

#--------------------------------------------------
#--------------------------------------------------
#Rayleigh Distribution:
#--------------------------------------------------

#Rayleigh distribution is used in signal processing.

#It has two parameters:

#scale - (standard deviation) decides how flat the distribution will be (default 1.0).

#size - The shape of the returned array.

#--------------------------------------------------

#from numpy import random

#result = random.rayleigh(scale=2, size=(2, 3))

#print(result)

#--------------------------------------------------

#from numpy import random

#import seaborn
#import matplotlib.pyplot as pyplot

#result = random.rayleigh(size=1000)

#seaborn.histplot(result)
#seaborn.distplot(result, hist=False)

#pyplot.show()

#--------------------------------------------------
#--------------------------------------------------
#--------------------------------------------------

#--------------------------------------------------
#--------------------------------------------------
#Pareto Distribution:
#--------------------------------------------------

#A distribution following Pareto's law i.e. 80-20 distribution (20% factors cause 80% outcome).

#It has two parameter:

#a - shape parameter.

#size - The shape of the returned array.

#--------------------------------------------------

#from numpy import random

#result = random.pareto(a=2, size=(2, 3))

#print(result)

#--------------------------------------------------

#from numpy import random

#import seaborn
#import matplotlib.pyplot as pyplot

#result = random.pareto(a=2, size=1000)

##seaborn.histplot(result)
#seaborn.distplot(result, kde=False)

#pyplot.show()

#--------------------------------------------------
#--------------------------------------------------
#--------------------------------------------------

#--------------------------------------------------
#--------------------------------------------------
#Zipf Distribution:
#--------------------------------------------------

#Zipf distritutions are used to sample data based on zipf's law.

#Zipf's Law: In a collection, the nth common term is 1/n times of the most common term. E.g. the 5th most common word in English occurs nearly 1/5 times as often as the most common word.

#It has two parameters:
#	a - distribution parameter.
#	size - The shape of the returned array.

#--------------------------------------------------

#from numpy import random

#result = random.zipf(a=2, size=(2, 3))

#print(result)

#--------------------------------------------------

#from numpy import random

#import seaborn
#import matplotlib.pyplot as pyplot

#result = random.zipf(a=2, size=1000)

##seaborn.histplot(result[result<10])
#seaborn.distplot(result[result<10], kde=False)

#pyplot.show()

#--------------------------------------------------
#--------------------------------------------------
#--------------------------------------------------