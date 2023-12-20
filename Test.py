import urllib
from datetime import datetime, date, time
import os
from os import path
import urllib.request
import json

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
for x in range(5,20,4):
    print(x)
#####################
mylist = ['a', 'b', 'c', 'd']
for a, b in enumerate(mylist):
    print(a, b)
#####################
class firstClass():
    def __init__(self, value='100'):
        self._v = value
        pass
    def methodOne(self):
        print(1)
    def methodTwo(self):
        return 2
    def get_value(self):
        return self._v
class secondClass(firstClass):
    def __init__(self):
        pass
    def methodOne(self):
        super().methodOne()
        return 'one'
    def methodTwo(self):
        return 'Two'
s = secondClass()
print(s.methodOne())
print(s.methodTwo())
###########################################
today = date.today()
print(today, today.year)
now = datetime.now()
print(now.strftime('%c-%a-%A-%b-%B-%d-%D-%m-%y-%Y-%m'))
###########################################
'''f = open('test.dat','w+')
f.write('test\nnew line')
f.close()
n = open('test.dat', 'a+')
n.write('\r\nappend line here')
n.close()
r = open('test.dat','r')
index = 1
for x in r.readlines():
    print(str(index) + ': ' + x)
    index = index + 1
r.close()'''
###########################################
print(os.name)
print(path)
print(path.exists("test.dat"))
print(path.isfile("test.dat"))
print(path.isdir("test.dat"))
print(path.realpath("test.dat"))
#########################################
'''
request_url = urllib.request.urlopen('http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_day.geojson')
print(request_url.getcode())
data = request_url.read()
theJson = json.loads(data)
print(theJson['metadata'])
for x in theJson['features']:
    print(x['properties']['place'])'''
#########################################


