def do_twice(func):
    def wrapper_do_twice(*args, **kwargs):
        func(*args, **kwargs)
        print(type(args))
        print(type(kwargs))
        func(*args, **kwargs)
    return wrapper_do_twice