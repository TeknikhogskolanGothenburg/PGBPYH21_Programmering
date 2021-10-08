import sys
from io import StringIO

def main():
    new_out = StringIO()
    old_out = sys.stdout
    sys.stdout = new_out
    print('hej hopp')
    sys.stdout = old_out
    print('after')
    result = new_out.getvalue()
    print()


if __name__ == '__main__':
    main()
