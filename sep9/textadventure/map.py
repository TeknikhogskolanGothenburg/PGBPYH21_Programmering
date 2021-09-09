room1 = {
    "description": "a dark room",
    "items": [],
    "exits": ["south", "east"]
}
room2 = {
    "description": "a pink room",
    "items": ["key", "spoon", "mirror"],
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
    "items": [],
    "exits": ["west"]
}

the_map = [
    [room1, room2],
    [room3, room4, room5]
]
