class Generate:
    def __init__(self, start, stop, step):
        self.start = start
        self.stop = stop
        self.step = step
        for i in self.incude_range(self.start, self.stop, self.step):
            print(i, end=' ')

    def incude_range(self, start, stop, step):
        self.index = start
        while self.index <= stop:
            yield self.index
            self.index += step

if __name__ == "__main__":
    gen = Generate(1, 25, 2)
