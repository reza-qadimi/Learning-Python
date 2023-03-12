# -------------------------
# -------------------------
# -------------------------

##Inheritance allows us to define a class that inherits all the methods and properties from another class.

##Parent class is the class being inherited from, also called base class.

##Child class is the class that inherits from another class, also called derived class.

#class my_class_01(object):
#	pass

# -------------------------

##Any class can be a parent class, so the syntax is the same as creating any other class:

#class My_Parent_Class(object):

#	def __init__(self, firstParameter, secondParameter):
#		self.firstParameter = firstParameter
#		self.secondParameter = secondParameter

#	def print(self):
#		value = f"{self.firstParameter} - {self.secondParameter}"

#		print(value)

#class My_Child_Class(My_Parent_Class):
#	pass

#myChid = My_Child_Class(firstParameter = "A", secondParameter = "B")

#myChid.print()

# -------------------------

#class My_Parent_Class(object):

#	def __init__(self, firstParameter, secondParameter):
#		self.firstParameter = firstParameter
#		self.secondParameter = secondParameter

#	def print(self):
#		value = f"{self.firstParameter} - {self.secondParameter}"

#		print(value)

#class My_Child_Class(My_Parent_Class):
#	def __init__(self,firstParameter, secondParameter, anotherParameter):

#		My_Parent_Class.__init__(
#			self = self,
#			firstParameter = firstParameter,
#			secondParameter = secondParameter)

#		self.anotherParameter = anotherParameter

#	def print_child(self):
#		value = f"{self.anotherParameter} - " +\
#			f"{self.firstParameter} - {self.secondParameter}"

#		print(value)


#myChid = My_Child_Class(
#	firstParameter = "A",
#	secondParameter = "B",
#	anotherParameter = 12)

#myChid.print()
#myChid.print_child()

# -------------------------

##Python also has a super() function that will make the child class inherit all the methods and properties from its parent:

#class My_Parent_Class(object):

#	def __init__(self, firstParameter, secondParameter):
#		self.firstParameter = firstParameter
#		self.secondParameter = secondParameter

#	def print(self):
#		value = f"{self.firstParameter} - {self.secondParameter}"

#		print(value)

#class My_Child_Class(My_Parent_Class):
#	def __init__(self,firstParameter, secondParameter, anotherParameter):

#		super().__init__(
#			firstParameter = firstParameter,
#			secondParameter = secondParameter)

#		self.anotherParameter = anotherParameter

#	def print_child(self):
#		value = f"{self.anotherParameter} - " +\
#			f"{self.firstParameter} - {self.secondParameter}"

#		print(value)


#myChid = My_Child_Class(
#	firstParameter = "A",
#	secondParameter = "B",
#	anotherParameter = 12)

#myChid.print()
#myChid.print_child()

# -------------------------

#class My_Parent_Class(object):

#	def __init__(self, firstParameter, secondParameter):
#		self.firstParameter = firstParameter
#		self.secondParameter = secondParameter

#	def print(self):
#		value = f"{self.firstParameter} - {self.secondParameter}"

#		print(value)

#class My_Child_Class(My_Parent_Class):
#	def __init__(self,firstParameter, secondParameter, anotherParameter):

#		super().__init__(
#			firstParameter = firstParameter,
#			secondParameter = secondParameter)

#		self.anotherParameter = anotherParameter

#	def print_child(self):
#		value = f"{self.anotherParameter} - " +\
#			f"{self.firstParameter} - {self.secondParameter}"

#		print(value)

#	def print(self):
#		value = f"{self.anotherParameter} - " +\
#			f"{self.firstParameter} - {self.secondParameter}"
		
#		print(value)

#myChid = My_Child_Class(
#	firstParameter = "A",
#	secondParameter = "B",
#	anotherParameter = 12)

#myChid.print()
#myChid.print_child()

# -------------------------
# -------------------------
# -------------------------




