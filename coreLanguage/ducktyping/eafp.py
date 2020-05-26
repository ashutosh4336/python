# Duck Typingand Easier to ask foregiveness than permission (EAFP)
import os


class Duck:
    def quack(self):
        print('Quak, quack')

    def fly(self):
        print("Flap, flap")


class Person:
    def quack(self):
        print("I'm Quacking like a Duck")

    def fly(self):
        print("I'm Flapping my Arms")


def quackandfly(thing):
    # Not duck Types non-pythonic
    # if isinstance(thing, Duck):
    #     thing.quack()
    #     thing.fly()
    # else:
    #     print('This has to be a Duck')

    # EAFP (Pythonic)

    try:
        thing.quack()
        thing.fly()
    except Exception as e:
        print(e)

    print('')


d = Duck()
# quackandfly(d)

# print('P instance : ')
p = Person()
# quackandfly(p)


# New example
mydata = {
    'name': 'Ashutosh Panda',
    'age': 21,
    'Occupation': 'Software Developer'
}


# try:
#     print('My name is {name}, I am {age} years old and I am Currently {Occupation}'.format(**mydata))
# except Exception as e:
#     print(f'Missing {e} key')

# New Example

mylist = [1, 5, 32, 4, 6, 97, 4, 5]

# Pythonic

# try:
#     print(mylist[8])
# except Exception as e:
#     print(f'In the List only {len(mylist)} Number is Present')

# more Example


# myfile = '/tmp/test.txt'
myfile = '/tmp/sudo.txt'

# if os.access(myfile, os.R_OK):
#     with open(myfile) as f:
#         print(f.read())
# else:
#     print('File can not be accessed')

try:
    f = open(myfile)
except IOError as e:
    print(f'File can not be accessed {e}')
else:
    with f:
        print(f.read())


# print(f.closed)
