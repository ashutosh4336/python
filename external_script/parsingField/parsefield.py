import csv

htmloutput = ''
names = []

with open('rawdata200.csv', 'r') as csvfile:
    csvreader = csv.DictReader(csvfile)
    next(csvreader)

    for line in csvreader:
        # print(f"{line['First Name']} {line['Last Name']}")
        names.append(f"{line['First Name']} {line['Last Name']}")

# print(names)
# for name in names:
#     print(name)

htmloutput += f'<p> There are currently {len(names)} People in Washington DC. Thank You...</p>'
htmloutput += '\n<ul>'

for name in names:
    htmloutput += f'\n\t<li>{name}</li>'

htmloutput += '\n</ul>'
print(htmloutput)
