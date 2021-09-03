room1 = {
    "description": "a dark room",
    "exits": ["south", "east"]
}
room2 = {
    "description": "a pink room",
    "exits": ["south", "west"]
}
room3 = {
    "description": "at your starting point",
    "exits": ["north"]
}
room4 = {
    "description": "a room with a trap",
    "exits": ["north", "east"]
}
room5 = {
    "description": "a dead end",
    "exits": ["west"]
}

the_map = [
    [room1, room2],
    [room3, room4, room5]
]
