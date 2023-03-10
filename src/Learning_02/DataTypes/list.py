#List items are ordered, changeable, and allow duplicate values.
#List is a collection which is ordered and changeable. Allows duplicate members.
#List items are indexed, the first item has index [0], the second item has index [1] etc.

#Ordered
#Changeable
#Allow Duplicates

#-------------------------
#-------------------------
#-------------------------

#cars = ["BMW", "Benz", "Iran Khodro", "Kia"]

#print(cars)

#carsLength = len(cars)

#print(carsLength)

#carsDataType = type(cars)

#print(carsDataType)

#-------------------------

#differentValueTypes = ["String", 1, True, { 1, 2, 3}, ["A", "B", 3], (4, 5, 6)]

#print(differentValueTypes)

#-------------------------

## using the list() constructor:

#cars = list(("BMW", "Benz", "Iran Khodro", "Benz"));

#print(cars)

#-------------------------
#-------------------------
#-------------------------

#-------------------------
#-------------------------
#-------------------------

#cars = ["BMW", "Benz", "Iran Khodro", "Kia"]


#secondCar = cars[1]

#print(secondCar)

#-------------------------

##Negative indexing means start from the end

##-1 refers to the last item, -2 refers to the second last item etc.


#cars = ["BMW", "Benz", "Iran Khodro", "Kia"]


#lastCar = cars[-1]

#print(lastCar)

#-------------------------

#cars = ["BMW", "Benz", "Iran Khodro", "Kia"]


#selectedCars = cars[1:3]

#print(selectedCars)

#-------------------------

##By leaving out the start value, the range will start at the first item:

#cars = ["BMW", "Benz", "Iran Khodro", "Kia"]


#selectedCars = cars[:3]

#print(selectedCars)

#-------------------------

##By leaving out the end value, the range will go on to the end of the list:

#cars = ["BMW", "Benz", "Iran Khodro", "Kia"]


#selectedCars = cars[3:]

#print(selectedCars)

#-------------------------

##Specify negative indexes if you want to start the search from the end of the list:

#cars = ["BMW", "Benz", "Iran Khodro", "Kia"]


#selectedCars = cars[-3:-1]

#print(selectedCars)

#-------------------------

#cars = ["BMW", "Benz", "Iran Khodro", "Kia"]


#if "Iran Khodro" in cars:
#	print("Why??")

#-------------------------

#cars = ["BMW", "Benz", "Iran Khodro", "Kia"]

#print(cars)

#cars[2] = "Porsche"

#print(cars)

#-------------------------

#cars = ["BMW", "Benz", "Iran Khodro", "Kia"]

#print(cars)

#cars[2:4] = ["Porsche", "Tesla"]

#print(cars)

#-------------------------

#cars = ["BMW", "Benz", "Iran Khodro", "Kia"]

#print(cars)

#cars[2:2] = ["Porsche", "Tesla"]

#print(cars)

#-------------------------

#cars = ["BMW", "Benz", "Iran Khodro", "Kia"]

#print(cars)

#cars[0:4] = ["Tesla"]

#print(cars)

#-------------------------
#-------------------------
#-------------------------

#-------------------------
#-------------------------
#-------------------------

#cars = ["BMW", "Benz", "Iran Khodro", "Kia"]

#print(cars)

#cars.insert(0, "Tesla")

#print(cars)

#-------------------------

#cars = ["BMW", "Benz", "Iran Khodro", "Kia"]

#print(cars)

#cars.append("Tesla")

#print(cars)

#-------------------------

#cars1 = ["BMW", "Benz", "Iran Khodro"]
#cars2 = ["Kia", "Tesla", "Prosche"]

#print(cars1)

#cars1.extend(cars2)

#print(cars1)

#-------------------------

#cars1 = ["BMW", "Benz", "Iran Khodro"]
#cars2 = ("Kia", "Tesla", "Prosche")

#print(cars1)

#cars1.extend(cars2)

#print(cars1)

#-------------------------
#-------------------------
#-------------------------

#-------------------------
#-------------------------
#-------------------------

#cars = ["BMW", "Benz", "Iran Khodro", "Kia"]

#print(cars)

#cars.remove("Iran Khodro")

#print(cars)

#-------------------------

#cars = ["BMW", "Benz", "Iran Khodro", "Kia"]

#print(cars)

#cars.remove("iran khodro") #Runtime Error: list.remove(x): x not in list

#print(cars)

#-------------------------

#cars = ["BMW", "Benz", "Iran Khodro", "Kia", "Iran Khodro"]

#print(cars)

#cars.remove("Iran Khodro")

#print(cars)

#-------------------------

#cars = ["BMW", "Benz", "Iran Khodro", "Kia"]

#print(cars)

#cars.pop()

#print(cars)

#-------------------------

#cars = ["BMW", "Benz", "Iran Khodro", "Kia"]

#print(cars)

#cars.pop(0)

#print(cars)

#-------------------------

#cars = ["BMW", "Benz", "Iran Khodro", "Kia"]

#print(cars)

#cars.pop(2)

#print(cars)

#-------------------------

#cars = ["BMW", "Benz", "Iran Khodro", "Kia"]

#print(cars)

#del cars

#print(cars) # Runtime Error: name 'cars' is not defined

#-------------------------

#cars = ["BMW", "Benz", "Iran Khodro", "Kia"]

#print(cars)

#del cars[0]

#print(cars)

#-------------------------

#cars = ["BMW", "Benz", "Iran Khodro", "Kia"]

#print(cars)

#cars.clear()

#print(cars)

#-------------------------
#-------------------------
#-------------------------
