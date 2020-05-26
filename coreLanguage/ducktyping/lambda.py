"""
--> What is Lambda function ?

Lambda function are Namesless or Anonymous functions
'lambda' is  not a function it is a keywork in python


--> Why they are Used.

One-Time-Use ==> Throw away function as they're only used Once
IO of other function ==> They're also passed as inputs or returned as outputs of other High-Order function
Reduce Code Size ==> The body of Lambda function is written in a single line

--> Syntax
lambda arguments: expression
    lambda : 'Specify purpose'
    lambda a1: "Specify use of a1"
    lambda a1...n: "Specify use of a1...n"

"""

# x = lambda a: a * a
# # def x(a): return a * a
# print(x(3))

"""
Anonymous function with in user defined function
"""
def a(x):
    return(lambda y: x + y)

# s = a(5)
# print(s(5))
#
# c = a(10)
# print(c(8))

'''
filter() ==> used to filter the given iterables(list, set, etc) with the help of another function
passed as an argument to test all the elements to be true or false
'''
'''
# lambda with filter
mylist = [1,5,3,5,4,6]
newlist = list(filter(lambda x: (x % 2 == 0), mylist))
# print(newlist)
'''
'''
# lambda with Map()
mylist = [1, 2 ,3, 4, 5, 6, 7, 8, 9]
newlist = list(map(lambda x: (x / 3 != 2), mylist))
print(newlist)
'''


# lambda with reduce()
import functools
a = functools.reduce(lambda x,y: x+y, [23, 56, 48, 91, 1])
print(a)
