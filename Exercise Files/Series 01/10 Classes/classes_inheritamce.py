class Person:
    def __init__(self):
        print('initialize person')

    def get_profile(self):
        return 'this is a person'

class Employee(Person):

    def __init__(self):
        print(super().get_profile())
        print('this is an employee after a person')

class supervisor(Employee):
    pass


def main():
    donald = Employee()
    sup = supervisor()


if __name__ == "__main__":
    main()
