# Conetxt Manger
### Generic way of Writing to a File
```
f = open('sample.txt', 'w')
f.write('This is contextmanager Test')
f.close()
```
### Generic way of Reading from a File
```
f = open('sample.txt', 'r')
# print(f)
print(f.readlines())
f.close()
```

### General (Convenient) (Writing to a File)
```
with open('sample.txt', 'w') as f:
	f.write('Lorem ipsum dolor sit amet, consectetur adipisicing elit. Impedit asperiores.')

```
### General (Convenient) (Reading from a File)
```
with open('sample.txt', 'r') as f:
	print(f.readlines())

```
### Understanding ContextManager with `Class`
```
class Open_FIle():
	def __init__(self, filename, mode):
		self.filename = filename
		self.mode = mode

	def __enter__(self):
		self.file = open(self.filename, self.mode)
		return self.file


	def __exit__(self, exec_type, exec_value, traceback):
		self.file.close()
		

with Open_FIle('sample.txt', 'w') as f:
	f.write('Class Context Manager Testing\n')

print(f.closed)
```
Here in the class Open_File we've three methods 
	1. __init__
	2. __enter__
	3. __exit__
The first method ```__init__``` is to accept the arguments that we pass and the method will access the attributes that we set from out other Method.
_self_ is the instance itself.
_filename_ is the filename we want perform operation on
_mode_ is the Mode in which We'll open the file. ```['w', 'b']```

The second method ```__enter__``` is where we open or close our file and the object we're working with is returned.

The third method ```__exit__``` is where is safely exit and close the file.
The extra parameters are used when we throw a Error and try to use those Information

`print(f.closed)` verifies whether the file is closed or not

If the file is closed `print(f.closed)` returns `True` otherwise `False`

### Understanding ContextManager with ```Function```

```
from contextlib import contextmanager

@contextmanager
def open_file(file, mode):
	try:
		f = open(file, mode)
		yield f
	finally:
		f.close()

with open_file('sample2.txt', 'w') as f:
	f.write('This is ContextManager with Function')

print(f.closed)
```
To demonstarte contextmanager with function we have to import contextlib class

`@contextmanager` Generator

In the above example we're accepting two paramaters and in the `try` block in the first line we're providing the file and mode to open which is equivalent to the `__init__` method of the `Open_FIle` class

The line `(yield f)` is opening the file which again equivalent to the `__enter__` method

In the `finally` block `f.close()` is making a exit by closing the file.

We also can write the function without `try finally` blcok like this:

```
def open_file(file, mode):
	f = open(file, mode)
	yield f
	f.close()
```

