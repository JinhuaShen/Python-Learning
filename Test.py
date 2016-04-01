
x = 7
if x < 1 or x > 6:
    print ("xxx")

y = 8
if y < 9 and y > 7:
    print ("yyy")

# loop
for i in [1, 2, 3, 4, 5]:
    print ("This is iterration number", i)

x = 10
while x >= 0:
    print ("x is still not negative", x)
    x = x - 1

for v in range(100):
    print (v)

#input
#x = input("Please enter a number: ")
#print ("The square of that number is", int(x) * int(x))

# list
name = ["cat", "dog"]
y = 2
z = 3
x = [[1, 2, 3], [y, z], [[[]]]]
print(name[1], name[0])
name[0] = "replace"
print(name[0])

x = ["SPAM", "SPAM", "SPAM", "SPAM", "SPAM", "eggs", "and", "SPAM"]
print(x[5:7])

print(x[:6])
print(x[6:])
print(x[-2])

# dict
phone = {"Alice": 12345, "Bob": 23456, "Cat": 34567}
person = {'first name': "Robin", "Last Name": "Hood"}
print(phone["Alice"])
print(person['first name'])
person['first name'] = "xxxx"
print(person['first name'])

# function
def square(x):
    return x*x

print(square(2))

def change(x):
    x[1] = 4
y = [1, 2, 3]
change(y)
print(y[1])

def change2(y):
    y = 0

y = 1
change2(y)
print(y)

queeble = square
print(queeble(3))

# class
class Basket:
    def __init__(self, contents=None):
        self.contents = contents or []

    def add(self, element):
        self.contents.append(element)

    def print_me(self):
       result = ""
       for element in self.contents:
           result = result + " " + repr(element)

       print("Contains:" + result)

    def __str__(self):
       result = ""
       for element in self.contents:
           result = result + " " + repr(element)

       return result        

b = Basket(["apple", "orange"])
b.add("lemon")
b.print_me()
print(b)

import math
x = math.sqrt(4)
print(x)

from math import sqrt
y = sqrt(9)
print(y)


def safe_division(a, b):
    try:
        return a/b
    except ZeroDivisionError: pass

safe_division(5, 0)
