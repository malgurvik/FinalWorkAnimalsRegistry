import sqlite3


def create_database():
    with sqlite3.connect('animal_registry.db') as db:
        cursor = db.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS animals
                         (id INTEGER PRIMARY KEY AUTOINCREMENT,
                         species TEXT NOT NULL,
                         name TEXT NOT NULL,
                         birthday DATE NOT NULL,
                         commands TEXT)''')
        db.commit()


def save_new_animal_to_db(species, name, birthday, commands):
    with sqlite3.connect('animal_registry.db') as db:
        cursor = db.cursor()
        cursor.execute(
            f"INSERT INTO animals (species, name, birthday, commands) "
            f"VALUES ('{species}', '{name.capitalize()}', '{birthday}', '{' '.join(commands)}')"
        )
        db.commit()
        print("New animal added successfully")


def delete_animal_from_db(animal_id):
    with sqlite3.connect('animal_registry.db') as db:
        cursor = db.cursor()
        cursor.execute(f"DELETE FROM animals WHERE id='{animal_id}'")
        db.commit()
        print(f"Animal deleted successfully")


def get_animal_from_db(name):
    with sqlite3.connect('animal_registry.db') as db:
        cursor = db.cursor()
        cursor.execute(f"SELECT * FROM animals WHERE name='{name.capitalize()}'")
        return cursor.fetchall()


def get_all_animal_ordered_birthdays():
    with sqlite3.connect('animal_registry.db') as db:
        cursor = db.cursor()
        cursor.execute(f"SELECT * FROM animals ORDER BY birthday")
        return cursor.fetchall()


def update_animal_in_db(animal_id, commands):
    with sqlite3.connect('animal_registry.db') as db:
        cursor = db.cursor()
        cursor.execute(f"UPDATE animals SET commands='{' '.join(commands)}' WHERE id='{animal_id}'")
        db.commit()
        print("Animal commands updated successfully")
