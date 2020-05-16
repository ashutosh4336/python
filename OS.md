# OS Module

# Imports

```
from datetime import datetime
import os
```

### Different Methods of `OS` Module

```
print(help(os))
print(dir(os))
```

### Get Current Working Directory

`print(os.getcwd())`

### Change Working Directory

`os.chdir('/home/User/Desktop/')`

### List Content of Current Directory

`print(os.listdir())`

### Create a Directory

````

os.makedirs('osMod/videoOne')

--> Can't directory inside a directory

os.makedir('osMod')

```

### Delete a Directory

`os.removedirs('osMode/videoOne')`

### Rename a file

`os.rename('cat.png', 'dog.png')`

### Last Modified Time / Access Time / Change Time

```

modTime = os.stat('file').st_mtime
print(datetime.fromtimestamp(modTime)) [DateTime Module is Needed]

```

### Tree Structure File Listing for Current Directory

```

for dirpath, dirname, filename, in os.walk(os.getcwd()):
print('dirpath --> {}'.format(dirpath))
print('dirname --> {}'.format(dirname))
print('Filename --> {}'.format(filename))
print(' ')
print(' ')

```

### Console Env Variables

```

print(os.environ.get('GOPATH'))

```

### Creating a Document (Text) File with the ENV path and NAME

```

filePath = os.environ.get('GOPATH') + '.txt'
fileName = filePath.split('/')[-1]

# print(type(filePath), filePath)

# print(fileName)

with open(fileName, 'w') as f:
f.write(os.environ.get('GOPATH') + '\n')

```

# `OS.PATH` Module file operation

`print(dir(os.path))`

### Print File name

```

print(os.path.basename('/home/ashutosh/Desktop/go.txt'))

```

### Print Directory Path containing the file

```

print(os.path.dirname('/home/ashutosh/Desktop/go.txt'))

```

### Print Direct and File Name Separately in a Tuple

```

print(os.path.split('/home/ashutosh/Desktop/go.txt'))

```

### Check if File Exist or Not

```

print(os.path.exists('/home/ashutosh/Desktop/go.txt'))

```

### Check the input data is a Directory or File

```

print(os.path.isdir('/home/ashutosh/Desktop/go.txt'))
print(os.path.isfile('/home/ashutosh/Desktop/go.txt'))

```

```

print(os.path.splitext('/home/ashutosh/Desktop/go.txt'))
Output : ('/home/ashutosh/Desktop/go', '.txt')

```

```
````
