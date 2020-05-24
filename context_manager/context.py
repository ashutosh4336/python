import os
# f = open('sample.txt', 'w')
# f.write('Lorem ipsum dolor sit amet, consectetur adipisicing elit. Doloremque dignissimos esse accusamus ipsam sit eum quo repellat expedita officia dolorem velit molestias nam, voluptas aut molestiae illum fugit explicabo facere?')
# f.close()

# f = open('sample.txt', 'r')
# # print(f)
# print(f.readlines())
# f.close()

# print(os.listdir())
# print(os.remove('sample.txt'))
# print(os.listdir())


# ------------------------ With Context Manager -------------------------------- #
# with open('sample.txt', 'w') as f:
# 	f.write('Lorem ipsum dolor sit amet, consectetur adipisicing elit. Impedit asperiores.')

# with open('sample.txt', 'r') as f:
# 	print(f.readlines())


# ------------------- Context Manager With Class ---------------------- #
# class Open_FIle():
# 	def __init__(self, filename, mode):
# 		self.filename = filename
# 		self.mode = mode

# 	def __enter__(self):
# 		self.file = open(self.filename, self.mode)
# 		return self.file


# 	def __exit__(self, exec_type, exec_value, traceback):
# 		self.file.close()
		

# with Open_FIle('sample.txt', 'w') as f:
# 	f.write('Class Context Manager Testing\n')
# 	f.write('Class Context Manager Testing Two\n')


# print(f.closed)
# ------------------- Context Manager With Function ---------------------- #
from contextlib import contextmanager

@contextmanager
def open_file(file, mode):
	f = open(file, mode)
	yield f
	f.close()

with open_file('sample2.txt', 'w') as f:
	f.write('This is ContextManager with Function')

print(f.closed)