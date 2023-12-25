import sqlite3
from decorators import do_twice, timer
import turtle

class getIter():
    def __init__(self, *args):
        number = len(args)
        if number < 1:
            raise TypeError('insert at least two args')
        elif number == 2:
            self._start = args[0]
            self._end = args[1]
            self._step = 1
        elif number == 3:
            self._start = args[0]
            self._end = args[1]
            self._step = args[2]
        elif number > 3:
            raise TypeError('insert most 3 args')

    def __iter__(self):
        while self._start <= self._end:
            yield  self._start
            self._start = self._start + self._step

def main():
    db = sqlite3.connect('test.db')
    db.execute('drop table test')
    db.commit()
    db.execute('create table test ( id int )')
    db.commit()
    db.execute('insert into test select 1')
    db.commit()
    st = db.execute('select * from test').fetchall()
    db.commit()
    print(st)

if __name__ == '__main__':
    main()
    gi = getIter(1,20,3)
    for i in gi:
        print(i)

#############################################################
def shout(text):
    return text.upper()

def whisper(text):
    return text.lower()

def greet(func):
    greeting = func("""Hi, I am created by a function passed as an argument.""")
    print(greeting)

greet(shout)
greet(whisper)
#############################################################
def create_adder(x):
    def adder(y):
        return x + y
    return adder

add_15 = create_adder(15)
print(add_15(10))
#############################################################

@do_twice
def say_whee(keys):
    print(keys)

print(say_whee('meysam'))
print(help(say_whee))

@timer
def waste_some_time(num_times):
    for _ in range(num_times):
        sum([i**2 for i in range(10000)])

waste_some_time(100)

###################################################################
class Accolade:
    def __init__(self, function):
        self.function = function

    def __call__(self, name):
        # Adding Excellency before name
        name = "Excellency " + name
        self.function(name)
        # Saluting after the name
        print("Thanks " + name + " for gracing the occasion")


@Accolade
def simple_function(name):
    print(name)

simple_function('John McKinsey')
###############################################################################
from functools import lru_cache

@lru_cache(maxsize=128)
@timer
def factorial(n):
    return n * factorial(n-1) if n else 1

print(factorial(3))
###############################################################################
class Pencil:
    def __init__(self, count):
        self._counter = count

    @property
    def counter(self):
        return self._counter

    @counter.setter
    def counter(self, count):
        self._counter = count

    @counter.getter
    def counter(self):
        return self._counter

    def __call__(self, *args, **kwargs):
        print('you called me as a method')


HB = Pencil(100)
print(HB.counter)
HB.counter = 20
print(HB.counter)
# call Pencil as a method
print(HB())



