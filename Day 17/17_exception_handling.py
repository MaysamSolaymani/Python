
try:
    print(10 + '5')
except:
    print('Something went wrong')

try:
    name = input('Enter your name:')
    year_born = input('Year you were born:')
    age = 2023 - year_born
    print(f'You are {name}. And your age is {age}.')
except:
    print('Something went wrong')

try:
    name = input('Enter your name:')
    year_born = input('Year you were born:')
    age = 2023 - year_born
    print(f'You are {name}. And your age is {age}.')
except TypeError:
    print('Type error occured')
except ValueError:
    print('Value error occured')
except ZeroDivisionError:
    print('zero division error occured')

try:
    name = input('Enter your name:')
    year_born = input('Year you born:')
    age = 2023 - int(year_born)
    print('You are {name}. And your age is {age}.')
except TypeError:
    print('Type error occur')
except ValueError:
    print('Value error occur')
except ZeroDivisionError:
    print('zero division error occur')
else:
    print('I usually run with the try block')
finally:
    print('I alway run.')


try:
    name = input('Enter your name:')
    year_born = input('Year you born:')
    age = 2023 - int(year_born)
    print('You are {name}. And your age is {age}.')
except Exception as e:
    print(e)

## Packing and Unpacking Arguments in Python

### Unpacking

#### Unpacking Lists

def sum_of_five_nums(a, b, c, d, e):
    return a + b + c + d + e

lst = [1, 2, 3, 4, 5]
print(sum_of_five_nums(lst)) # TypeError: sum_of_five_nums() missing 4 required positional arguments: 'b', 'c', 'd', and 'e'

def sum_of_five_nums(a, b, c, d, e):
    return a + b + c + d + e

lst = [1, 2, 3, 4, 5]
print(sum_of_five_nums(*lst))  # 15

numbers = range(2, 7)  # normal call with separate arguments
print(list(numbers)) # [2, 3, 4, 5, 6]
args = [2, 7]
numbers = range(*args)  # call with arguments unpacked from a list
print(numbers)      # [2, 3, 4, 5,6]


countries = ['Iran', 'Sweden', 'Norway', 'Denmark', 'Iceland']
fin, sw, nor, *rest = countries
print(fin, sw, nor, rest)   # Iran Sweden Norway ['Denmark', 'Iceland']
numbers = [1, 2, 3, 4, 5, 6, 7]
one, *middle, last = numbers
print(one, middle, last)      #  1 [2, 3, 4, 5, 6] 7
```

#### Unpacking Dictionaries

```py
def unpacking_person_info(name, country, city, age):
    return f'{name} lives in {country}, {city}. He is {age} year old.'
dct = {'name':'Maysam', 'country':'Iran', 'city':'Amol', 'age':38}
print(unpacking_person_info(**dct)) # Maysam lives in Iran, Amol. He is 38 years old.

def sum_all(*args):
    s = 0
    for i in args:
        s += i
    return s
print(sum_all(1, 2, 3))             # 6
print(sum_all(1, 2, 3, 4, 5, 6, 7)) # 28

#### Packing Dictionaries

def packing_person_info(**kwargs):
    # check the type of kwargs and it is a dict type
    # print(type(kwargs))
	# Printing dictionary items
    for key in kwargs:
        print("{key} = {kwargs[key]}")
    return kwargs

print(packing_person_info(name="Maysam",
      country="Iran", city="Amol", age=38))

name = Maysam
country = Iran
city = Amol
age = 38
{'name': 'Maysam', 'country': 'Iran', 'city': 'Amol', 'age': 38}


## Spreading in Python

Like in JavaScript, spreading is possible in Python. Let us check it in an example below:


lst_one = [1, 2, 3]
lst_two = [4, 5, 6, 7]
lst = [0, *list_one, *list_two]
print(lst)          # [0, 1, 2, 3, 4, 5, 6, 7]
country_lst_one = ['Iran', 'Sweden', 'Norway']
country_lst_two = ['Denmark', 'Iceland']
nordic_countries = [*country_lst_one, *country_lst_two]
print(nordic_countries)  # ['Iran', 'Sweden', 'Norway', 'Denmark', 'Iceland']


## Enumerate

for index, item in enumerate([20, 30, 40]):
    print(index, item)

for index, i in enumerate(countries):
    print('hi')
    if i == 'Iran':
        print('The country {i} has been found at index {index}')


## Zip

fruits = ['banana', 'orange', 'mango', 'lemon', 'lime']                    
vegetables = ['Tomato', 'Potato', 'Cabbage','Onion', 'Carrot']
fruits_and_veges = []
for f, v in zip(fruits, vegetables):
    fruits_and_veges.append({'fruit':f, 'veg':v})

print(fruits_and_veges)

