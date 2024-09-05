from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters

from secrets import BOT_TOKEN

# Используй Heroku

# Команда /start
async def start(update: Update, context) -> None:
    await update.message.reply_text('Привет! Я Telegram-бот. Напиши мне что-нибудь.')

# Ответ на обычные сообщения
async def echo(update: Update, context) -> None:
    received_text = update.message.text
    await update.message.reply_text(f'Ты написал: {received_text}')

# Основной блок
if __name__ == '__main__':
    # Создаем приложение
    application = ApplicationBuilder().token(BOT_TOKEN).build()

    # Добавляем обработчики команд и сообщений
    application.add_handler(CommandHandler('start', start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    # Запускаем бота
    application.run_polling()