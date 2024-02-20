import csv
import os

origfilepath = os.path.join('data', 'airqorig.csv')
origfile = open(origfilepath, 'r', encoding = 'utf-8')
semicleanpath = os.path.join('data', 'semiclean_data.csv')
semicleanfile = open(semicleanpath, 'w', encoding = 'utf-8')

data = []

with origfile as csv_file:
    reader = csv.reader(csv_file)
    for row in reader:
        data.append(row)

# Checking redundancy of rows through Unique ID; done to double check if I could get rid of Unique ID column

'''
unique = []
for i in data:
    if i[0] not in unique:
        unique.append(i[0])

if len(unique) == len(data):
    print("None of the rows are redundant!")
else:
    print("Uh oh... you might want to check for redundancy and drop some rows.")
'''


# Write a function to remove columns: Unique ID, Indicator ID, Geo Type Name, Geo Type ID, Message
removeindex = [0,1,5,6,11]
def removecol(line):
    for i in sorted(removeindex, reverse = True):
        del line[i] # Reverse index order so they don't interfere with one another
    line = ",".join(line) + '\n'
    return line

# Checking unique data values in the pollutant column
'''
unique = []
for i in data:
    if i[0] not in unique:
        unique.append(i[0])

for i in unique:
    print(i)
'''

# Remove rows that include categorical data and use the column-removing function to write new file
wanteddata = ['Name', 'Nitrogen dioxide (NO2)', 'Fine particles (PM 2.5)', 'Ozone (O3)']
for i in data:
    if i[2] in wanteddata:
        semicleanfile.write(removecol(i))
    else:
        continue


# Reading semi-clean data file
readsemicleanfile = open(semicleanpath, 'r', encoding = 'utf-8')
newdata = []

with readsemicleanfile as csv_file:
    reader = csv.reader(csv_file)
    for row in reader:
        newdata.append(row)

# Checking redundancy of Measure and Measure Info; done to double check if I could get rid of them
'''
unique = []
for i in newdata:
    if i[2] not in unique:
        unique.append(i[2])

print(unique)
'''

newdata[0][-1] = "Data Value(Mean)"

cleanpath = os.path.join('data', 'clean_data.csv')
cleanfile = open(cleanpath, 'w', encoding = 'utf-8')

# Get rid of Measure Info column to finalize clean_data.csv

removeindex = [1]

for i in newdata:
    cleanfile.write(removecol(i))

origfile.close()
semicleanfile.close()
cleanfile.close()