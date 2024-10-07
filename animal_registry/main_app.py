import animal_regisrty as ar
from animal_registry.animal_regisrty import get_animal_info

"""cat, tomas, 9.10.2009, sit, rest"""


def menu_print():
    menu_list = ['Welcome to the Pet Registry!',
                 '1. Добавить новое животное',
                 '2. Удалить животное из реестра',
                 '3. Информация о животном',
                 '4. Обучить животное новым командам',
                 '5. Вывести список всех животных по дате рождения',
                 '6. Вывести общее количество животных',
                 '7. Выход']
    for el in menu_list:
        print(el)


def main():
    while True:
        menu_print()
        operation = int(input('Выберите действие: '))
        match operation:
            case 1:
                ar.add_animal()
            case 2:
                ar.delete_animal()
            case 3:
                ar.get_animal_info()
            case 4:
                ar.learn_animal()
            case 5:
                ar.get_all_animals()
            case 6:
                ar.get_amount()
            case 7:
                print('До свидания!')
                break


if __name__ == '__main__':
    main()
