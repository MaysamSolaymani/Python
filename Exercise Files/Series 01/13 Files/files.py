def main():
    buffersize = 40000
    fin = open('lines.txt', 'r')
    fout = open('new.txt', 'w')
    buffer = fin.read(buffersize)
    while len(buffer):
        fout.write(buffer)
        buffer = fin.readlines(buffersize)
    buffersize = 40000
    fin = open('olives.jpg', 'rb')
    fout = open('newolives.jpg', 'wb')
    buffer = fin.read(buffersize)
    while len(buffer):
        fout.write(buffer)
        buffer = fin.readlines(buffersize)

if __name__ == "__main__":
    main()
