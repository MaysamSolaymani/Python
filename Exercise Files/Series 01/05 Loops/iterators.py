def main():
    str = 'this is a text'
    for index, value in enumerate(str):
        if value == 't':
            print('index {} of t is'.format(index))

if __name__ == "__main__":
    main()
