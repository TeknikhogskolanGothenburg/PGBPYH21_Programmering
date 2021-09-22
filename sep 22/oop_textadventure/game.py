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
        self.main_command = None
        self.sub_command = None
        self.running = True

    def run(self):
        while self.running:
            self.print_room_info()
            self.get_user_input()
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

    def get_user_input(self):
        command = input("> ")
        command_parts = command.split()

        self.main_command = None
        self.sub_command = None
        if len(command_parts) > 0:
            self.main_command = command_parts[0].lower()
            if len(command_parts) > 1:
                self.sub_command = command_parts[1].lower()

    def process_user_input(self):
        if self.main_command == "go":
            self.player.go(self.sub_command, self.map.get_current_room(self.player.position).exits)

        elif self.main_command == "get":
            self.player.get_item(self.sub_command, self.map.get_current_room(self.player.position))

        elif self.main_command == "drop":
            self.player.drop_item(self.sub_command, self.map.get_current_room(self.player.position))

        elif self.main_command == "inventory":
            self.player.show_inventory()

        elif self.main_command == "save":
            self.save()

        elif self.main_command == "load":
            self.load()

        elif self.main_command == "quit":
            self.running = False
        else:
            print("I don't understand", self.main_command)

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
