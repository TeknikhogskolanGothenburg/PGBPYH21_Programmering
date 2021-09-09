from map import the_map
from terminal_color import color_print


def go(row, col, direction):
    if direction in the_map[row][col]['exits']:
        if direction == "north":
            row -= 1
        elif direction == "south":
            row += 1
        elif direction == "east":
            col += 1
        elif direction == "west":
            col -= 1
    else:
        print("You can't go in that direction.")
    return row, col


def get(row, col, item, inventory):
    # Check if the selected item is in the room
    if item in the_map[row][col]['items']:
        color_print("yellow", f"You pick up the {item}")
        the_map[row][col]['items'].remove(item)
        inventory.append(item)
    else:
        color_print("red", f"There is no {item} in this room")


def drop(row, col, item, inventory):
    # Check if the selected item is in the inventory
    if item in inventory:
        color_print("yellow", f"You drop the {item} to the floor")
        inventory.remove(item)
        the_map[row][col]["items"].append(item)
    else:
        color_print("red", f"There is no {item} in your inventory")


def show_inventory(inventory):
    if len(inventory) == 0:
        color_print("red", "Your inventory is empty")
    else:
        print("You have the following in your inventory:")
        for item in inventory:
            color_print("magenta", f"* {item}")


def main():
    row = 1
    col = 0
    inventory = []
    running = True

    while running:
        print("You are now in", the_map[row][col]['description'])
        color_print("blue", f"There are exits to the {the_map[row][col]['exits']}")
        if len(the_map[row][col]['items']) > 0:
            print("Items in the room:", the_map[row][col]['items'])

        command = input("> ")
        command_parts = command.split()

        main_command = command_parts[0].lower()

        if main_command == "go":
            row, col = go(row, col, command_parts[1].lower())

        elif main_command == "get":
            get(row, col, command_parts[1].lower(), inventory)

        elif main_command == "drop":
            drop(row, col, command_parts[1].lower(), inventory)

        elif main_command == "inventory":
            show_inventory(inventory)

        elif main_command == "quit":
            running = False

        else:
            print("I don't understand", command_parts[0])

    print("Thanks for playing the game.")


if __name__ == '__main__':
    main()
