from random import randint

from telegram import Update, Bot
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters

from secrets import BOT_TOKEN
from database import getPredict, addExpression, get_prediction_store

import random

# Команда /start
async def predict(update: Update, context) -> None:
    store = get_prediction_store()
    morningPredict = 'Утром вас ждет: ' + getPredict(store)
    afternoonPredict = 'В обед случится невероятное: ' + getPredict(store)
    eveningPredict = 'Но на ужин у вас: ' + getPredict(store)
    await update.message.reply_text(morningPredict + '\n' + afternoonPredict + '\n' + eveningPredict)

# Команда /start
async def add(update: Update, context) -> None:
    message = update.message.text.replace('/addprediction', '')
    if message == "":
        await update.message.reply_text('Ничего не добавлено')
        return
    structure = list(
        map(str.strip, message.split(';'))
    )
    try:
        adjective = structure[0]
    except IndexError:
        adjective = ""
    try:
        noun = structure[1]
        addExpression('noun', structure[1].strip())
    except IndexError:
        noun = ""
    try:
        verb = structure[2]
        addExpression('verb', structure[2].strip())
    except IndexError:
        verb = ""
    print(adjective, noun, verb)
    words = []
    if adjective != "":
        addExpression('adjective', adjective)
        words.append(adjective)
    if noun != "":
        addExpression('noun', noun)
        words.append(noun)
    if verb != "":
        addExpression('verb', verb)
        words.append(verb)

    await update.message.reply_text('Спасибо, добавлено: ' + str(list(map(str.strip, words))))

async def dices(update: Update, context) -> None:
    sum = 0
    for i in range(100):
        sum += randint(1, 6)
    await update.message.reply_text(f'Я ставлю, что выпадет: {sum}')

if __name__ == '__main__':
    application = ApplicationBuilder().token(BOT_TOKEN).build()
    application.add_handler(CommandHandler('predict', predict))
    application.add_handler(CommandHandler('addprediction', add))
    application.add_handler(CommandHandler('dices', dices))
    application.run_polling()

