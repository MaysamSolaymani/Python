def main():
    validfunc()
    showNumber(1)
    showNumber(2,5)
    showNumber(1,2,41)
    func(1,2,3,4,5,6,7,8,9)
    withargs(1,2,3,4,5,6,one = 1, two = 2, three = 3)
    for i in withreturn(25):
        print(i, end=' ')

def showNumber(one, two=None, three=3):
    if two is None:
        two = 2
    print('one is {} and two is {} and three is {}'.format(one,two,three))

def withargs(this, that, others, *args, **kwargs):
    print(this, that, others, args, kwargs)
    for k in kwargs:
        print(k, kwargs[k])

def func(one, two, three, *args):
    print(one, two, three)
    print(one, two, three, args)
    for a in args:
        print(a, end=' ')

def withreturn(n):
    return range(n)

def validfunc():
    #Has to have at least one line
    pass

if __name__ == "__main__":
    main()
