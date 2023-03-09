# This is a comment

#print('Hello, World!');

#-------------------------
#x = 13		# x is of type int (integer)
#print(x)
#-------------------------

#-------------------------
#x = 13;		# x is of type int (integer)
#print(x);
#-------------------------

#-------------------------
#x = "Hi";	# x is now of type str (string)
#print(x);
#-------------------------


#-------------------------
#x = 'Hi';	# x is of type str (string)
#print(x);
#-------------------------

#-------------------------
#x = 13;
#y = 26;

#print(x * y);
#-------------------------

#-------------------------
#x, y = 13, 26;

#print(x * y);
#print(x + y);
#-------------------------

#-------------------------
#x, y = 13, 'Hello';

#print(x);
#print(y);

#print(x * y);
#print(x + y); -> Runtime Error: unsupported operand type(s) for +: 'int' and 'str'
#-------------------------

#-------------------------
#x, y = 13, 26;

#z1 = x * y;
#z2 = x + y;

#print(z1);
#print(z2);
#-------------------------

#-------------------------
#l = [13, 26];
#x, y = l;
#z1 = x * y;
#z2 = x + y;

#print(z1);
#print(z2);
#-------------------------

#-------------------------
#l1 = l2 = [13, 26];

#x1, y1 = l1;
#x2, y2 = l2;

#z1 = x1 * y1;
#z2 = x2 * y2;

#print(z1);
#print(z2);
#-------------------------

#-------------------------
# casting:
#-------------------------
#x = str(3)		# x will be '3'
#y = int(3)		# y will be 3
#z = float(3)	# z will be 3.0

# y = int('string')		#Runtime Error: invalid literal for int() with base 10: 'string'
#-------------------------

#-------------------------
# Type
#-------------------------
#typeOfX = type(x);
#print(typeOfX);
##print(type(x));
##print(type(x))

#typeOfY = type(y);
#print(typeOfY);

##print(type(y));
##print(type(y))
#-------------------------

#-------------------------
# Case-Sensitive:
# variable names are case-sensitive:
#-------------------------
#a = 23;
#A = 24;

#print(a);
#print(A);

#Note: A will not overwrite a
#------------------------


#------------------------
# Naming:
#------------------------

# نام متغیرها می بایستی با:
#	- شروع شود underscore حروف یا
# نام متغیرها نمی تواند با اعداد شروع شود

# نام متغیرها صرفا و فقط می تواند شامل حروف، اعداد و _باشد

# نام متغیرها به حروف بزرگ و کوچک حساس هستند -> Case-Sensitive
# age, Age and AGE are 3 different variables

# نام متغیرها نمی تواند برابر با هیچ یک از حروف خاص پایتون باشد
# https://w3schools.com/python/python_ref_keywords.asp

# هر چند میتوان از نام گذاری به این صورت استفاده کرد:
# a = 12
# b = 'x'
# r = 13 * 12
# اما ما به عنوان یک برنامه نویس حرفه ای، برای نام گذاری متغیرهای خود از اسامی با معنای مناسب (جهت افزایش خوانایی کد) استفاده میکنیم.

#------------------------

#------------------------
#------------------------
#------------------------
# Camel Case:
#------------------------
# Each word, except the first, starts with a capital letter:

#myVariableName = "John"
#------------------------


#------------------------
#Pascal Case:
#------------------------
# Each word starts with a capital letter:

#MyVariableName = "John"
#------------------------

#------------------------
#Snake Case
#------------------------
#Each word is separated by an underscore character:

#my_variable_name = "John"
#------------------------
#------------------------
#------------------------

#------------------------

#------------------------
