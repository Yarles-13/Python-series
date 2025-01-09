"""
small func that are RESTRICTED to a single expression
-anonymous functions

"""
square = lambda x: x ** 2
print(square(56))

multiple_argument_lambda = lambda var1, var2 : var1 * var2
print(multiple_argument_lambda(4,0))

def my_func(nums):
    return lambda x: x * nums
doubler = my_func(2)
print(doubler(5))

#using lambda with pythons list() builtin func
my_list = [12,4,2,4,5,5]
odd_numbers = list(filter(lambda x: x % 2 != 0, my_list))

#using lambda func for sorting
list_before_sorted = [("apple", 50), ("banana", 20), ("cherry", 30)]
list_sorted = sorted(list_before_sorted, key=lambda x: x[1])
print(list_sorted)

#using lambda function return a func
def my_new_function (nums):
    return lambda x: x + nums

adder = my_new_function(5)
print(adder(10))

my_teams = [("Chicago Bears",4), ("White Sox", 41), ("BlackHawks", 24), ("Bulls", 40)]
new_teams_list =  [(lambda x: x[1])(x) for x in my_teams]
print(new_teams_list)

#using lamda func to sort a list of string by last character
string_array = ["apple", "banana", "cherry"]
sorted = sorted(string_array, key=lambda x:x[-1])
print(sorted)

#Using lambda func w reduce func
from functools import reduce

before_reduce = [1,3,4,5,6,7,8,8,8,5,3,2]
product = reduce((lambda x, y: x * y), before_reduce)
print(product)

#Using a lambda func with the map func

before_map = [22,4,4432,324,34,335,325,25]
after_map = list(map(lambda x: x ** 2, before_map))
print(after_map)