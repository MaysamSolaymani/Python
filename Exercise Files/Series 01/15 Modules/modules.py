import sys
import os

def main():
    print('Python version {}.{}.{}'.format(*sys.version_info))
    print(sys.platform)
    print(os.name)

if __name__ == "__main__":
    main()
