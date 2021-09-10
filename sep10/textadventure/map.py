room1 = {
    "description": "a dark room",
    "items": [],
    "exits": ["south", "east"]
}

room2 = {
    "description": "a pink room",
    "items": ["id1", "id2", "id3"],
    "exits": ["south", "west"]
}

room3 = {
    "description": "your starting location",
    "items": [],
    "exits": ["north"]
}

room4 = {
    "description": "a room with a trap",
    "items": [],
    "exits": ["north", "east"]
}

room5 = {
    "description": "a dead end",
    "items": ["id4"],
    "exits": ["west"]
}

the_map = [
    [room1, room2],
    [room3, room4, room5]
]
