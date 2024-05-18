def main():
    choice = dict(one=1, two=2, three=3, four=4, five=5)
    print(choice['four'])
    print(choice.get('six','other'))

if __name__ == "__main__": main()
