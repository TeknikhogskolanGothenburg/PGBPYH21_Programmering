from sys import getsizeof

def main():
    a = 'abc'
    print(getsizeof(a))
    print(ord('木'))
    # line = "Alice was beginning to get very tired of sitting by her sister on the"
    # password = "s3cr37"
    # encrypted = ""
    # for i, c in enumerate(line):
    #     print(ord(c) ^ ord(password[i % len(password)]))

if __name__ == '__main__':
    main()
