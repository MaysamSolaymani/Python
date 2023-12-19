
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

a, b = 1,2
print('a is greater than b' if a > b else 'a is less than b or equal b')