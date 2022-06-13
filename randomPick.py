import sys
import random


def pickRandomOption():
    options = sys.argv
    options.pop(0)
    print(random.choice(options))


pickRandomOption()
