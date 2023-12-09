import sqlite3

# Підключення до бази даних
conn = sqlite3.connect('users.db')
cursor = conn.cursor()

# Створення таблиці "users"
cursor.execute('''CREATE TABLE IF NOT EXISTS users
                  (id INTEGER PRIMARY KEY, username TEXT, password TEXT, age INTEGER, gender TEXT)''')

# Реєстрація користувача
def register_user():
    username = input("Введіть ім'я користувача: ")
    password = input("Введіть пароль: ")
    age = int(input("Введіть вік: "))
    gender = input("Введіть стать: ")

    # Перевірка на унікальність імені користувача
    cursor.execute("SELECT * FROM users WHERE username=?", (username,))
    if cursor.fetchone() is not None:
        print("Користувач з таким ім'ям вже існує.")
    else:
        # Вставка нового запису в таблицю "users"
        cursor.execute("INSERT INTO users (username, password, age, gender) VALUES (?, ?, ?, ?)",
                       (username, password, age, gender))
        conn.commit()
        print("Користувач успішно зареєстрований.")

# Авторизація користувача
def login_user():
    username = input("Введіть ім'я користувача: ")
    password = input("Введіть пароль: ")

    # Перевірка наявності користувача з введеними ім'ям та паролем
    cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
    if cursor.fetchone() is not None:
        print("Ви успішно увійшли в систему.")
    else:
        print("Неправильне ім'я користувача або пароль.")

# Отримання даних користувача
def get_user_data():
    username = input("Введіть ім'я користувача: ")

    # Перевірка наявності користувача з введеним ім'ям
    cursor.execute("SELECT * FROM users WHERE username=?", (username,))
    user = cursor.fetchone()
    if user is not None:
        print("Ім'я: ", user[1])
        print("Вік: ", user[3])
        print("Стать: ", user[4])
    else:
        print("Користувача з таким ім'ям не знайдено.")

# Зміна даних користувача
def change_user_data():
    username = input("Введіть ім'я користувача: ")
    new_age = int(input("Введіть новий вік: "))

    # Перевірка наявності користувача з введеним ім'ям
    cursor.execute("SELECT * FROM users WHERE username=?", (username,))
    user = cursor.fetchone()
    if user is not None:
        # Оновлення запису користувача з новим віком
        cursor.execute("UPDATE users SET age=? WHERE username=?", (new_age, username))
        conn.commit()
        print("Дані користувача оновлено.")
    else:
        print("Користувача з таким ім'ям не знайдено.")

# Виклик функцій
register_user()  # Реєстрація нового користувача
login_user()  # Авторизація користувача
get_user_data()  # Отримання даних користувача
change_user_data()  # Зміна даних користувача

# Закриття підключення до бази даних
conn.close()