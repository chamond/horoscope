import sqlite3
import random

connection = sqlite3.connect('database.db')
cursor = connection.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS vocabulary (id INTEGER PRIMARY KEY AUTOINCREMENT, type STRING, value STRING)''')

def addExpression(type, value):
    cursor.execute('''INSERT INTO vocabulary (type, value) VALUES (?, ?)''', (type, value))
    connection.commit()
    cursor.execute('''DELETE FROM vocabulary WHERE rowid NOT IN (SELECT MIN(rowid) FROM vocabulary GROUP BY type, value)''')
    connection.commit()

cursor.execute('''DELETE FROM vocabulary WHERE rowid NOT IN (SELECT MIN(rowid) FROM vocabulary GROUP BY type, value)''')

# Закрываем соединение и сохраняем изменения
connection.commit()

def get_prediction_store():
    cursor.execute('SELECT value FROM vocabulary WHERE type = "adjective"')
    result = cursor.fetchall()
    adjectives = [row[0] for row in result]

    cursor.execute('SELECT value FROM vocabulary WHERE type = "noun"')
    result = cursor.fetchall()
    nouns = [row[0] for row in result]

    cursor.execute('SELECT value FROM vocabulary WHERE type = "verb"')
    result = cursor.fetchall()
    verbs = [row[0] for row in result]

    return [adjectives, nouns, verbs]


def getPredict(store):
    index = random.randint(0, len(store[0]) - 1)
    adjective = store[0][index]
    store[0].pop(index)

    index = random.randint(0, len(store[1]) - 1)
    noun = store[1][index]
    store[1].pop(index)

    index = random.randint(0, len(store[2]) - 1)
    verb = store[2][index]
    store[2].pop(index)

    return adjective + ' ' + noun + ' ' + verb