def main():
    # for-loop
    for i in range(10, -1, -1):
        print(i)

    for i in range(4):
        print(i)

    names = ['bob', 'sara', 'lisa', 'don']
    for name in names:
        print(name)

    fruit = "apple"
    for letter in fruit:
        print(letter)

    values = list(range(6))
    print(values)

    running = True
    while running:
        print("Running")
        command = input("Enter command: ")
        if command.lower() == "quit":
            running = False

    print("Done")

if __name__ == '__main__':
    main()
