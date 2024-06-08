def funcOne():
    index = 1
    print(locals())
    
def funcTwo(new):
    print(globals())

def func(name='name'):

    def t1():
        return 't1'
    def t2(text):
        return 't2' + text
    if name == 'main':
        return t1()
    else:
        return t2

if __name__ == '__main__':
    '''funcOne()
    funcTwo('new')
    objFunc = funcTwo
    print(objFunc('two'))
    del funcTwo
    objFunc('three')'''
    #print(funcTwo('t'))
    f = func()
    print(f('tr'))

