import sys
import random


def main():
    options = sys.argv
    options.pop(0)
    print(random.choice(options))


if __name__ == '__main__':
    main()
