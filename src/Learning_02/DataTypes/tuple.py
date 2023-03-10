#Tuples are used to store multiple items in a single variable.

#Tuple items are ordered, unchangeable, and allow duplicate values.

#A tuple is a collection which is ordered and unchangeable (Immutable).

#Ordered
#When we say that tuples are ordered, it means that the items have a defined order, and that order will not change.

#Unchangeable
#Tuples are unchangeable, meaning that we cannot change, add or remove items after the tuple has been created.

#Allow Duplicates
#Since tuples are indexed, they can have items with the same value:

#-------------------------
#-------------------------
#-------------------------

#cars = ("BMW", "Benz", "Iran Khodro", "Kia")

#print(cars)

#variableType = type(cars)

#print(variableType)

#-------------------------

#cars = ("BMW", "Benz", "Iran Khodro", "Kia")

#print(cars)

#tupleLength = len(cars)

#print(tupleLength)

#-------------------------

#cars = ("BMW (1)",)

#print(cars)

#variableType = type(cars)

#print(variableType)


#cars = ("BMW (2)")

#print(cars)

#variableType = type(cars)

#print(variableType)

#-------------------------

#cars = ("BMW", "Benz", "Iran Khodro", "Kia")

#print(cars)

#bmwCount = cars.count("BMW")

#print(bmwCount)

#bmwIndex = cars.index("BMW")

#print(bmwIndex)

#-------------------------

##A tuple can contain different data types

#items = ("hello, world!", 26, True, 40, False)

#print(items)

#-------------------------

#cars = tuple(("BMW", "Benz", "Iran Khodro", "Kia"))

#print(cars)

#-------------------------

#cars = tuple(("BMW", "Benz", "Iran Khodro", "Kia"))

#cars[0] = "Another BMW" #Runtime Error: 'tuple' object does not support item assignment

#print(cars)

#-------------------------
#-------------------------
#-------------------------

#-------------------------
#-------------------------
#-------------------------

#cars = tuple(("BMW", "Benz", "Iran Khodro", "Kia"))

#print(cars)

#carsList = list(cars)

#carsList[0] = "Another BMW"

#cars = tuple(carsList)

#print(cars)

#-------------------------

#cars = tuple(("BMW", "Benz", "Iran Khodro", "Kia"))

#print(cars)

#carsList = list(cars)

#carsList.append("Another BMW")

#cars = tuple(carsList)

#print(cars)

#-------------------------

#cars = tuple(("BMW", "Benz", "Iran Khodro", "Kia"))

#print(cars)

#anotherCarsTuple = ("Another BMW", "Tesla")

#cars += anotherCarsTuple

#print(cars)

#-------------------------

#cars = tuple(("BMW", "Benz", "Iran Khodro", "Kia"))

#print(cars)

#carsList = list(cars)

#carsList.remove("BMW")

#cars = tuple(carsList)

#print(cars)

#-------------------------

#cars = tuple(("BMW", "Benz", "Iran Khodro", "Kia"))

#print(cars)

#del cars

#print(cars) #Runtime Error: name 'cars' is not defined

#-------------------------
#-------------------------
#-------------------------

#-------------------------
#-------------------------
#-------------------------

##packing:

#cars = ("BMW", "Benz", "Iran Khodro", "Kia")

#-------------------------

##unpacking:

#cars = ("BMW", "Benz", "Iran Khodro", "Kia")

#(BMW, Benz, googooli, Kia) = cars

#print(BMW)
#print(googooli)

#-------------------------

#cars = ("BMW", "Benz", "Iran Khodro", "Kia")

#(BMW, *googoolies, Kia) = cars

#print(BMW)
#print(googoolies)
#print(Kia)

#-------------------------
#-------------------------
#-------------------------

#-------------------------
#-------------------------
#-------------------------

#numbers = (10, 20, 3, 15)
#cars = ("BMW", "Benz", "Iran Khodro", "Kia")

#result = cars + numbers

#print(result)

#-------------------------

#numbers = (10, 20, 3, 15)
#cars = ("BMW", "Benz", "Iran Khodro", "Kia")

#result = cars * 2

#print(result)

#-------------------------
#-------------------------
#-------------------------
