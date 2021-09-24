class Person:
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone

    def __str__(self):
        return f"{self.name} has email {self.email} and phone number {self.phone}!"


class Teacher(Person):
    def __init__(self, name, email, phone, subject):
        super().__init__(name, email, phone)
        self.subject = subject


class Student(Person):
    def __init__(self, name, email, phone, classes, grades):
        super().__init__(name, email, phone)
        self.classes = classes
        self.grades = grades


def main():
    t1 = Teacher('Joakim', 'joakim@school.com', '07342323232', 'Python Programming')
    s1 = Student('Pelle', 'pelle@school.com', '0754949383', ['Programming for beginners', 'Super Programmer'], ['G', 'VG'])
    print(t1)
    print(s1)


if __name__ == '__main__':
    main()
