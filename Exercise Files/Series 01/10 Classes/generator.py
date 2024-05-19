class inclusive_range:
    def __init__(self, *args):
        self.len = len(args)
        if self.len < 1:
            raise TypeError('insert at least one argument')
        elif self.len == 1:
            self.stop = args[0]
            self.start = 1
            self.step = 1
        elif self.len == 2:
            (self.start, self.stop) = args
        elif self.len == 3:
            (self.start, self.stop, self.step) = args
        else:
            raise TypeError('insert most 3 args not {} args'.format(self.len))
    def __iter__(self):
        i = 1
        while i <= self.stop:
            yield i
            i += self.step

def main():
    o = range(25)
    for i in o: print(i, end = ' ')
    print()
    for ind in inclusive_range(5, 30, 7):
        print(ind, end= ' ')

if __name__ == "__main__":
    main()
