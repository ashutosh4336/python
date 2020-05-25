# Lists
# language = ['JavaScript', 'Python', 'Clojure', 'Rust', 'C']
# framework = ['React', 'Angular', 'Vue', 'Django', 'PyTorch']
# nums = [5, 6, 9, 5, 6, 6, 56, 87, 96, 98]
# In Formatting with [::] first index is inclusive but second index is not inclusive
#
# courses.append('React')
# courses.insert(0, 'React')
# language.extend(framework)
# language.remove('Rust')
# poped = language.pop(1)
# print(poped)
# language.reverse()
# language.sort()
# nums.sort(reverse=True)
#
# Sorted Function
# print(sorted(language))
#
# print(min(nums))
# print(max(nums))
# print(sum(nums))
#
# print(language.index('Rust'))
# print('Java' in language)
# print('Python' in language)
#
#
# for index, item in enumerate(language, start=1):
#     print(index, item)
#
# courses_str = ', '.join(language)
# print(type(courses_str))
# print(courses_str)
#
# newlist = courses_str.split(', ')
# print(newlist)
#
# print(language)
# print(nums)

# Tuples

# copyofLang = language
# print(copyofLang)
#
# language[0] = 'Assembly'
#
# print(language)
# print(copyofLang)

#
# language = ('JavaScript', 'Python', 'Clojure', 'Rust', 'C')
# framework = ('React', 'Angular', 'Vue', 'Django', 'PyTorch')
# nums = (5, 6, 9, 5, 6, 6, 56, 87, 96, 98)
#
#
# copyofLang = language
#
# print(language)
# print(copyofLang)

# Sets
#
# language = {'JavaScript', 'Python', 'Clojure', 'Rust', 'C'}
# morelanguage = {'JavaScript', 'Java', 'Ruby', 'PHP', 'C++', 'Python'}
#
# print(morelanguage.intersection(language))
# print(morelanguage.difference(language))
# print(morelanguage.union(language))

# Dictionaries
# students = {
#     'name': 'Ashutosh',
#     'age': 21,
#     'gender': 'Male',
#     'languageknown': [
#         'JavaScript', 'Python', 'Nodejs', 'React'
#     ]
# }
#
# students['phone'] = '8763076463'
# students['name'] = 'Ashutosh Panda'
#
# students.update({'name': 'Ashutosh Panda', 'phone': 8763076463})
#
# age = students.pop("age")
#
# del students['age']
#
# print(students.keys())
# print(students.values())
# print(students.items())
#
#
# for key, val in students.items():
#     print(key, val)
#
#
# print(students)
# print(age)

'''
Comparison
Equal:              ==
Not Equal           !=
Greater Than        >
Less Than           <
Grater or Equal     >=
Less or Equal       <=
Object Identity     is
'''


lang = 'Python'

if lang == 'Python':
    print('We\'re Learning Python ')
else:
    print('Condition is False')
