# ==========================
# 1. Variables and Data Types
# ==========================
x = 10 #Integer
price = 19.99 #Float
name = 'Yardley' #String
isActive = False #Boolean
listExample = [1,2,3,4,5] #List
tupleExample = (10,20,30 )#Tuple
person = {name : "Jason"} #Dictionary
unique_numbers = {1,2,3,4} #Set

#Print and type() function
print(type(x))
print(type(price))

# ==========================
# 2. Conditional Statements
# ==========================
age = 20

if age >= 18:
    print("adult")
elif age > 12:
    print("Teen")
else:
    print("Child")

#Ternary
status = "Adult" if age > 18 else "Minor"
print(status)

# <do this> if condition else <do this>


# ==========================
# 3. Loops
# ==========================

#For Loop
for i in range(10):
    print(i)

#While Loop
count = 0
while count < 2:
   print(count)
   count += 1

#Loop w Break and Continue
for numbers in range(50):
    if numbers == 5:
        break #Eit loop
    if numbers % 2 == 0:
        continue #Skip even nums


# ==========================
# 4. Functions
# ==========================

def greet (name, age):
    return f"Hello, {name}, you are {age}"


#Default Parameters
def add (x, y=10):
    return x + y


#Lambda Functions
square = lambda x: x * x
print(square(4))

# ==========================
# 5. Lists and List Comprehensions
# ==========================
favoriteNumbers = [13,24,513,23,1,5240,40];
squared = [n ** 2 for n in favoriteNumbers]
print(f"these are my favorite numbers squared: {squared}")

# List Methods
favoriteNumbers.append(6)
favoriteNumbers.append(3)
print(favoriteNumbers)

# ==========================
# 6. Dictionaries
# ==========================
person = {
    "name": "Yardley",
    "age": 25,
    "city": "Chicago"
}
print(person["name"])

for key, value in person.items():
    print(f"{key}:{value}")

# ==========================
# 7. Classes and Objects
# ==========================

class Person:
    def __init__(self, name, food):
        self.name = name
        self.favoriteFood = food
    def greet(self):
        return f"Hi, My name is {self.name} and my favorite food is {self.favoriteFood}"

firstInstance = Person("Jack", "Greek Food")
print(firstInstance)

# ==========================
# 8. Exception Handling
# ==========================
try:
    result = 10/ 0
except ZeroDivisionError:
    print("cannot divide by zero")
finally:
    print("execution complete")

# ==========================
# 9. File Handling
# ==========================

with open("example.txt", "w") as file:
    file.write("hello world! This is a text for a new file")
with open("example.txt" , "r") as file:
    content = file.read()
    print(content)


# ==========================
# 10. Importing Modules
# ==========================

import math
print(math.sqrt(16))

from datetime import datetime
print(datetime.now())

print("minute" ,datetime.min)




# ==========================
# 11. List of Common Built-in Functions
# ==========================

"""
- len()       - Get length of object
- type()      - Get type of object
- str()       - Convert to string
- int()       - Convert to integer
- float()     - Convert to float
- bool()      - Convert to boolean
- sorted()    - Sort iterable
- sum()       - Sum of elements
- max()       - Maximum element
- min()       - Minimum element
- zip()       - Combine iterables
- map()       - Apply function to iterable
- filter()    - Filter elements based on condition
- range()     - Create sequence of numbers
- enumerate() - Get index and value in a loop

"""