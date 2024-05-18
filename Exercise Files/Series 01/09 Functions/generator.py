def main():
    for i in range(25):
        print(i, end = ' ')
    print()
    for i in incude_range(0,25,1):
        print(i, end=' ')

def incude_range(start, stop, step):
    index = start
    while index <= stop:
        yield index
        index += step

if __name__ == "__main__":
    main()
