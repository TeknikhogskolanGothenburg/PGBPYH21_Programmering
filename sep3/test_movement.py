def main():
    exits = ["north", "east"]
    dir = input("> ")
    if dir.lower() in exits:
        print("You can go there")
    else:
        print("You can't go there")



if __name__ == '__main__':
    main()
