
"""
Comparison
Equal:              ==
Not Equal           !=
Greater Than        >
Less Than           <
Grater or Equal     >=
Less or Equal       <=
Object Identity     is
"""

"""
and
or
not
"""

#
# lang = 'Python'
#
# if lang == 'JavaScript':
#     print('We\'re Learning JavaScript')
# elif lang == 'PHP':
#     print('We\'re Learning PHP')
# else:
#     print('Unknown Language')


# user = 'Admin'
#
# loggedin = False
# if user == 'Admin' or loggedin:
#     print('Authorized User')
# else:
#     print('Unauthorized user')

#
# if not loggedin:
#     print('Please login')
# else:
#     print('Welcome Admin')

# a = [1, 2, 3]
# b = a

# print(a == b)
# print(a is b)
#
# print(id(a))
# print(id(b))
# print(a is b)
"""
False values:
            False
            None
            Zero of any numeric type
            Any empty sequency. eg - [], (), ''
            Any empty mapping. eg - {}
"""
#
# condition = []
#
# if condition:
#     print('Evaluated to True')
# else:
#     print('Evaluated to False')

# nums = [1, 5, 6, 9]
# for n in nums:
#     if n == 3:
#         print(f'Found it... {n}')
#         continue
#     print(n)

# for n in nums:
#     for letter in 'abcde':
#         print(n, letter)

# for i in range(len(nums)):
#     print(i)

# for i in range(1, 9):
#     print(i)


# While Loops

# while condition:
# pass

# x = 0
#
# while x < 10:
#     if(x == 5):
#         break
#
#     print(x)
#     x += 1


# Else Clause in Loops
# i = 5
# for i in nums:
#     print(i)
#
# else:
#     print('Hello Surprise MOFO')
# ----------------------------------------------------------------------------- #
# import socket
# import requests
# hostname = socket.gethostname()
# IPAddr = socket.gethostbyname(hostname)
#
# url = 'https://api.ipify.org'
# r = requests.get(url)
#
# print('')
# print(f"Your Computer Name is: {hostname}")
# print(f"Your Computer Internal  IP Address is: {IPAddr}")
# print(f"Your Computer External  IP Address is: {r.text}\n")
# ----------------------------------------------------------------------------- #
