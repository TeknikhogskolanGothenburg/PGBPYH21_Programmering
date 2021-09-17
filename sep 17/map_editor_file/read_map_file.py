import json


def main():
    with open('map.json', 'r', encoding='utf-8') as map_file:
        data = json.load(map_file)
    elements = data['elements']
    rooms = [room for room in elements if room['_type'] == "Room"]
    connectors = [connector for connector in elements if connector['_type'] == "Connector"]

    rooms = [{'id': room['id'], 'name': room['_name'], 'description': room['_description'], 'items': room['objects']} for room in rooms]
    print()


if __name__ == '__main__':
    main()
