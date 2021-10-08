from terminal_color import color_print


class Player:
    def __init__(self, position):
        self.position = position
        self.inventory = []

    def go(self, direction):
        """
        Moves a player to a different room
        Parameters:
            direction: str, the direction the player should move. Possible values are north, south, east, and west
            Returns:
                None
        """
        match direction:
            case 'north':
                self.position.row -= 1
            case 'south':
                self.position.row += 1
            case 'east':
                self.position.col += 1
            case 'west':
                self.position.col -= 1

    def get_item(self, item_name, current_room):
        found_item = None
        for item in current_room.items:
            if item.name == item_name:
                found_item = item
                break
        if found_item:
            if 'get' in found_item.actions:
                color_print("yellow", f"You pick up the {item_name} from the floor")
                current_room.items.remove(found_item)
                self.inventory.append(found_item)
            else:
                color_print("red", f"You can see the {found_item.name}, but there is no way for you to pick it up")
        else:
            color_print("red", f"There is no {item_name} in this room")

    def drop_item(self, item_name, current_room):
        found_item = None
        for item in self.inventory:
            if item.name == item_name:
                found_item = item
                break
        if found_item:
            if 'drop' in found_item.actions:
                color_print("yellow", f"You drop the {item_name} to the floor")
                self.inventory.remove(found_item)
                current_room.items.append(found_item)
            else:
                color_print("red", f"For some reason you can't drop the {item_name}")
        else:
            color_print("red", f"There is no {item_name} in your inventory")

    def show_inventory(self):
        if len(self.inventory) == 0:
            color_print("red", "Your inventory is empty")
        else:
            print("You have the following in your inventory:")
            for item in sorted(self.inventory, key=lambda i: i.name):
                color_print("magenta", f"* {item.name}")
