import json

def main():
    persons = [
        {
            'name': 'lisa',
            'age': 34,
            'email': 'lisa@email.com'
        },
        {
            'name': 'pelle',
            'age': 45,
            'email': 'pelle@email.com'
        }
    ]
    with open('python_persons.json', 'w') as json_file:
        json.dump(persons, json_file)


if __name__ == '__main__':
    main()
