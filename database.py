import sqlite3

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

def getPredict():
    adjective = cursor.execute('SELECT value FROM vocabulary WHERE type = "adjective" ORDER BY RANDOM() LIMIT 1').fetchone()[0]
    noun = cursor.execute('SELECT value FROM vocabulary WHERE type = "noun" ORDER BY RANDOM() LIMIT 1').fetchone()[0]
    verb = cursor.execute('SELECT value FROM vocabulary WHERE type = "verb" ORDER BY RANDOM() LIMIT 1').fetchone()[0]
    return adjective + ' ' + noun + ' ' + verb