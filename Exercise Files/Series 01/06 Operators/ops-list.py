def main():
    list = [1,2,3,4,5,6,7,8,9,10]
    print(list)
    list.append(11)
    print(list)
    list[10] = 12
    print(list)
    print(list[3:7])
    new_list = []
    new_list[:] = range(20)
    print(new_list)
    print(new_list[1:20:3])
    new_list[1:20:4] = ('hi', 'this', 'is', 'a', 'string')
    print(new_list)

if __name__ == "__main__":
    main()
