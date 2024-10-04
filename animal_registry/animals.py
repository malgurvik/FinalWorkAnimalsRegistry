import datetime


class Animal:
    _type = ['Pet', 'Pack Animal']

    def __init__(self, name, birthday, commands=None):
        self.name = name
        self.birthday = datetime.date(year=int(birthday.split('.')[2]),
                                      month=int(birthday.split('.')[1]),
                                      day=int(birthday.split('.')[0]))
        self.commands = commands if commands else []

    def learn_command(self, *args):
        for command in args:
            self.commands.append(command)
        return f'{self.name} learned a new command: {self.commands}.'

    def __str__(self):
        return f'{self.name} {self.birthday} {self.commands if self.commands else None}'


class Cat(Animal):
    def __init__(self, name, birthday):
        super().__init__(name, birthday)
        self.type = super()._type[0]

    def __str__(self):
        return f'Cat, {super().__str__()}'


class Dog(Animal):
    def __init__(self, name, birthday):
        super().__init__(name, birthday)
        self.type = super()._type[0]

    def __str__(self):
        return f'Dog, {super().__str__()}'


class Hamster(Animal):
    def __init__(self, name, birthday):
        super().__init__(name, birthday)
        self.type = super()._type[0]

    def __str__(self):
        return f'Hamster, {super().__str__()}'


class Horse(Animal):
    def __init__(self, name, birthday):
        super().__init__(name, birthday)
        self.type = super()._type[1]

    def __str__(self):
        return f'Horse, {super().__str__()}'


class Donkey(Animal):
    def __init__(self, name, birthday):
        super().__init__(name, birthday)
        self.type = super()._type[1]

    def __str__(self):
        return f'Donkey, {super().__str__()}'


class Camel(Animal):
    def __init__(self, name, birthday):
        super().__init__(name, birthday)
        self.type = super()._type[1]

    def __str__(self):
        return f'Camel, {super().__str__()}'
