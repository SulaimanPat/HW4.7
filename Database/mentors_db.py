import sqlite3
import random

def sq_create():
    global db, cursor
    db=sqlite3.connect("mentors_db.sqlite3")
    cursor=db.cursor()

    if db:
        print("База данных подключена")

    db.execute("CREATE TABLE mentors"
               "(id INTEGER PRIMATY KEY, name TEXT, direction TEXT,"
               "age INTEGER, group_ TEXT)")
    db.commit()

async def sql_command_insert(state):
    async with state.proxy() as data:
        cursor.execute("INSERT INTO anketa VALUES "
                       "(?, ?, ?, ?, ?)", tuple(data.values()))
        db.commit()


async def sql_command_random():
    result = cursor.execute("SELECT * FROM anketa").fetchall()
    random_user = random.choice(result)
    return random_user


async def sql_command_delete(user_id):
    cursor.execute("DELETE FROM anketa WHERE id = ?", (user_id,))
    db.commit()
sq_create()