from map import the_map


def main():
    row = 1
    col = 0
    running = True

    while running:
        print("You are now in", the_map[row][col]['description'])
        print("There are exits to the", the_map[row][col]['exits'])

        command = input("> ")
        command_parts = command.split()

        if command_parts[0].lower() == "go":
            if command_parts[1].lower() in the_map[row][col]['exits']:
                if command_parts[1].lower() == "north":
                    row -= 1
                elif command_parts[1].lower() == "south":
                    row += 1
                elif command_parts[1].lower() == "east":
                    col += 1
                elif command_parts[1].lower() == "west":
                    col -= 1
            else:
                print("You can't go in that direction.")
        elif command_parts[0].lower() == "quit":
            running = False
        else:
            print("I don't understand", command_parts[0])

    print("Thanks for playing the game.")


if __name__ == '__main__':
    main()
