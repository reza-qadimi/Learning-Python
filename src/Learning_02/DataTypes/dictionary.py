#Dictionaries are used to store data values in key:value pairs.
#Dictionary items can be referred to by using the key name.
#A dictionary is a collection which is ordered*, changeable and do not allow duplicates.

#Ordered or Unordered?
#When we say that dictionaries are ordered, it means that the items have a defined order, and that order will not change.
#Unordered means that the items does not have a defined order, you cannot refer to an item by using an index.

#Changeable
#Dictionaries are changeable, meaning that we can change, add or remove items after the dictionary has been created.

#Duplicates Not Allowed
#Dictionaries cannot have two items with the same key:

#-------------------------
#-------------------------
#-------------------------

#user = {
#	"username": "Reza-Qadimi",

#	"firstName": "Reza",
#	"lastName": "Qadimi",

#	"birthDate": 1995,

#	"isActive": True,
#	"isVerified": True,
#}

#print(user)

#valueDataType = type(user)

#print(valueDataType)

#-------------------------

#user = {
#	"username": "Reza-Qadimi",

#	"firstName": "Reza",
#	"lastName": "Qadimi",

#	"birthDate": 1995,

#	"isActive": True,
#	"isVerified": True,
#}

#print(user)

#print(user["username"])

#-------------------------

#user = {
#	"username": "Reza-Qadimi (1)",
#	"username": "Reza-Qadimi (2)",

#	"firstName": "Reza",
#	"lastName": "Qadimi",

#	"birthDate": 1995,

#	"isActive": True,
#	"isVerified": True,
#}

#print(user)

#print(user["username"])

#-------------------------

#user = {
#	"username": "Reza-Qadimi (1)",
#	"username": "Reza-Qadimi (2)",

#	"firstName": "Reza",
#	"lastName": "Qadimi",

#	"birthDate": 1995,

#	"isActive": True,
#	"isVerified": True,
#}

#print(user)

#dictionaryLength = len(user)

#print(dictionaryLength)

#-------------------------

#user = dict(username = "Reza-Qadimi",
#	firstName = "Reza", lastName = "Qadimi",
#	birthDate = 1995, isActive =  True, isVerified = True)

#print(user)

#-------------------------
#-------------------------
#-------------------------

#-------------------------
#-------------------------
#-------------------------

#user = {
#	"username": "Reza-Qadimi",

#	"firstName": "Reza",
#	"lastName": "Qadimi",

#	"birthDate": 1995,

#	"isActive": True,
#	"isVerified": True,
#}

#print(user)

#firstName = user["firstName"]

#print(firstName)

#-------------------------

#user = {
#	"username": "Reza-Qadimi",

#	"firstName": "Reza",
#	"lastName": "Qadimi",

#	"birthDate": 1995,

#	"isActive": True,
#	"isVerified": True,
#}

#print(user)

#firstName = user.get("firstName")

#print(firstName)

#-------------------------

#user = {
#	"username": "Reza-Qadimi",

#	"firstName": "Reza",
#	"lastName": "Qadimi",

#	"birthDate": 1995,

#	"isActive": True,
#	"isVerified": True,
#}

#print(user)

#keys = user.keys()

#print(keys)

#-------------------------

#user = {
#	"username": "Reza-Qadimi",

#	"firstName": "Reza",
#	"lastName": "Qadimi",

#	"birthDate": 1995,

#	"isActive": True,
#	"isVerified": True,
#}

#print(user)

#values = user.values()

#print(values)

#-------------------------

#user = {
#	"username": "Reza-Qadimi",

#	"firstName": "Reza",
#	"lastName": "Qadimi",

#	"birthDate": 1995,

#	"isActive": True,
#	"isVerified": True,
#}

#print(user)

#items = user.items()

#print(items)

#-------------------------

#user = {
#	"username": "Reza-Qadimi",

#	"firstName": "Reza",
#	"lastName": "Qadimi",

#	"birthDate": 1995,

#	"isActive": True,
#	"isVerified": True,
#}

#print(user)

#if "firstName" in user:
#	print(True)

#-------------------------
#-------------------------
#-------------------------

#-------------------------
#-------------------------
#-------------------------

#user = {
#	"username": "Reza-Qadimi",

#	"firstName": "Reza",
#	"lastName": "Qadimi",

#	"birthDate": 1995,

#	"isActive": True,
#	"isVerified": True,
#}

#print(user)

#user["birthDate"] = 1994
#user["isActive"] = False
#user["isVerified"] = False

#print(user)

#-------------------------

#user = {
#	"username": "Reza-Qadimi",

#	"firstName": "Reza",
#	"lastName": "Qadimi",

#	"birthDate": 1995,

#	"isActive": True,
#	"isVerified": True,
#}

#print(user)

#user["gender"] = "Male"

#print(user)

#-------------------------

#user = {
#	"username": "Reza-Qadimi",

#	"firstName": "Reza",
#	"lastName": "Qadimi",

#	"birthDate": 1995,

#	"isActive": True,
#	"isVerified": True,
#}

#print(user)

#user.update({ "isActive": False, "isVerified": False })

#print

#-------------------------

#user = {
#	"username": "Reza-Qadimi",

#	"firstName": "Reza",
#	"lastName": "Qadimi",

#	"birthDate": 1995,

#	"isActive": True,
#	"isVerified": True,
#}

#print(user)

#user.update({ "gender": "Male" })

#print(user)

#-------------------------
#-------------------------
#-------------------------

#-------------------------
#-------------------------
#-------------------------

#user = {
#	"username": "Reza-Qadimi",

#	"firstName": "Reza",
#	"lastName": "Qadimi",

#	"birthDate": 1995,

#	"isActive": True,
#	"isVerified": True,
#}

#print(user)

#user.pop("username")

#print(user)

#-------------------------

#user = {
#	"username": "Reza-Qadimi",

#	"firstName": "Reza",
#	"lastName": "Qadimi",

#	"birthDate": 1995,

#	"isActive": True,
#	"isVerified": True,
#}

#print(user)

#user.pop() #Runtime Error: pop expected at least 1 argument, got 0

#print(user)

#-------------------------

#user = {
#	"username": "Reza-Qadimi",

#	"firstName": "Reza",
#	"lastName": "Qadimi",

#	"birthDate": 1995,

#	"isActive": True,
#	"isVerified": True,
#}

#print(user)

#user.popitem() #"isVerified": True,

#print(user)

#-------------------------

#user = {
#	"username": "Reza-Qadimi",

#	"firstName": "Reza",
#	"lastName": "Qadimi",

#	"birthDate": 1995,

#	"isActive": True,
#	"isVerified": True,
#}

#print(user)

#del user["isActive"]
#del user["isVerified"]

#print(user)

#-------------------------

#user = {
#	"username": "Reza-Qadimi",

#	"firstName": "Reza",
#	"lastName": "Qadimi",

#	"birthDate": 1995,

#	"isActive": True,
#	"isVerified": True,
#}

#print(user)

#del user

#print(user) #Runtime Error: name 'user' is not defined

#-------------------------

#user = {
#	"username": "Reza-Qadimi",

#	"firstName": "Reza",
#	"lastName": "Qadimi",

#	"birthDate": 1995,

#	"isActive": True,
#	"isVerified": True,
#}

#print(user)

#user.clear()

#print(user)

#-------------------------
#-------------------------
#-------------------------

#-------------------------
#-------------------------
#-------------------------

#user1 = {
#	"username": "Reza-Qadimi",

#	"firstName": "Reza",
#	"lastName": "Qadimi",

#	"birthDate": 1995,

#	"isActive": True,
#	"isVerified": True,
#}

#print(user1)

#user2 = user1.copy()

#print(user2)

#-------------------------

#user1 = {
#	"username": "Reza-Qadimi",

#	"firstName": "Reza",
#	"lastName": "Qadimi",

#	"birthDate": 1995,

#	"isActive": True,
#	"isVerified": True,
#}

#print(user1)

#user2 = dict(user1)

#print(user2)

#-------------------------
#-------------------------
#-------------------------

#-------------------------
#-------------------------
#-------------------------

#user1 = {
#	"username": "Reza-Qadimi",

#	"firstName": "Reza",
#	"lastName": "Qadimi",

#	"birthDate": 1995,

#	"isActive": True,
#	"isVerified": True,
#}

#user2 = {
#	"username": "Farbod-Javan",

#	"firstName": "Farbod",
#	"lastName": "Fazaeli Javan",

#	"birthDate": 1990,

#	"isActive": False,
#	"isVerified": True,
#}

#team2 = {
#	"backendDeveloper": user1,
#	"ProductOwner": user2
#}

#print(team2)

#backendDeveloperFullName =\
#	team2["backendDeveloper"]["firstName"] +\
#	" " +\
#	team2["backendDeveloper"]["lastName"]

#print(backendDeveloperFullName)

#-------------------------

#-------------------------
#-------------------------
#-------------------------

#-------------------------
#-------------------------
#-------------------------

#user = {
#	"username": "Reza-Qadimi",

#	"firstName": "Reza",
#	"lastName": "Qadimi",

#	"birthDate": 1995,

#	"isActive": True,
#	"isVerified": True,
#}

#for item in user: #print keys
#	print(item)

#-------------------------

#user = {
#	"username": "Reza-Qadimi",

#	"firstName": "Reza",
#	"lastName": "Qadimi",

#	"birthDate": 1995,

#	"isActive": True,
#	"isVerified": True,
#}

#for item in user.keys():
#	print(item)

#-------------------------

#user = {
#	"username": "Reza-Qadimi",

#	"firstName": "Reza",
#	"lastName": "Qadimi",

#	"birthDate": 1995,

#	"isActive": True,
#	"isVerified": True,
#}

#for item in user.values():
#	print(item)

#-------------------------

#user = {
#	"username": "Reza-Qadimi",

#	"firstName": "Reza",
#	"lastName": "Qadimi",

#	"birthDate": 1995,

#	"isActive": True,
#	"isVerified": True,
#}

#for item in user.items():
#	print(item)

#-------------------------
#-------------------------
#-------------------------
