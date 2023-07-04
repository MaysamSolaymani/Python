Maysam@Maysam:~$ python
Python 3.9.6 (default, July 28 2023, 15:26:21)
[Clang 11.0.0 (clang-1100.0.33.8)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> num = 10
>>> type(num)
<class 'int'>
>>> string = 'string'
>>> type(string)
<class 'str'>
>>> boolean = True
>>> type(boolean)
<class 'bool'>
>>> lst = []
>>> type(lst)
<class 'list'>
>>> tpl = ()
>>> type(tpl)
<class 'tuple'>
>>> set1 = set()
>>> type(set1)
<class 'set'>
>>> dct = {}
>>> type(dct)
<class 'dict'>


### Creating a Class


# syntax
class ClassName:
  code goes here


class Person:
  pass
print(Person)

<__main__.Person object at 0x10804e510>

### Creating an Object

p = Person()
print(p)

### Class Constructor

class Person:
      def __init__ (self, name):
        # self allows to attach parameter to the class
          self.name =name

p = Person('Maysam')
print(p.name)
print(p)


# output
Maysam
<__main__.Person object at 0x2abf46907e80>

class Person:
      def __init__(self, firstname, lastname, age, country, city):
          self.firstname = firstname
          self.lastname = lastname
          self.age = age
          self.country = country
          self.city = city


p = Person('Maysam', 'Solaymani', 38, 'Iran', 'Amol')
print(p.firstname)
print(p.lastname)
print(p.age)
print(p.country)
print(p.city)

# output
Maysam
Solaymani
38
Iran
Amol

### Object Methods

class Person:
      def __init__(self, firstname, lastname, age, country, city):
          self.firstname = firstname
          self.lastname = lastname
          self.age = age
          self.country = country
          self.city = city
      def person_info(self):
        return f'{self.firstname} {self.lastname} is {self.age} years old. He lives in {self.city}, {self.country}'

p = Person('Maysam', 'Solaymani', 38, 'Iran', 'Amol')
print(p.person_info())


# output
Maysam Solaymani is 38 years old. He lives in Amol, Iran

### Object Default Methods

class Person:
      def __init__(self, firstname='Maysam', lastname='Solaymani', age=38, country='Iran', city='Amol'):
          self.firstname = firstname
          self.lastname = lastname
          self.age = age
          self.country = country
          self.city = city

      def person_info(self):
        return f'{self.firstname} {self.lastname} is {self.age} years old. He lives in {self.city}, {self.country}.'

p1 = Person()
print(p1.person_info())
p2 = Person('John', 'Doe', 38, 'Nomanland', 'Noman city')
print(p2.person_info())

# output
Maysam Solaymani is 38 years old. He lives in Amol, Iran.
John Doe is 38 years old. He lives in Noman city, Nomanland.


### Method to Modify Class Default Values

class Person:
      def __init__(self, firstname='Maysam', lastname='Solaymani', age=38, country='Iran', city='Amol'):
          self.firstname = firstname
          self.lastname = lastname
          self.age = age
          self.country = country
          self.city = city
          self.skills = []

      def person_info(self):
        return f'{self.firstname} {self.lastname} is {self.age} years old. He lives in {self.city}, {self.country}.'
      def add_skill(self, skill):
          self.skills.append(skill)

p1 = Person()
print(p1.person_info())
p1.add_skill('HTML')
p1.add_skill('CSS')
p1.add_skill('JavaScript')
p2 = Person('John', 'Doe', 38, 'Nomanland', 'Noman city')
print(p2.person_info())
print(p1.skills)
print(p2.skills)

# output
Maysam Solaymani is 38 years old. He lives in Amol, Iran.
John Doe is 38 years old. He lives in Noman city, Nomanland.
['HTML', 'CSS', 'JavaScript']
[]


### Inheritance

class Student(Person):
    pass


s1 = Student('Maysam', 'Solaymani', 38, 'Iran', 'Amol')
s2 = Student('Mona', 'Hedayati', 28, 'Iran', 'Espoo')
print(s1.person_info())
s1.add_skill('JavaScript')
s1.add_skill('React')
s1.add_skill('Python')
print(s1.skills)

print(s2.person_info())
s2.add_skill('Organizing')
s2.add_skill('Marketing')
s2.add_skill('Digital Marketing')
print(s2.skills)


output
Maysam Solaymani is 38 years old. He lives in Amol, Iran.
['JavaScript', 'React', 'Python']
Mona Hedayati is 28 years old. He lives in Espoo, Iran.
['Organizing', 'Marketing', 'Digital Marketing']


### Overriding parent method

class Student(Person):
    def __init__ (self, firstname='Maysam', lastname='Solaymani',age=38, country='Iran', city='Amol', gender='male'):
        self.gender = gender
        super().__init__(firstname, lastname,age, country, city)
    def person_info(self):
        gender = 'He' if self.gender =='male' else 'She'
        return f'{self.firstname} {self.lastname} is {self.age} years old. {gender} lives in {self.city}, {self.country}.'

s1 = Student('Maysam', 'Solaymani', 38, 'Iran', 'Amol','male')
s2 = Student('Mona', 'Hedayati', 28, 'Iran', 'Amol', 'female')
print(s1.person_info())
s1.add_skill('JavaScript')
s1.add_skill('React')
s1.add_skill('Python')
print(s1.skills)

print(s2.person_info())
s2.add_skill('Organizing')
s2.add_skill('Marketing')
s2.add_skill('Digital Marketing')
print(s2.skills)

Maysam Solaymani is 38 years old. He lives in Amol, Iran.
['JavaScript', 'React', 'Python']
Mona Hedayati is 28 years old. She lives in Amol, Iran.
['Organizing', 'Marketing', 'Digital Marketing']
