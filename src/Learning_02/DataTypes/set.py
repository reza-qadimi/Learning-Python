#Sets are used to store multiple items in a single variable.

#A set is a collection which is unordered, unchangeable*, and unindexed.

#Unordered
#Unordered means that the items in a set do not have a defined order.

#Set items can appear in a different order every time you use them, and cannot be referred to by index or key.

#Unchangeable
#Set items are unchangeable, meaning that we cannot change the items after the set has been created.

#Once a set is created, you cannot change its items, but you can remove items and add new items.

#Duplicates Not Allowed
#Sets cannot have two items with the same value.

#Set items can be of any data type

#True and 1 is considered the same value
#False and 0 is considered the same value

#-------------------------
#-------------------------
#-------------------------

#cars = {"BMW", "Benz", "Iran Khodro", "Kia"}

#print(cars)

#carsLength = len(cars)

#print(carsLength)

#carsDataType = type(cars)

#print(carsDataType)


#-------------------------

#differentValueTypes = {"BMW", "Benz", "Iran Khodro", "Kia", "Kia", "KIA", 1, True, False, 0}

#print(differentValueTypes)

#-------------------------

## using the set() constructor:

#cars = set(("BMW", "Benz", "Iran Khodro", "Benz"));

#print(cars)

#-------------------------
#-------------------------
#-------------------------

#-------------------------
#-------------------------
#-------------------------

#cars = {"BMW", "Benz", "Iran Khodro", "Kia"}

#for item in cars:
#	print(item)

#-------------------------

#cars = {"BMW", "Benz", "Iran Khodro", "Kia"}

#print ("BMW"in cars)

#-------------------------
#-------------------------
#-------------------------

#-------------------------
#-------------------------
#-------------------------

##Once a set is created, you cannot change its items, but you can add new items.

#cars = {"BMW", "Benz", "Iran Khodro", "Kia"}

#print(cars)

#cars.add("Another BMW")

#print(cars)

#-------------------------

##Add Any Iterable
##The object in the update() method does not have to be a set, it can be any iterable object (tuples, lists, dictionaries etc.).

#cars1 = {"BMW (1)", "Benz (1)", "Iran Khodro (1)", "Kia (1)"}
#cars2 = {"BMW (2)", "Benz (2)", "Iran Khodro (2)", "Kia (2)"}

#print(cars1)

#cars1.update(cars2)

#print(cars1)

#-------------------------

##Add Any Iterable
##The object in the update() method does not have to be a set, it can be any iterable object (tuples, lists, dictionaries etc.).

#cars1 = {"BMW (1)", "Benz (1)", "Iran Khodro (1)", "Kia (1)"}
#cars2 = ["BMW (2)", "Benz (2)", "Iran Khodro (2)", "Kia (2)"]

#print(cars1)

#cars1.update(cars2)

#print(cars1)

#-------------------------
#-------------------------
#-------------------------

#-------------------------
#-------------------------
#-------------------------

##If the item to remove does not exist, remove() will raise an error.

#cars = {"BMW", "Benz", "Iran Khodro", "Kia"}

#print(cars)

#cars.remove("BMW")

#print(cars)

#-------------------------

#If the item to remove does not exist, discard() will NOT raise an error.

#cars = {"BMW", "Benz", "Iran Khodro", "Kia"}

#print(cars)

#cars.discard("BMW")

#print(cars)

#-------------------------

#cars = {"BMW", "Benz", "Iran Khodro", "Kia"}

#print(cars)

#cars.pop()

#print(cars)

#-------------------------

#cars = {"BMW", "Benz", "Iran Khodro", "Kia"}

#print(cars)

#cars.clear()

#print(cars)

#-------------------------

#cars = {"BMW", "Benz", "Iran Khodro", "Kia"}

#print(cars)

#del cars

#print(cars) #Runtime Error: name 'cars' is not defined

#-------------------------
#-------------------------
#-------------------------

#-------------------------
#-------------------------
#-------------------------

#cars = {"BMW", "Benz", "Iran Khodro", "Kia"}

#for item in cars:
#	print(item)

#-------------------------
#-------------------------
#-------------------------

#-------------------------
#-------------------------
#-------------------------

##The union() method returns a new set with all items from both sets:

#set1 = {"BMW", "Benz", "Iran Khodro", "Kia"}
#set2 = {10, 20.1, 30, 40, 50, 60, 70, 80, 90, 100}

#result = set1.union(set2)

#print(result)

#-------------------------

#set1 = {"BMW", "Benz", "Iran Khodro", "Kia"}
#set2 = {10, 20.1, 30, 40, 50, 60, 70, 80, 90, 100}

#set1.update(set2)

#print(set1)

#-------------------------

##The intersection_update() method will keep only the items that are present in both sets.

#set1 = {"BMW", "Benz", "Iran Khodro", "Kia"}
#set2 = {10, 20.1, 30, 40, 50, 60, 70, 80, 90, 100, "Kia"}

#set1.intersection_update(set2)

#print(set1)

#-------------------------

##The intersection() method will return a new set, that only contains the items that are present in both sets.

#set1 = {"BMW", "Benz", "Iran Khodro", "Kia"}
#set2 = {10, 20.1, 30, 40, 50, 60, 70, 80, 90, 100, "Kia"}

#result = set1.intersection(set2)

#print(result)

#-------------------------

##The symmetric_difference_update() method will keep only the elements that are NOT present in both sets.

#set1 = {"BMW", "Benz", "Iran Khodro", "Kia"}
#set2 = {10, 20.1, 30, 40, 50, 60, 70, 80, 80, 90, 100, "BMW", "Benz", "Iran Khodro", }

#set1.symmetric_difference_update(set2)

#print(set1)

#-------------------------

##The symmetric_difference() method will return a new set, that contains only the elements that are NOT present in both sets.

#set1 = {"BMW", "Benz", "Iran Khodro", "Kia"}
#set2 = {10, 20.1, 30, 40, 50, 60, 70, 80, 80, 90, 100, "BMW", "Benz", "Iran Khodro", }

#result = set1.symmetric_difference(set2)

#print(result)

#-------------------------
#-------------------------
#-------------------------
