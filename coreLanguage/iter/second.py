import itertools


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
numbers = [1, 2, 3, 4, 5, 6]
names = ['Ashutosh', 'Pinky']


# result = itertools.combinations(letters, 2)
# result = itertools.permutations(letters, 2)
# result = itertools.product(numbers, repeat=4)
# result = itertools.combinations_with_replacement(numbers, 4)
result = itertools.chain(letters, numbers, names)

for i in result:
    print(i)
