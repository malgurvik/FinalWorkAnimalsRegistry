from datetime import datetime


class Animal:

    def __init__(self, name: str, birthday: str, commands: str = None):
        self.name = name
        self.birthday = datetime.strptime(birthday, '%Y-%m-%d').date()
        self.commands = commands.split() if commands else []

    def learn_command(self, *args):
        for command in args:
            self.commands.append(command)
        return f'{self.name} learned a new command: {self.commands}.'

    def get_commands(self):
        if self.commands:
            return f'{self.name} can carry out commands: {','.join(self.commands)}'
        else:
            return f'{self.name} doesn\'t know any commands yet.'

    def __str__(self):
        return f'{self.name} {self.birthday} {self.commands if self.commands else None}'


class Cat(Animal):
    def __init__(self, name, birthday, commands=None):
        super().__init__(name, birthday, commands)

    def __str__(self):
        return f'Cat, {super().__str__()}'


class Dog(Animal):
    def __init__(self, name, birthday, commands=None):
        super().__init__(name, birthday, commands)

    def __str__(self):
        return f'Dog, {super().__str__()}'


class Hamster(Animal):
    def __init__(self, name, birthday, commands=None):
        super().__init__(name, birthday, commands)

    def __str__(self):
        return f'Hamster, {super().__str__()}'


class Horse(Animal):
    def __init__(self, name, birthday, commands=None):
        super().__init__(name, birthday, commands)

    def __str__(self):
        return f'Horse, {super().__str__()}'


class Donkey(Animal):
    def __init__(self, name, birthday, commands=None):
        super().__init__(name, birthday, commands)

    def __str__(self):
        return f'Donkey, {super().__str__()}'


class Camel(Animal):
    def __init__(self, name, birthday, commands=None):
        super().__init__(name, birthday, commands)

    def __str__(self):
        return f'Camel, {super().__str__()}'


class AnimalRegistry:
    @staticmethod
    def get_animal(animal_species, *args, **kwargs):
        if animal_species.lower() == 'cat':
            return Cat(*args, **kwargs)
        elif animal_species.lower() == 'dog':
            return Dog(*args, **kwargs)
        elif animal_species.lower() == 'hamster':
            return Hamster(*args, **kwargs)
        elif animal_species.lower() == 'horse':
            return Horse(*args, **kwargs)
        elif animal_species.lower() == 'camel':
            return Camel(*args, **kwargs)
        elif animal_species.lower() == 'donkey':
            return Donkey(*args, **kwargs)
        else:
            return None

# class AnimalRegistry:
#     @staticmethod
#     def add_animal(animal_species, name, birthday, commands=None):
#         if animal_species.lower() == 'cat':
#             return Cat(name, birthday, commands)
#         elif animal_species.lower() == 'dog':
#             return Dog(name, birthday, commands)
#         elif animal_species.lower() == 'hamster':
#             return Hamster(name, birthday, commands)
#         elif animal_species.lower() == 'horse':
#             return Horse(name, birthday, commands)
#         elif animal_species.lower() == 'camel':
#             return Camel(name, birthday, commands)
#         elif animal_species.lower() == 'donkey':
#             return Donkey(name, birthday, commands)
#         else:
#             return None
