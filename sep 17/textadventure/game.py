import json
from map import the_map
from items import items
from terminal_color import color_print
from os import listdir
from os.path import isfile, join


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


def get(row, col, items_in_room, item, inventory):
    # Get a list of actions for this item
    actions_for_item = []
    for room_item in items_in_room:
        if item == room_item['name']:
            actions_for_item = room_item['actions']

    # if actions_for_item is empty, the item is not in this room
    if len(actions_for_item) > 0:
        # if get one of the actions we can perform on this item?
        if 'get' in actions_for_item:
            color_print("yellow", f"You pick up the {item}")
            item_id = [room_item['id'] for room_item in items_in_room if room_item["name"] == item][0]
            the_map[row][col]['items'].remove(item_id)
            inventory.append(item_id)
        else:
            color_print("red", f"There is no way for you to pick up the {item}")
    else:
        color_print("red", f"There is no {item} in this room")


def drop(row, col, item, inventory):
    # Get id and actions for the item we want to drop
    item_info = [(an_item['id'], an_item['actions']) for an_item in items if an_item['name'] == item]

    # Check if the item we want to drop exists in the items list
    if len(item_info) >= 1:
        # The first item in the list is a tuple, and the first item in that tuple is the id we are looking for
        item_id = item_info[0][0]
        # and the second thing in the tuple is the list of action we can perform on this item
        item_actions = item_info[0][1]
        # Check if the selected item is in the inventory
        if item_id in inventory:
            if 'drop' in item_actions:
                color_print("yellow", f"You drop the {item} to the floor")
                inventory.remove(item_id)
                the_map[row][col]["items"].append(item_id)
            else:
                color_print("red", f"You can't drop the {item}")
        else:  # The player does not have this item in the inventory
            color_print("red", f"There is no {item} in your inventory")
    else:  # This item is not in the game at all
        color_print("red", f"There is no {item} in your inventory")


def show_inventory(inventory):
    if len(inventory) == 0:
        color_print("red", "Your inventory is empty")
    else:
        # inventory_items will be a list of the names of the items in the inventory
        # TODO: Sort inventory before printing. Use function to make this simpler
        inventory_items = [an_item['name'] for item_id in inventory for an_item in items if item_id == an_item['id']]
        print("You have the following in your inventory:")
        for item in inventory_items:
            color_print("magenta", f"* {item}")


def room_items(room):
    """
    This function creates a list of dictionaries
    Each dictionary contains information about one item
    that exists in this room
    parameters:
    room: dict (a dict containing the room information)
    returns: list[dict]
    """
    items_in_room = []
    for item_id in room["items"]:
        for item in items:
            if item_id == item["id"]:
                # Found an item for the current room
                items_in_room.append(item)
    return items_in_room


def save(row, col, inventory):
    file_name = input("What would you like to call this save? ")
    file_name += '.taf'

    data_to_save = {
        'position': {
            'row': row,
            'col': col
        },
        'inventory': inventory,
        'map': the_map
    }

    with open('./saved_games/' + file_name, 'w', encoding='utf-8') as save_file:
        json.dump(data_to_save, save_file)

def list_saved_games():
    files = []
    for f in listdir('./saved_games'):
        if f.endswith('.taf'):
            files.append(f.replace('.taf', ''))

    files = [f.replace('.taf', '') for f in listdir('./saved_games') if f.endswith('.taf')]

    return files


def load():
    global the_map
    saved_games = list_saved_games()

    while True:
        print("You have these games saved:")
        for game in saved_games:
            color_print("yellow", f"\t{game}")
        file_name = input("What save would you like to load? ")
        if file_name in saved_games:
            break
        color_print("red", f"{file_name} is not the name of a saved game")

    file_name += '.taf'
    with open('./saved_games/' + file_name, 'r', encoding='utf-8') as save_file:
        loaded_data = json.load(save_file)

    the_map = loaded_data['map']
    inventory = loaded_data['inventory']
    row = loaded_data['position']['row']
    col = loaded_data['position']['col']
    return row, col, inventory

def room_items_comp(room):
    """
    Same as function room_items, but this one uses a comprehension
    """
    # same as room_items
    return [item for item_id in room["items"] for item in items if item_id == item["id"]]


def main():
    row = 0
    col = 1
    inventory = []
    running = True

    while running:
        print("You are now in", the_map[row][col]['description'])
        color_print("blue", f"There are exits to the {the_map[row][col]['exits']}")

        # Get a list of all the items in this room
        items_in_room = room_items(the_map[row][col])

        if len(items_in_room) > 0:
            # Create a list with the item names for all the items in this room
            found_items = [item['name'] for item in items_in_room]
            print("Items in the room:", found_items)

        command = input("> ")
        command_parts = command.split()

        main_command = command_parts[0].lower()

        if main_command == "go":
            row, col = go(row, col, command_parts[1].lower())

        elif main_command == "get":
            get(row, col, items_in_room, command_parts[1].lower(), inventory)

        elif main_command == "drop":
            drop(row, col, command_parts[1].lower(), inventory)

        elif main_command == "inventory":
            show_inventory(inventory)

        elif main_command == "save":
            save(row, col, inventory)

        elif main_command == "load":
            row, col, inventory = load()

        elif main_command == "quit":
            running = False

        else:
            print("I don't understand", command_parts[0])

    print("Thanks for playing the game.")


if __name__ == '__main__':
    main()
