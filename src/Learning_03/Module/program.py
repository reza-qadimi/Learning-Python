#Now we can use the module we just created, by using the import statement:


# -------------------------
# -------------------------
# -------------------------

#import module;

#module.my_custom_print("Hello, World")

#print(personFirstName)

# -------------------------

#import module;

#personFirstName = module.person["firstName"]

#print(personFirstName)

# -------------------------

#import module as m;

#personFirstName = m.person["firstName"]

#print(personFirstName)

# -------------------------

#import platform;

#myPlatform = platform.system()

#print(myPlatform)

# -------------------------

##Using the dir() Function
##There is a built-in function to list all the function names (or variable names) in a module. The dir() function:

import platform;

platformNames = dir(platform)

print(platformNames)

# -------------------------
# -------------------------
# -------------------------
