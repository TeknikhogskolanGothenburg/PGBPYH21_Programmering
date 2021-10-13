def main():
    name = '木'
    name_bytes = name.encode('utf-8')

    for c in name_bytes:
        print(c)

    name_str = name_bytes.decode('utf-8')
    print(name_str)


if __name__ == '__main__':
    main()
