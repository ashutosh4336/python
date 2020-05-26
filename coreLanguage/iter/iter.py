# iniarray = [11, 12, 13, 14]

# print(dir(iniarray))

# itar = iniarray.__iter__()
# itar = iter(iniarray)

# print(itar)
# print(dir(itar))

# while True:
#     try:
#         i = next(itar)
#         print(i)
#     except StopIteration:
#         print('No Item')
#         break


# print(next(itar))
# print(next(itar))
# print(next(itar))


# for i in iniarray:
# print(i)

# print(next())


#---------------------------------------------------------#
class Myrange:
    def __init__(self, start, end):
        self.value = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.value >= self.end:
            raise StopIteration
        current = self.value
        self.value += 1
        return current


nums = Myrange(1, 10)
# print(next(nums))
# for i in nums:
#     print(i)


def myrangedef(start, end):
    current = start
    while current < end:
        yield current
        current += 1


numb = myrangedef(5, 10)

# for i in numb:
#     print(i)


cities = ['bhubaneswar', 'lucknow', 'indoore', 'delhi', 'mumbai', 'chennai', 'london']
# print(sorted(cities))


def sortbylen(l):
    result = sorted(l, key=lambda x: len(x))
    return result


print(sortbylen(cities))
