
# Syntax
open('filename', mode) # mode(r, a, w, x, t,b)  could be to read, write, update


- "r" - Read - Default value. Opens a file for reading, it returns an error if the file does not exist
- "a" - Append - Opens a file for appending, creates the file if it does not exist
- "w" - Write - Opens a file for writing, creates the file if it does not exist
- "x" - Create - Creates the specified file, returns an error if the file exists
- "t" - Text - Default value. Text mode
- "b" - Binary - Binary mode (e.g. images)

### Opening Files for Reading

f = open('./files/reading_file_example.txt')
print(f) # <_io.TextIOWrapper name='./files/reading_file_example.txt' mode='r' encoding='UTF-8'>

f = open('./files/reading_file_example.txt')
txt = f.read()
print(type(txt))
print(txt)
f.close()

# output
<class 'str'>
This is an example to show how to open a file and read.
This is the second line of the text.

f = open('./files/reading_file_example.txt')
txt = f.read(10)
print(type(txt))
print(txt)
f.close()


```sh
# output
<class 'str'>
This is an

f = open('./files/reading_file_example.txt')
line = f.readline()
print(type(line))
print(line)
f.close()

# output
<class 'str'>
This is an example to show how to open a file and read.

f = open('./files/reading_file_example.txt')
lines = f.readlines()
print(type(lines))
print(lines)
f.close()

# output
<class 'list'>
['This is an example to show how to open a file and read.\n', 'This is the second line of the text.']


f = open('./files/reading_file_example.txt')
lines = f.read().splitlines()
print(type(lines))
print(lines)
f.close()

# output
<class 'list'>
['This is an example to show how to open a file and read.', 'This is the second line of the text.']

with open('./files/reading_file_example.txt') as f:
    lines = f.read().splitlines()
    print(type(lines))
    print(lines)

# output
<class 'list'>
['This is an example to show how to open a file and read.', 'This is the second line of the text.']

### Opening Files for Writing and Updating

- "a" - append - will append to the end of the file, if the file does not it creates a new file.
- "w" - write - will overwrite any existing content, if the file does not exist it creates.

Let us append some text to the file we have been reading:

with open('./files/reading_file_example.txt','a') as f:
    f.write('This text has to be appended at the end')

with open('./files/writing_file_example.txt','w') as f:
    f.write('This text will be written in a newly created file')

### Deleting Files

import os
os.remove('./files/example.txt')

import os
if os.path.exists('./files/example.txt'):
    os.remove('./files/example.txt')
else:
    print('The file does not exist')

## File Types

### File with txt Extension

### File with json Extension

# dictionary
person_dct= {
    "name":"Maysam",
    "country":"Iran",
    "city":"Amol",
    "skills":["JavaScrip", "React","Python"]
}
# JSON: A string form a dictionary
person_json = "{'name': 'Maysam', 'country': 'Iran', 'city': 'Amol', 'skills': ['JavaScrip', 'React', 'Python']}"

# we use three quotes and make it multiple line to make it more readable
person_json = '''{
    "name":"Maysam",
    "country":"Iran",
    "city":"Amol",
    "skills":["JavaScrip", "React","Python"]
}'''

### Changing JSON to Dictionary

import json
# JSON
person_json = '''{
    "name": "Maysam",
    "country": "Iran",
    "city": "Amol",
    "skills": ["JavaScrip", "React", "Python"]
}'''

# let's change JSON to dictionary
person_dct = json.loads(person_json)
print(type(person_dct))
print(person_dct)
print(person_dct['name'])

# output
<class 'dict'>
{'name': 'Maysam', 'country': 'Iran', 'city': 'Amol', 'skills': ['JavaScrip', 'React', 'Python']}
Maysam


### Changing Dictionary to JSON

import json
# python dictionary
person = {
    "name": "Maysam",
    "country": "Iran",
    "city": "Amol",
    "skills": ["JavaScrip", "React", "Python"]
}
# let's convert it to  json
person_json = json.dumps(person, indent=4) # indent could be 2, 4, 8. It beautifies the json
print(type(person_json))
print(person_json)

# output
# when you print it, it does not have the quote, but actually it is a string
# JSON does not have type, it is a string type.
<class 'str'>
{
    "name": "Maysam",
    "country": "Iran",
    "city": "Amol",
    "skills": [
        "JavaScrip",
        "React",
        "Python"
    ]
}

### Saving as JSON File

import json
# python dictionary
person = {
    "name": "Maysam",
    "country": "Iran",
    "city": "Amol",
    "skills": ["JavaScrip", "React", "Python"]
}
with open('./files/json_example.json', 'w', encoding='utf-8') as f:
    json.dump(person, f, ensure_ascii=False, indent=4)

### File with csv Extension

import csv
with open('./files/csv_example.csv') as f:
    csv_reader = csv.reader(f, delimiter=',') # w use, reader method to read csv
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are :{", ".join(row)}')
            line_count += 1
        else:
            print(
                f'\t{row[0]} is a teachers. He lives in {row[1]}, {row[2]}.')
            line_count += 1
    print(f'Number of lines:  {line_count}')


### File with xlsx Extension

import xlrd
excel_book = xlrd.open_workbook('sample.xls)
print(excel_book.nsheets)
print(excel_book.sheet_names)

### File with xml Extension

<?xml version="1.0"?>
<person gender="male">
  <name>Maysam</name>
  <country>Iran</country>
  <city>Amol</city>
  <skills>
    <skill>JavaScrip</skill>
    <skill>React</skill>
    <skill>Python</skill>
  </skills>
</person>

import xml.etree.ElementTree as ET
tree = ET.parse('./files/xml_example.xml')
root = tree.getroot()
print('Root tag:', root.tag)
print('Attribute:', root.attrib)
for child in root:
    print('field: ', child.tag)

# output
Root tag: person
Attribute: {'gender': 'male'}
field: name
field: country
field: city
field: skills
