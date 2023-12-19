from datetime import datetime, date, time
def main():
    print('B')
def t():
    print('Bwww')
if __name__ == "__main__":
    main()
    t()
val = 1
print(val)
del val
del t
#t()

#####################
a, b = 1,2
print('a is greater than b' if a > b else 'a is less than b or equal b')
#####################
for x in range(5,20,3):
    print(x)
#####################
mylist = ['a', 'b', 'c', 'd']
for a, b in enumerate(mylist):
    print(a, b)
#####################
class firstClass():
    def __init__(self):
        pass
    def methodOne(self):
        return 1
    def methodTwo(self):
        return 2
class secondClass(firstClass):
    def __init__(self):
        pass
    def methodOne(self):
        return 'one'
    def methodTwo(self):
        return 'Two'
f = firstClass()
s = secondClass()
print(f.methodOne())
print(f.methodTwo())
print(s.methodOne())
print(s.methodTwo())
###########################################
today = date.today()
print(today, today.year)
now = datetime.now()
print(now.strftime('%c-%a-%A-%b-%B-%d-%D-%m-%y-%Y-%m'))
###########################################
