# ZIP Module
* Type of ZIP files
	* zip: 	ZIP file
	* tar: 	Uncompressed tar File
	* gztar:  gzip'ed tar file
	* bztar:  bzip2'ed tar file
	* xztar:  xz'ed tar file
	* Many More

### Import Packages
```
import zipfile
import shutil
import requests
import os
``` 
### Creating a ZIP file Manually With `write` method
```
myzip =  zipfile.ZipFile('pngs.zip', 'w')

myzip.write('1.png')
myzip.write('2.png')
myzip.write('3.png')
myzip.write('4.png')

# close zip file
myzip.close()
```

### Creating ZIP file with context manager
```
myzip =  zipfile.ZipFile('pngs.zip', 'w')
with zipfile.ZipFile('pngs.zip', 'w', compression=zipfile.ZIP_DEFLATED) as myzip:
	myzip.write('1.png')
	myzip.write('2.png')
	myzip.write('3.png')
	myzip.write('4.png')

```
To compress the zip file we can add a parameter `compression=zipfile.ZIP_DEFLATED`.

In context manager we don't have to close the zip file as it do it by default.

### List the content of the ZIP file
```
with zipfile.ZipFile('pngs.zip', 'r') as myzip:
	print(myzip.namelist()) 
```

### Extracting ZIP file (All Files)
```
with zipfile.ZipFile('pngs.zip', 'r') as myzip:
	myzip.extractall('files')
```
### Extracting Specific file
```
with zipfile.ZipFile('pngs.zip', 'r') as myzip:
	myzip.extract('1.png')
```

### Create ZIP using ```SHUTIL``` library
```
# shutil.make_archive('resultzipname', 'FileType', "directoryName")
shutil.make_archive('another', 'zip', "files")
shutil.make_archive('another', 'gztar', "files")
```
### Creating ZIP file after getting Response from web
```
url = 'https://github.com/ashutosh4336/axios/archive/master.zip'

r = requests.get(url)
# print(r.content)

with open('dotfile.zip', 'wb') as f:
	f.write(r.content)

with zipfile.ZipFile('dotfile.zip', 'r') as myzip:
	print(myzip.namelist())
```
While Opening `dotfile.zip` the mode is `wb` where `w` represents `write` and `b` represents `bytes`