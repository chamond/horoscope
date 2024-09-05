from random import randint

from telegram import Update, Bot
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters

from secrets import BOT_TOKEN
from database import getPredict, addExpression

import random

# Команда /start
async def predict(update: Update, context) -> None:
    morningPredict = 'Утром вас ждет: ' + getPredict()
    afternoonPredict = 'В обед случится невероятное: ' + getPredict()
    eveningPredict = 'Но на ужин у вас: ' + getPredict()
    await update.message.reply_text(morningPredict + '\n' + afternoonPredict + '\n' + eveningPredict)

# Команда /start
async def add(update: Update, context) -> None:
    structure = update.message.text.replace('/addPrediction', '').split(';')
    try:
        addExpression('adjective', structure[0].strip())
    except IndexError:
        await update.message.reply_text('Бро, дай мне прилагательное')
        return
    try:
        addExpression('noun', structure[1].strip())
    except IndexError:
        await update.message.reply_text('Бро, дай мне существительное')
        return
    try:
        addExpression('verb', structure[2].strip())
    except IndexError:
        await update.message.reply_text('Бро, дай мне действие')
        return
    await update.message.reply_text('Спасибо, добавлено: ' + str(list(map(str.strip, structure))))

def generate_random_integer(start, end):
    return random.randint(start, end)

async def dices(update: Update, context) -> None:
    sum = 0
    for i in range(100):
        sum += randint(1, 6)
    await update.message.reply_text(f'Я ставлю, что выпадет: {sum}')


# Основной блок
if __name__ == '__main__':
    # Создаем приложение
    application = ApplicationBuilder().token(BOT_TOKEN).build()

    # Добавляем обработчики команд и сообщений
    application.add_handler(CommandHandler('predict', predict))
    application.add_handler(CommandHandler('addPrediction', add))
    application.add_handler(CommandHandler('dices', dices))

    # Запускаем бота
    application.run_polling()

