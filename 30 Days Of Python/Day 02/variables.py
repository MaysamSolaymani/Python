
# Variables in Python

first_name = 'Maysam'
last_name = 'Solaymani'
country = 'Iran'
city = 'Amol'
age = 38
is_married = True
skills = ['Java', 'SQL', 'C#', 'Python']
person_info = {
    'firstname':'Maysam', 
    'lastname':'Solaymani', 
    'country':'Iran',
    'city':'Amol'
    }
# Printing the values stored in the variables
print('First name:', first_name)
print('First name length:', len(first_name))
print('Last name: ', last_name)
print('Last name length: ', len(last_name))
print('Country: ', country)
print('City: ', city)
print('Age: ', age)
print('Married: ', is_married)
print('Skills: ', skills)
print('Person information: ', person_info)

# Declaring multiple variables in one line

first_name, last_name, country, age, is_married = 'Maysam', 'Solaymani', 'Iran', 38, True

print(first_name, last_name, country, age, is_married)
print('First name:', first_name)
print('Last name: ', last_name)
print('Country: ', country)
print('Age: ', age)
print('Married: ', is_married)
