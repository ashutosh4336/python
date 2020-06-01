import itertools
import operator

'''
infinite methods of itertools

    count
    cycle
    repeat
'''

'''
# counter = itertools.count(start=5, step=3)
# counter = itertools.cycle(('On', 'Off'))
# counter = itertools.repeat(2, times=3)

# print(next(counter))
# print(next(counter))
# print(next(counter))
# print(next(counter))
# print(next(counter))
# print(next(counter))
'''
'''
# Map
# square = map(pow, range(10), itertools.repeat(3))
# square = map(lambda x: (x * x * x), range(10))
# square = itertools.starmap(pow, [(0, 2), (1, 2), (2, 4), (3, 5)])

# print(list(square))
'''
'''
# randomnum = [100, 200, 300, 400, 500, 600, 700, 800, 900]
# dailydata = list(zip(itertools.count(), randomnum))
# dailydata = list(zip(range(5), randomnum))
# dailydata = list(itertools.zip_longest(range(10), randomnum))

# print(dailydata)
'''
letters = ['a', 'b', 'c', 'd']
numbers = [10000, 2, 5, 2, 3, 4, 5, 6, 1]
names = ['Ashutosh', 'Pinky']
selctors = [True, False, True, False]


# def lessdntwo(n):
#     if(n < 3):
#         return True
#     else:
#         return False


# result = itertools.takewhile(lessdntwo, numbers)
# result = itertools.dropwhile(lessdntwo, numbers)
# result = itertools.filterfalse(lessdntwo, numbers)
# result = filter(lambda x: x > 2, numbers)
# result = filter(lessdntwo, numbers)
# result = itertools.compress(letters, selctors)
# result = itertools.combinations(letters, 2)
# result = itertools.permutations(letters, 2)
# result = itertools.product(numbers, repeat=4)
# result = itertools.combinations_with_replacement(numbers, 4)
# result = itertools.chain(letters, numbers, names)
# result = itertools.islice(range(10), 6)
# result = itertools.islice(range(10), 3, 8)
# result = itertools.islice(range(10), 3, 8, 2)
# (range(x), starting point, ending point, stepstomove)

#

# result = itertools.accumulate(numbers, lambda x, y: x / y)
# result = itertools.accumulate(numbers, lambda x, y: x * y)
# result = itertools.accumulate(numbers, operator.mul)

# for i in result:
#     print(i)


# File Example
# with open('log.log', 'r') as f:
#     # a = f.read()
#     header = itertools.islice(f, 3)
#
#     for line in header:
#         print(line, end='')


# GROUPBY
people = [
    {
        'name': 'John Doe',
        'city': 'Gotham',
        'state': 'NY'
    },
    {
        'name': 'Jane Doe',
        'city': 'Kings Landing',
        'state': 'NY'
    },
    {
        'name': 'Corey Schafer',
        'city': 'Boulder',
        'state': 'CO'
    },
    {
        'name': 'Al Einstein',
        'city': 'Denver',
        'state': 'CO'
    },
    {
        'name': 'John Henry',
        'city': 'Hinton',
        'state': 'WV'
    },
    {
        'name': 'Randy Moss',
        'city': 'Rand',
        'state': 'WV'
    },
    {
        'name': 'Nicole K',
        'city': 'Asheville',
        'state': 'NC'
    },
    {
        'name': 'Jim Doe',
        'city': 'Charlotte',
        'state': 'NC'
    },
    {
        'name': 'Jane Taylor',
        'city': 'Faketown',
        'state': 'NC'
    }
]


def getstate(person):
    return person['state']


result = itertools.groupby(people, getstate)

# for key, group in result:
#     print(f'{key} {len(list(group))}')
#     for person in group:
#         print(person)
#         print('')
