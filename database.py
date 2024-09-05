import sqlite3

connection = sqlite3.connect('database.db')
cursor = connection.cursor()

# Караульный
# Накурился амурской химки
# "а потом"
# Забрался в шишигу
# "и"
# Перевернул танк
# "в итоге"
# Вся рота отжималась

cursor.execute('''CREATE TABLE IF NOT EXISTS vocabulary (id INTEGER PRIMARY KEY AUTOINCREMENT, type STRING, value STRING)''')

def addExpression(type, value):
    cursor.execute('''INSERT INTO vocabulary (type, value) VALUES (?)''', (type, value))

addExpression('adjective', 'Караульный')
addExpression('noun1', 'Леха')
addExpression('future_verb1', 'Накурится амурской химки')