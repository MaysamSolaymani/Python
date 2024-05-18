def main():
    fh = open('lines.txt')
    for line in fh.readlines():
        print(line, end='')

if __name__ == "__main__":
    main()
