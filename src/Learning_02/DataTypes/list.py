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

#cars = ["BMW", "Benz", "Iran Khodro", "Kia"]

#for item in cars:
#	print(item)

#-------------------------

#cars = ["BMW", "Benz", "Iran Khodro", "Kia"]

#carsLength = len(cars);

#for index in range(carsLength):

#	currentItem = cars[index];

#	print(currentItem)

#-------------------------

#cars = ["BMW", "Benz", "Iran Khodro", "Kia"]

#for index, item in enumerate(cars):

#	message = f"{index + 1}. {item}"

#	print(message)

#-------------------------

#index = 0

#cars = ["BMW", "Benz", "Iran Khodro", "Kia"]

#while index < len(cars):

#	currentItem = cars[index]

#	message = f"{index + 1}. {currentItem}"

#	print(message)

#	index += 1
#	#index = index + 1

#-------------------------

#index = 0

#cars = ["BMW", "Benz", "Iran Khodro", "Kia"]

#while index < cars.__len__():

#	currentItem = cars[index]

#	message = f"{index + 1}. {currentItem}"

#	print(message)

#	index += 1
#	#index = index + 1

#-------------------------

#index = 0

#cars = ["BMW", "Benz", "Iran Khodro", "Kia"]

#carsLength = len(cars);

#while index < carsLength:

#	currentItem = cars[index]

#	message = f"{index + 1}. {currentItem}"

#	print(message)

#	index += 1
#	#index = index + 1

#-------------------------

#cars = ["BMW", "Benz", "Iran Khodro", "Kia"]

#[print(item) for item in cars]

#-------------------------

#cars = ["BMW", "Benz", "Iran Khodro", "Kia"]

#[print(f"{index + 1}. {item}") for index, item in enumerate(cars)]

#-------------------------
#-------------------------
#-------------------------

#-------------------------
#-------------------------
#-------------------------

#cars = ["BMW", "Benz", "Iran Khodro", "Kia"]

#selectedCars = []

#for item in cars:
#	if "B" in item:
#		selectedCars.append(item)

#print(selectedCars)

#-------------------------

##newlist = [expression for item in iterable if condition == True]

#cars = ["BMW", "Benz", "Iran Khodro", "Kia"]

#selectedCars = [item for item in cars if "B" in item]

#print(selectedCars)

#-------------------------

#cars = ["BMW", "Benz", "Iran Khodro", "Kia"]

#selectedCars = [item.upper() if "B" in item else item.lower() for item in cars]

#print(selectedCars)

#-------------------------
#-------------------------
#-------------------------


#-------------------------
#-------------------------
#-------------------------

#numbers = [10, 20, 3, 15, 1616]

#print(numbers)

#numbers.sort()

#print(numbers)

#-------------------------

#numbers = [10, 20, 3, 15, 1616]

#print(numbers)

#numbers.sort(reverse = True)

#print(numbers)

#-------------------------

#cars = ["BMW", "Benz", "Iran Khodro", "Kia"]

#print(cars)

#cars.sort()

#print(cars)

#-------------------------

#cars = ["BMW", "Benz", "Iran Khodro", "Kia"]

#print(cars)

##case-insensitive
#cars.sort(key = str.lower)

#print(cars)

#-------------------------

#cars = ["BMW", "Benz", "Iran Khodro", "Kia"]

#print(cars)

#cars.reverse()

#print(cars)

#-------------------------

#def customizeSort(value):
#	result = abs(value - 50)

#	return result

#numbers = [10, 20.1, 30, 40, 50, 60, 70, 80, 90, 100]

#print(numbers)

#numbers.sort(key = customizeSort)

#print(numbers)

#-------------------------
#-------------------------
#-------------------------

#-------------------------
#-------------------------
#-------------------------

#cars1 = ["BMW", "Benz", "Iran Khodro", "Kia"]

#print(cars1)

#cars2 =  cars1.copy()

#print(cars2)

#-------------------------

#cars1 = ["BMW", "Benz", "Iran Khodro", "Kia"]

#print(cars1)

#cars2 =  list(cars1)

#print(cars2)

#-------------------------
#-------------------------
#-------------------------

#-------------------------
#-------------------------
#-------------------------

#cars = ["BMW", "Benz", "Iran Khodro", "Kia"]
#numbers = [10, 20.1, 30, 40, 50, 60, 70, 80, 90, 100]

#mixedList = cars + numbers

#print(mixedList)

#-------------------------

#cars = ["BMW", "Benz", "Iran Khodro", "Kia"]
#numbers = [10, 20.1, 30, 40, 50, 60, 70, 80, 90, 100]

#mixedList = cars.extend(numbers)

#print(mixedList)

#-------------------------

#cars = ["BMW", "Benz", "Iran Khodro", "Kia"]
#numbers = [10, 20.1, 30, 40, 50, 60, 70, 80, 90, 100]

#mixedList = cars.extend(numbers)

#print(mixedList)

#-------------------------
#-------------------------
#-------------------------


#-------------------------
#Python - List Methods()
#-------------------------
#https://www.w3schools.com/python/python_lists_methods.asp
#-------------------------
