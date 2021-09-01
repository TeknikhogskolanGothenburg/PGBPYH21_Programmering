def main():
    # Numeriska datatyper
    # Heltal - int
    value = 13
    number = 7
    # Flyttal - float
    float_value = 4.67
    # Strängar - str
    name = "Joakim"
    other_name = 'Lisa'

    # Logiska datatyper
    # Boolean - bool
    done = False
    run = True

    # Sekvenstyper
    # Lista - list
    # List är mutable - går att ändra
    values = [56, 3, 45, 1, 19, 7, 3]
    names = ['Pelle', 'Anna', 'Kalle', 'Fjodor']
    things = [1, 3.45, 'Hej', True]
    table = [
        [1, 2, 3],
        [4, 5, 6]
    ]
    values[2] = 777
    print(values)

    # Tuple
    # Är immutable - går INTE att ändra
    numbers = (2, 2, 2)
    print(numbers)

    # Set - Kan bara lagra unika värden
    # Mutable
    set_values = {1, 2, 3, 4, 1, 2, 3}
    list_values = [13, 22, 9, 22, 3, 13, 7, 22]
    unique_values = list(set(list_values))
    print(list_values)
    print(unique_values)

    the_text = "Hej du. Hoppas allt är bra med digöäå"
    unique_letters = list(set(the_text))
    unique_letters.sort()
    print(unique_letters)

    # Mapping type
    # Dictionary - dict
    persons = [
        {
            "name": "Sue Jones",
            "age": 34,
            "email": "sue@email.com"
        },
        {
            "name": "Bob Smith",
            "age": 45,
            "email": "bob@email.com"
        }
    ]
    ages = persons[0]['age'] + persons[1]['age']
    print(ages)


if __name__ == '__main__':
    main()
