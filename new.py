fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)
"""
#global variable
def globalfun():
    global x
    x = 'fantastic'
globalfun()
print('python is ' +x)
"""
#global variable and two variables
x = 'fun'
#Only the global variable value will be executed.
def globalfun():
    global x
    x = 'fantastic'
globalfun()
print('python is ' +x)

x = frozenset({"apple", "banana", "cherry"})

#display x:
print(x)

#display the data type of x:
print(type(x))

#Type Casting
x = 1    # int
y = 2.8  # float
z = 1j   # complex

#convert from int to float:
a = float(x)

#convert from float to int:
b = int(y)

#convert from int to complex:
c = complex(x)

z = float(z.real)
print(z)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))

x = str(2)
print(x)

#string [array]
a = 'Hello'
print(a[1], a[2], a[4])

#string through a for loop
for x in 'string':
    print(x)

#Return the length of a string
a = 'Hello'
print(len(a))

#check for a particular word in a string
x = 'hello, there u r!'
print('u' in x)
#If there word is present in the string, it returns true else false

#keeping the same string
x = 'hello, there u r!'
if 'u' in x:
    print("Yes, 'u' not in x")

#check for a particular word not in a string
x = 'hello, there u r!'
print('hi' not in x)
#If there word is present in the string, it returns false else true

#slicing
x = 'Hello, world!'
print(x[2:7])
#from the start to the 7th position
print(x[:7])
#excluding the first 3 letter aka index of array from 0 to 2
print(x[2:])
#Negative indexing -> starts from left to right
print(x[-5:-2])

#case
a = " Hello, Nice to see you! "
print(a.upper())
print(a.lower())
#trim white space
print(a.strip())
#replace letters or words
print(a.replace('Hello','Hi'))
#split
print(a.split(","))

import pandas as pd

json = pd.read_csv(r'C:\Users\KAREN J FERNANDES\AppData\Local\Programs\Python\Python311\Scripts\Files\Study Notes\json_data.csv')

json.head()

#how to include an integer in a string and print it
age = 25
txt = "I am Karlyn, I am {} years old. "
print(txt.format(age))

text = "I am strong \"and\" supported by God"
print(text)







