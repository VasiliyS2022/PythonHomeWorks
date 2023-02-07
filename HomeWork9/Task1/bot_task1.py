from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import config_task1 as c1

updater = Updater(token = c1.TOKEN)
dispatcher = updater.dispatcher

def start(update, context):
    context.bot.send_message(update.effective_chat.id, 'Добро пожаловать! Напишите текст: ')

def censor(update, context):
    text = update.message.text
    context.bot.send_message(update.effective_chat.id, f"{' '.join(filter(lambda i: 'абв' not in i.lower(), text.split()))}")

start_handler = CommandHandler('start', start)
censor_handler = MessageHandler(Filters.text, censor)
dispatcher.add_handler(start_handler)
dispatcher.add_handler(censor_handler)

updater.start_polling()
updater.idle()