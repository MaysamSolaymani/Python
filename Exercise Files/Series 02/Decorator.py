def decorator(func):
    def changefunc():
        print('new string before change \'{}\''.format(func.__name__))
        func()
        print('\'{}\' changed'.format(func.__name__))
    return changefunc


@decorator
def func():
    print('test decorator')
func()
