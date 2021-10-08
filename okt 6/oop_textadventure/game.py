import pickle
from os import listdir
from map import Map
from player import Player
from position import Position
from terminal_color import color_print


class Game:
    def __init__(self):
        self.player = Player(Position(1, 0))
        self.map = Map()
        self.running = True

    def run(self):
        while self.running:
            self.print_room_info()
            self.process_user_input()
        print("Thanks for playing the game.")

    def print_room_info(self):
        current_room = self.map.get_current_room(self.player.position)

        print("You are now in", current_room.description)
        color_print("blue", f"There are exits to the {current_room.exits}")

        if len(current_room.items) > 0:
            # Create a list with the item names for all the items in this room
            found_items = [item.name for item in current_room.items]
            print("Items in the room:", found_items)

    def process_user_input(self):
        command = input("> ")

        current_room = self.map.get_current_room(self.player.position)

        match command.lower().split():
            case ['go', direction] if direction in current_room.exits:
                self.player.go(direction)
            case ['go', *bad_direction]:
                color_print('red', f'It is impossible to go in the direction {" ".join(bad_direction)}')

            case ['get', 'all'] | ['pick', 'up', 'all'] | ['pick', 'all', 'up']:
                for item in current_room.items.copy():
                    self.player.get_item(item.name, current_room)
            case ['get', *items] | ['pick', 'up', *items] | ['pick', *items, 'up']:
                for item in items:
                    self.player.get_item(item, current_room)

            case ['drop', 'all']:
                for item in self.player.inventory.copy():
                    self.player.drop_item(item.name, current_room)
            case ['drop', *items]:
                for item in items:
                    self.player.drop_item(item, current_room)

            case ['inventory']:
                self.player.show_inventory()

            case ['save']:
                self.save()

            case ['load']:
                self.load()

            case ['quit' | 'exit']:
                self.running = False
            case _:
                color_print('red', f"I don't understand how to {command}")

    def save(self):
        file_name = input("What would you like to call this save? ")
        file_name += '.taf'

        data_to_save = {
            'player': self.player,
            'map': self.map
        }

        with open('./saved_games/' + file_name, 'wb') as save_file:
            pickle.dump(data_to_save, save_file)

    @staticmethod
    def list_saved_games():
        files = []
        for f in listdir('./saved_games'):
            if f.endswith('.taf'):
                files.append(f.replace('.taf', ''))

        files = [f.replace('.taf', '') for f in listdir('./saved_games') if f.endswith('.taf')]

        return files

    def load(self):
        saved_games = self.list_saved_games()

        while True:
            print("You have these games saved:")
            for game in saved_games:
                color_print("yellow", f"\t{game}")
            file_name = input("What save would you like to load? ")
            if file_name in saved_games:
                break
            color_print("red", f"{file_name} is not the name of a saved game")

        file_name += '.taf'
        with open('./saved_games/' + file_name, 'rb') as save_file:
            loaded_data = pickle.load(save_file)

        self.map = loaded_data['map']
        self.player = loaded_data['player']
