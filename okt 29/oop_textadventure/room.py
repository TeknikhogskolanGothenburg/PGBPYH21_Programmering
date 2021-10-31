from item import Item
from data.items_data import items
from utils import item_creator


class Room:
    def __init__(self, **room):
        self.__dict__ = room
        room_items = []
        for item_id in self.items:
            room_items.append(item_creator(item_id))

        self.items = room_items
