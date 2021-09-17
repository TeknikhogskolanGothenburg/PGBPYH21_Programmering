import pickle

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
    with open('person.bin', 'wb') as data_file:
        pickle.dump(persons, data_file)

if __name__ == '__main__':
    main()
