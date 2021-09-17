def main():
    with open('splwow64.exe', 'rb') as exe_file:
        data = exe_file.read(2)
        print(data)


if __name__ == '__main__':
    main()
