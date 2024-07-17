import sqlite3

connect=sqlite3.connect("it_park.db")
cursor=connect.cursor()

cursor.execute("""
                CREATE TABLE IF NOT EXISTS it_park(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    full_name VARCHAR(30) NOT NULL,
                    age INT DEFAULT NULL,
                    directions VARCHAR (10) NOT NULL,
                    is_activ BOOLEN NOT NULL DEFAULT FALSE
               )""")

def register():
    full_name=input("Введите Ф.И.О: ")
    age=int(input("Введите возраст: "))
    directions=input("Выберите направление(backend, frontend, ui ux design: )")
    is_activ=bool(input("Есть ноутбук?: "))
    print("Успешно зарегистрированы!")

    cursor.execute(f"""INSERT INTO it_park
                (full_name,age,directions,is_activ)
                VALUES('{full_name}', '{age}', '{directions}', '{is_activ}')
    """)

    connect.commit()

def all_students():
    cursor.execute("SELECT * FROM it_park")
    student = cursor.fetchall()
    print(student)

register()