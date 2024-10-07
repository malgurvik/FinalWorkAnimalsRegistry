from animals import AnimalRegistry as ar
import db_operations as db
from datetime import date, datetime


def user_input():
    actions = ['Введите вид животного(cat, dog, hamster, horse, camel, donkey): ',
               'Введите имя животного: ',
               'Введите дату рождения животного (в формате: yyyy-mm-dd): ',
               'Введите команды через пробел(если нет - оставьте пустым): ']
    result = []
    for action in actions:
        result.append(input(action))
    return result


def add_animal():
    animal = ar.get_animal(*user_input())
    db.save_new_animal_to_db(animal.__class__.__name__, animal.name, animal.birthday, animal.commands)


def get_animal_to_use():
    name = input('Введите имя животного: ')
    animal = db.get_animal_from_db(name)
    return animal


def delete_animal():
    animal = get_animal_to_use()
    if len(animal) > 1:
        print('Выберите животное из списка: ')
        for i, a in enumerate(animal, 1):
            print(f'{i}. {a[1]} {a[2]} {a[3]}')
        num = int(input('Введите номер животного: '))
        db.delete_animal_from_db(animal[num - 1][0])
    else:
        db.delete_animal_from_db(animal[0][0])


def get_age(birthday):
    today = date.today()
    birthday = datetime.strptime(birthday, '%Y-%m-%d').date()
    age = today.year - birthday.year - ((today.month, today.day) < (birthday.month, birthday.day))
    print((today.month, today.day) < (birthday.month, birthday.day))
    if age < 1:
        # age = today.month - birthday.month - ((today.year, today.month, today.day) > (birthday.year, birthday.month, birthday.day)) + 12
        age = today.month - birthday.month - ((today.month, today.day) < (birthday.month, birthday.day))
    return age


def get_animal_info():
    animal = get_animal_to_use()
    print('Информация о животном: ')
    for i, a in enumerate(animal, 1):
        print(f'{i}. Вид: {a[1]} Имя: {a[2]} Дата рождения: {a[3]} Возраст: {get_age(a[3])} лет Команды: {a[4]}')


def learn_animal():
    animal = get_animal_to_use()
    if len(animal) > 1:
        print('Выберите животное из списка: ')
        for i, a in enumerate(animal, 1):
            print(f'{i}. {a[1]} {a[2]} {a[3]}')
        num = int(input('Введите номер животного: '))
        new_commands = input('Введите новые команды через пробел: ')
        this_animal = ar.get_animal(*animal[num - 1][1:])
        this_animal.learn_command(*new_commands.split())
        db.update_animal_in_db(animal[num - 1][0], this_animal.commands)
    else:
        new_commands = input('Введите новые команды через пробел: ')
        this_animal = ar.get_animal(*animal[0][1:])
        this_animal.learn_command(*new_commands.split())
        db.update_animal_in_db(animal[0][0], this_animal.commands)


def get_all_animals():
    animals = db.get_all_animal_ordered_birthdays()
    print('Список всех животных: ')
    for i, a in enumerate(animals, 1):
        print(f'{i}. {a[1]} Имя: {a[2]} Дата рождения: {a[3]} Команды: {a[4]}')


def get_amount():
    animals = db.get_all_animal_ordered_birthdays()
    print(f'Общее количество животных: {len(animals)}')
