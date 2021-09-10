items = [
    {
        "id": "id1",
        "name": "key",
        "description": "An old rusty key",
        "actions": ["get", "drop", "look"],
        "container": False
    },
    {
        "id": "id2",
        "name": "spoon",
        "description": "A silver spoon that once was nice",
        "actions": ["get", "look"],
        "container": False
    },
    {
        "id": "id3",
        "name": "mirror",
        "description": "A small handheld mirror",
        "actions": ["get", "drop", "look"],
        "container": False
    },
    {
        "id": "id4",
        "name": "chest",
        "description": "A locked wooden chest",
        "actions": ["open", "close", "look"],
        "open constraint": ["id1"],
        "container": True,
        "items": ["id5"]
    },
    {
        "id": "id5",
        "name": "sock",
        "description": "An old smelly sock",
        "actions": ["get", "drop", "look"],
        "container": False
    },

]