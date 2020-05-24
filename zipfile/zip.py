import zipfile
import shutil
import requests
import os

myzip =  zipfile.ZipFile('pngs.zip', 'w')
with zipfile.ZipFile('pngs.zip', 'w', compression=zipfile.ZIP_DEFLATED) as myzip:
	myzip.write('1.png')
	myzip.write('2.png')
	myzip.write('3.png')
	myzip.write('4.png')


# myzip.write('1.png')
# myzip.write('2.png')
# myzip.write('3.png')
# myzip.write('4.png')

# myzip.close()

# with zipfile.ZipFile('pngs.zip', 'r') as myzip:
# 	# print(myzip.namelist())  
# 	# myzip.extractall('files')
# 	myzip.extract('1.png')

# import os
# print(os.getcwd())


# Create Using ```SHUTIL```
# shutil.make_archive('another', 'zip', "files")
# shutil.make_archive('another', 'gztar', "files")

# Rxtract zip[Compressed] file using ```SHUTIL```
# shutil.unpack_archive('another.zip', 'another')

'''
* Type of ZIP files
	* zip: 	ZIP file
	* tar: 	Uncompressed tar File
	* gztar:  gzip'ed tar file
	* bztar:  bzip2'ed tar file
	* xztar:  xz'ed tar file
'''

url = 'https://github.com/CoreyMSchafer/dotfiles/archive/master.zip'

r = requests.get(url)
# print(r.content)

with open('dotfile.zip', 'wb') as f:
	f.write(r.content)

with zipfile.ZipFile('dotfile.zip', 'r') as myzip:
	print(myzip.namelist())