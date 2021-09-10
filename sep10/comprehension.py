def main():
    items_in_room = [
        {
            'id': 'id1',
            'name': 'key',
            'description': 'An old rusty key',
            'actions': ['get', 'drop', 'look'],
            'container': False
        },
        {
            'id': 'id2',
            'name': 'spoon',
            'description': 'A silver spoon that once was nice',
            'actions': ['get', 'drop', 'look'],
            'container': False
        },
        {
            'id': 'id3',
            'name': 'mirror',
            'description': 'A small handheld mirror',
            'actions': ['get', 'drop', 'look'],
            'container': False
        }
    ]

    item_names = []
    for item in items_in_room:
        item_names.append(item['name'])

    print(item_names)

    item_names2 = [item['name'] for item in items_in_room]
    print(item_names2)

    values = [1, 2, 3, 4]

    times_2 = []
    for value in values:
        times_2.append(value * 2)


    print(times_2)



if __name__ == '__main__':
    main()
