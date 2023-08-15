"""
print("hello")

if 5>2:
    print("Five is greater than two")
else:
    print("Five not less than two")

x = 5
y = "hello"
print(x)

x = str(3)
y = int(2)
z = str("hello")

print(type(y))
"""

fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

x=5
y='Hello'
print(x,y)

#functions, yayy!
x = 'functions'

def funname():
    #If there is a print statement inside the function, it executes this variable first
    #and then it executes the print statement outside the function.
    x = 'fantastic'
    print('python is ' + x)
funname()

print('python is ' + x)

#convert complex to float
z = 0.134343+3322j   # complex
z = float(z.real)
print(z)

#convert complex to int
z = 134343+3322j   # complex
z = int(z.real)
print(z)

goldman = 0.005100608207126714+0j
print(goldman)

goldman = float(goldman.real)
print(goldman)