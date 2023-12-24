import sqlite3
from decorators import do_twice

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