def main():
    x = [1,5,8,6,7]
    x.append(9)
    x.insert(0,'t')
    print(type(x), x)
    dic = {'first': 1, 'second': 2, 'third':3, 'forth':4}
    for key in dic:
        print(key, dic[key])

if __name__ == "__main__":
    main()
