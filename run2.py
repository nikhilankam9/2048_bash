import sys

def get_string():
    return '1234'

def edge():
    for i in range(0, 26):
        if i % 5 == 0:
            sys.stdout.write('|')
        else:
            sys.stdout.write('-')

def center():
    for i in range(0, 26):
        if i % 5 == 0:
            sys.stdout.write('|')
        else:
            str = get_string()
            sys.stdout.write(str[i%5 - 1])

def block():
    edge()
    sys.stdout.write('\n')
    center()
    sys.stdout.write('\n')
    edge()
    sys.stdout.write('\n')
    center()
    sys.stdout.write('\n')
    edge()
    sys.stdout.write('\n')
    center()
    sys.stdout.write('\n')
    edge()
    sys.stdout.write('\n')
    center()
    sys.stdout.write('\n')
    edge()
    sys.stdout.write('\n')
    center()
    sys.stdout.write('\n')
    edge()

def main():
    sys.stdout.write('\n')
    sys.stdout.softspace=0
    block()
    sys.stdout.write('\n')

    sys.stdout.write('\n')
    sys.stdout.write('\n')
    sys.stdout.write('\n')

if __name__ == "__main__":
    main()
