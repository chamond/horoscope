import sqlite3

connection = sqlite3.connect('database.db')
cursor = connection.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS vocabulary (id INTEGER PRIMARY KEY AUTOINCREMENT, type STRING, value STRING)''')

def addExpression(type, value):
    cursor.execute('''INSERT INTO vocabulary (type, value) VALUES (?, ?)''', (type, value))
    connection.commit()

# addExpression('adjective', 'Караульный')
# addExpression('noun', 'Леха')
# addExpression('verb', 'Накурится амурской химки')
#
# addExpression('adjective', 'Няшный')
# addExpression('noun', 'Поросенок')
# addExpression('verb', 'Наплюет тебе в табло')
#
# addExpression('adjective', 'Бородатый')
# addExpression('noun', 'Таксист')
# addExpression('verb', 'Станет твоим новым мужем')
#
# addExpression('adjective', 'Симпатичный')
# addExpression('noun', 'Нотариус')
# addExpression('verb', 'Вьебет все твои деньги')
#
# addExpression('adjective', 'Накаченный')
# addExpression('noun', 'Чигма')
# addExpression('verb', 'Сделает тебе больно')
#
# addExpression('adjective', 'Низкоуровневый')
# addExpression('noun', 'Андрей Кревский')
# addExpression('verb', 'Наденет тебе трусы на жопу')
#
# addExpression('adjective', 'Пушистенький')
# addExpression('noun', 'Металлург')
# addExpression('verb', 'Даст тебе в долг')

cursor.execute('''DELETE FROM vocabulary WHERE rowid NOT IN (SELECT MIN(rowid) FROM vocabulary GROUP BY type, value)''')

# Закрываем соединение и сохраняем изменения
connection.commit()

def getPredict():
    adjective = cursor.execute('SELECT value FROM vocabulary WHERE type = "adjective" ORDER BY RANDOM() LIMIT 1').fetchone()[0]
    noun = cursor.execute('SELECT value FROM vocabulary WHERE type = "noun" ORDER BY RANDOM() LIMIT 1').fetchone()[0]
    verb = cursor.execute('SELECT value FROM vocabulary WHERE type = "verb" ORDER BY RANDOM() LIMIT 1').fetchone()[0]
    return adjective + ' ' + noun.lower() + ' ' + verb.lower()