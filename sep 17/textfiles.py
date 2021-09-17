def main():
    x = 10
    age = 45

    my_file = open("textfile.txt", "w", encoding="utf-8")
    my_file.write(f"Hej på dig {x}\nHur mår du {age}?\n")
    my_file.close()

    with open("textfile3.txt", "a", encoding="utf-8") as my_file:
        my_file.write("Jaha... en ny fil!\nDet var kul\n")

    with open("textfile2.txt", "r", encoding="utf-8") as f:
        for row in f:
            print(row.rstrip())

    with open("textfile2.txt", "r", encoding="utf-8") as f2:
        lines = [line.rstrip() for line in f2.readlines()]
        print()

    with open("textfile2.txt", "r", encoding="utf-8") as f3:
        result = f3.read(5)
        result = f3.read(7)
        result = f3.read(22)
        print()
    print()

if __name__ == '__main__':
    main()
