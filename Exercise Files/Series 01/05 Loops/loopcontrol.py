def main():
    s = 'this is a string'
    for c in s:
        print(c, end='')
    print()
    for c in s:
        if c == 's': continue
        print(c, end='')
    print()
    for c in s:
        if c == 's': break
        print(c, end='')
    print()
    for c in s:
        print(c, end='')
    else:
        print('end')
    i = 0
    while i < s.__len__():
        print(s[i],end='')
        i += 1
    else:
        print('end***')
if __name__ == "__main__": main()
