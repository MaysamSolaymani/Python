
empty_tuple = ()
# or using the tuple constructor
_empty_tuple = tuple()


tpl = ('item1', 'item2','item3')
fruits = ('banana', 'orange', 'mango', 'lemon')
len(tpl)

first_item = tpl[0]
second_item = tpl[1]

first_fruit = fruits[0]
second_fruit = fruits[1]
last_index =len(fruits) - 1
last_fruit = fruits[las_index]


first_item = tpl[-4]
second_item = tpl[-3]

first_fruit = fruits[-4]
second_fruit = fruits[-3]
last_fruit = fruits[-1]

### Slicing tuples

all_items = tpl[0:4]         # all items
all_items = tpl[0:]         # all items
middle_two_items = tpl[1:3]  # does not include item at index 3


all_fruits = fruits[0:4]    # all items
all_fruits= fruits[0:]      # all items
orange_mango = fruits[1:3]  # doesn't include item at index 3
orange_to_the_rest = fruits[1:]

all_items = tpl[-4:]         # all items
middle_two_items = tpl[-3:-1]  # does not include item at index 3 (-1)

all_fruits = fruits[-4:]    # all items
orange_mango = fruits[-3:-1]  # doesn't include item at index 3
orange_to_the_rest = fruits[-3:]

### Changing Tuples to Lists

fruits = list(fruits)
fruits[0] = 'apple'
print(fruits)     # ['apple', 'orange', 'mango', 'lemon']
fruits = tuple(fruits)
print(fruits)     # ('apple', 'orange', 'mango', 'lemon')

### Checking an Item in a Tuple

We can check if an item exists or not in a tuple using _in_, it returns a boolean.

print('orange' in fruits) # True
print('apple' in fruits) # False
fruits[0] = 'apple' # TypeError: 'tuple' object does not support item assignment

### Joining Tuples

fruits = ('banana', 'orange', 'mango', 'lemon')
vegetables = ('Tomato', 'Potato', 'Cabbage','Onion', 'Carrot')
fruits_and_vegetables = fruits + vegetables

### Deleting Tuples

fruits = ('banana', 'orange', 'mango', 'lemon')
del fruits

