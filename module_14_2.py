import sqlite3                     # Библиотека для работы с базами данных

# Установить на компьютер DB Browser for SQLite. С официального сайта https://sqlitebrowser.org/dl/.  64-разряда

# Создаем файл not_telegram.db

connection = sqlite3.connect("not_telegram.db")  # Подключение к базе данных not_telegram.db
                                                    # с помощью SQLite браузера sqlite3
cursor = connection.cursor()  # Курсор - какая ячейка отмечена

cursor.execute("""
CREATE TABLE IF NOT EXiSTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER NOT NULL
)
""")

# Заполняем таблицу Users десятью записями

for i in range(1, 11):
    cursor.execute("INSERT INTO Users (username, email, age, balance) VALUES (?, ? , ?, ?)",
                   (f"User{i}", f"example{i}@gmail.com", i * 10, 1000))

# Обновляем баланс у каждой второй записи, начиная с первой, на 500

for k in range(1, 11, 2):
    cursor.execute("UPDATE Users SET balance = ? WHERE username = ?", (500, f"User{k}"))

# Удаляем каждую третью запись, начиная с первой

for k in range(1, 11, 3):
    cursor.execute("DELETE FROM Users WHERE username = ?", (f"User{k}",))

# Удаляем из БД шестую запись
cursor.execute("DELETE FROM Users WHERE id = ?", (6,))

# Подсчитываем общее количество записей
cursor.execute(("SELECT COUNT(*) FROM Users"))
total_users = cursor.fetchone()[0]

# Считаем общую сумму всех балансов
cursor.execute(("SELECT SUM(balance) FROM Users"))
all_balances = cursor.fetchone()[0]

# Выводим в консоль средний баланс всех пользователей
print(all_balances / total_users)


connection.commit()  #  Сохраняем состояние
connection.close()   #  Закрываем подключение