def main():
    x = [1,5,8,6,7]
    x.append(9)
    x.insert(0,'t')
    print(type(x), x)
    dic = {'first': 1, 'second': 2, 'third':3, 'forth':4}
    for key in dic:
        print(key, dic[key])
    d = dict(one=1, two=2, three=3, four=4, five=5)
    for k in sorted(d):
        print(k, d[k])
    d['sex'] = 6
    for k in sorted(d):
        print(k, d[k])

if __name__ == "__main__":
    main()
