# Inbuilt CSV Reader Python

### Import Package


```python
import csv
import os
```

### Read File


```python
# os.listdir()



with open('new_name.csv', 'r') as f:
    csvread = csv.reader(f, delimiter='\t')
    
    for line in csvread:
        print(line)

```

### Read and Write to Another File


```python

with open('names.csv', 'r') as csvfile:
    csvReader = csv.reader(csvfile) 
    
#     title = next(csvReader) 
    with open('new_name.csv', 'w') as f:
        csvWriter = csv.writer(f, delimiter='\t')
        for line in csvReader:
#             print(line[2])
            csvWriter.writerow(line)
```

### Read CSV file with `DictReader()` method


```python
with open('names.csv', 'r') as csvfile:
    csvreader = csv.DictReader(csvfile)
    
    for line in csvreader:
        print(line['email'])
```

    john-doe@bogusemail.com
    maryjacobs@bogusemail.com
    davesmith@bogusemail.com
    janestuart@bogusemail.com
    tomwright@bogusemail.com
    steverobinson@bogusemail.com
    nicolejacobs@bogusemail.com
    janewright@bogusemail.com
    janedoe@bogusemail.com
    kurtwright@bogusemail.com
    kurtrobinson@bogusemail.com
    janejenkins@bogusemail.com
    neilrobinson@bogusemail.com
    tompatterson@bogusemail.com
    samjenkins@bogusemail.com
    stevestuart@bogusemail.com
    maggiepatterson@bogusemail.com
    maggiestuart@bogusemail.com
    janedoe@bogusemail.com
    stevepatterson@bogusemail.com
    davesmith@bogusemail.com
    samwilks@bogusemail.com
    kurtjefferson@bogusemail.com
    samstuart@bogusemail.com
    janestuart@bogusemail.com
    davedavis@bogusemail.com
    sampatterson@bogusemail.com
    tomjefferson@bogusemail.com
    janestuart@bogusemail.com
    maggiejefferson@bogusemail.com
    marywilks@bogusemail.com
    neilpatterson@bogusemail.com
    coreydavis@bogusemail.com
    stevejacobs@bogusemail.com
    janejenkins@bogusemail.com
    johnjacobs@bogusemail.com
    neilsmith@bogusemail.com
    coreywilks@bogusemail.com
    coreysmith@bogusemail.com
    marypatterson@bogusemail.com
    janestuart@bogusemail.com
    travisarnold@bogusemail.com
    johnrobinson@bogusemail.com
    travisarnold@bogusemail.com


### Write CSV file with `DictReader()` method


```python
with open('names.csv', 'r') as csvfile:
    csvreader = csv.DictReader(csvfile)
    
    with open('new_names.csv', 'w') as newfile:
        fieldname = ['first_name', 'last_name', 'email']
        csvwriter = csv.DictWriter(newfile,fieldnames=fieldname, delimiter='\t')
        
        csvwriter.writeheader()
        
        for line in csvreader:
            csvwriter.writerow(line)
```

### Delete a field and write to file with `DictReader()` method


```python
with open('names.csv', 'r') as csvfile:
    csvreader = csv.DictReader(csvfile)
    
    with open('new_names.csv', 'w') as newfile:
        fieldname = ['first_name', 'last_name']
        csvwriter = csv.DictWriter(newfile, fieldnames=fieldname, delimiter='\t')
        
        csvwriter.writeheader()
        
        for line in csvreader:
            del line['email']
            csvwriter.writerow(line)
```
