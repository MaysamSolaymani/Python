def f():
    ls = [1,2,5,4,3]
    print(ls)
    for item in ls:
        assert item / 2

if __name__ == "__main__":
    f()