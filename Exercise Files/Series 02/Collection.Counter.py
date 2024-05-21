from collections import Counter


for item, value in Counter.__dict__.items():
    print(item, value)

c = Counter('abcdeabcdabcaba')       # count elements from a string
print(c.most_common(3))              # three most common elements
print(sorted(c))                     # list all unique elements
print(''.join(sorted(c.elements()))) # list elements with repetitions
print(['a'])                         # count of letter 'a'
print(c['b'])
del c['b']                           # remove all 'b'
print(c['b'])
c.clear()                            # empty the counter
print(c)