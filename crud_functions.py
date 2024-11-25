import sqlite3


# Функция для инициализации базы данных и создания таблицы Products
def initiate_db(db_name="products.db"):

    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT,
            price INTEGER NOT NULL
        )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            email TEXT NOT NULL,
            age INTEGER NOT NULL,
            balance INTEGER NOT NULL
        )
    """)
    product_data = [
        ('Product 1', 'Белена', 100),
        ('Product 2', 'Вазелин', 300),
        ('Product 3', 'Зубы крокодила', 500),
        ('Product 4', 'Повязка на левый глаз', 400),
        ('Product 5', 'Зеленка', 200)
    ]
    user_data = []
    cursor.execute("SELECT COUNT(*) FROM Products")
    if cursor.fetchone()[0] == 0:
        cursor.executemany('INSERT INTO Products (title, description, price) VALUES (?, ?, ?)', product_data)
    conn.commit()
    conn.close()

# Функция для получения всех записей из таблицы Products
def get_all_products(db_name="products.db"):

    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM Products")
    products = cursor.fetchall()

    conn.close()
    return products

def add_user(username, email, age, db_name="products.db"):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    try:
        cursor.execute("INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)", (username, email, age, 1000))
        conn.commit()
        print(f"Пользователь {username} добавлен.")
    except sqlite3.IntegrityError:
        print(f"Пользователь с этим именем {username} уже существует.")
    finally:
        conn.close()


def is_included(username, db_name="products.db"):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    cursor.execute("SELECT 1 FROM Users WHERE username = ?", (username,))
    result = cursor.fetchone()
    conn.close()
    return bool(result)


