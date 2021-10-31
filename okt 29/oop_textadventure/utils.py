from data.items_data import items
from item import Item


def item_creator(item_id):
    item_object = None
    for item in items:
        if item['id'] == item_id:
            item_object = Item(**item)
            break
    return item_object
