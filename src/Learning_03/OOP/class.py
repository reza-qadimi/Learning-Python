# -------------------------
# -------------------------
# -------------------------

#class MyClass:

# -------------------------

#class MyClass:
#	value = 27

# -------------------------

#class MyClass:
#	value = 27

#myClass = MyClass()

#value = myClass.value

#print(value)

# -------------------------

#class GooGooli:
#	value = 27

#googooli1 = GooGooli()

#value = googooli1.value

#print(value)

# -------------------------

##All classes have a function called __init__(), which is always executed when the class is being initiated.

##Use the __init__() function to assign values to object properties, or other operations that are necessary to do when the object is being created:

##The __init__() function is called automatically every time the class is being used to create a new object.

#class User:

#	def __init__(self, username, password):

#		self.username = username
#		self.password = password

#user = User(username = "RezaQadimi", password = "*****")

#print(user.username)
#print(user.password)

# -------------------------

#class User:

#	def __init__(self, username, password):

#		self.username = username
#		self.password = password

#user = User(username = "RezaQadimi", password = "*****")

#print(user)

#result = user.__str__()
#print(result)

# -------------------------

##The __str__() function controls what should be returned when the class object is represented as a string.

##If the __str__() function is not set, the string representation of the object is returned:

#class User:

#	def __init__(self, username, password):

#		self.username = username
#		self.password = password

#	def __str__(self):
#		value = f"Username: {self.username} and Password: {self.password}"

#		return value

#user = User(username = "RezaQadimi", password = "*****")

#print(user)

##result = user.__str__()
##print(result)

# -------------------------

#class User:

#	def __init__(magooli1, username, password):

#		magooli1.username = username
#		magooli1.password = password

#	def __str__(magooli2):
#		value = f"Username: {magooli2.username} and Password: {magooli2.password}"

#		return value

#user = User(username = "RezaQadimi", password = "*****")

#print(user)

# -------------------------

#class User:

#	def __init__(self, username, password):

#		self.username = username
#		self.password = password

#	def __str__(self):
#		value = f"Username: {self.username} and Password: {self.password}"

#		return value

#	def change_username(self, username):
#		self.username = username

#user = User(username = "RezaQadimi", password = "*****")

#print(user.username)

#user.change_username("NewUsername")

#print(user.username)

# -------------------------

#class User:

#	def __init__(self, username, password):

#		self.username = username
#		self.password = password

#	def __str__(self):
#		value = f"Username: {self.username} and Password: {self.password}"

#		return value

#user = User(username = "RezaQadimi", password = "*****")

#print(user.username)

#user.username = "NewUsername"

#print(user.username)

# -------------------------

#class User:

#	def __init__(self, username, password, fullName):

#		self.username = username
#		self.password = password
#		self.fullName = fullName

#user = User(username = "RezaQadimi", password = "*****", fullName = "Reza Qadimi")

#print(user.fullName)

#del user.fullName

#print(user.fullName) #Runtime Error: 'User' object has no attribute 'fullName'

# -------------------------

#class User:

#	def __init__(self, username, password, fullName):

#		self.username = username
#		self.password = password
#		self.fullName = fullName

#user = User(username = "RezaQadimi", password = "*****", fullName = "Reza Qadimi")

#del user

#print(user.fullName) #Runtime Error: name 'user' is not defined

# -------------------------
# -------------------------
# -------------------------
