def main():
    room = {
        "description": "at your starting point",
        "exits": ["north", "east"]
    }

    print("You are now in", room['description'])
    print("There are exits to the", room['exits'])


if __name__ == '__main__':
    main()
