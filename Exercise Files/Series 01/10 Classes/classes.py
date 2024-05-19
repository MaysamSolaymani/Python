class Duck:
    def __init__(self, **kwargs):
        self.val = kwargs

    def get_value(self, k):
        return self.val[k]

    def set_value(self, key, val):
        self.val[key] = val

def main():
    donald = Duck()
    donald.set_value('number', 30)
    donald.set_value('color', 'red')
    print(donald.get_value('number'))
    print(donald.get_value('color'))

if __name__ == "__main__":
    main()
