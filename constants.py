import sys

try:
    FIELD_SIZE = int(sys.argv[1]) if len(sys.argv) > 1 else 3
    if FIELD_SIZE < 3 or FIELD_SIZE > 15:
        raise ValueError
except ValueError:
    print('Too small or huge field.')
    exit(1)
except:
    print('Wrong type.')
    exit(1)

WIDTH = 800
HEIGHT = 600

MIN_W = 150
MIN_H = 150
