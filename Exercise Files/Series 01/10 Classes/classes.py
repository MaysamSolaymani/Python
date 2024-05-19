class Duck:
    def __init__(self, value):
        self.val = value

    def quack(self):
        print('Quaaack! {}'.format(self.val))

    def walk(self):
        print('Walks like a duck. {}'.format(self.val))

def main():
    donald = Duck(50)
    donald.quack()
    donald.walk()

if __name__ == "__main__":
    main()
