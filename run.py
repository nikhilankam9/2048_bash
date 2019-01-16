import sys
import termios
import contextlib


@contextlib.contextmanager
def raw_mode(file):
    old_attrs = termios.tcgetattr(file.fileno())
    new_attrs = old_attrs[:]
    new_attrs[3] = new_attrs[3] & ~(termios.ECHO | termios.ICANON)
    try:
        termios.tcsetattr(file.fileno(), termios.TCSADRAIN, new_attrs)
        yield
    finally:
        termios.tcsetattr(file.fileno(), termios.TCSADRAIN, old_attrs)


def main():
    print 'exit with ^C or ^D'
    with raw_mode(sys.stdin):
        try:
            while True:
                ch = sys.stdin.read(3)
                # if not ch or ch == chr(4):
                #     break
                if not ch or ch == '\x1b[A':
                    print "up"
                    # break
                if not ch or ch == '\x1b[B':
                    print "down"
                    # break
                if not ch or ch == '\x1b[C':
                    print "right"
                    # break
                if not ch or ch == '\x1b[D':
                    print "left"
                    # break
                # print '%02x' % ord(ch),
        except (KeyboardInterrupt, EOFError):
            pass


if __name__ == '__main__':
    main()
