import pickle

def main():
    with open('person.bin', 'rb') as data_file:
        persons = pickle.load(data_file)

    print(persons)


if __name__ == '__main__':
    main()
