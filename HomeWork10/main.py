from controller import parsing_values, upshot
from telegram import Bot, InlineKeyboardButton,  InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, Filters, MessageHandler, ConversationHandler, CallbackQueryHandler
from logger import get_id, get_name, get_input_values, get_result, log_save, get_time
import config
import datetime

bot = Bot(token= config.TOKEN)
updater = Updater(token= config.TOKEN)
dispatcher = updater.dispatcher
start_calc = 0

def start(update, context):
    context.bot.send_message(update.effective_chat.id, f'Здравствуйте, {update.effective_user.first_name}! Это программа "Калькулятор положительных чисел"')
    context.bot.send_message(update.effective_chat.id, 'Используйте знаки: +, -, *, /, (, ). Вводите знаки и цифры без пробелов.\
Учитывается приоритет действий')
    get_id(update.effective_chat.id)
    get_name(update.effective_user.first_name)
    get_time(datetime.datetime.now())
    keyboard = [[InlineKeyboardButton('END', callback_data='end')]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    bot.send_message(update.effective_chat.id, 'Используйте кнопку END для отключения', reply_markup = reply_markup)
    return start_calc

def taking_values(update, context):
    values = update.message.text
    get_input_values(values)  
    list_data = parsing_values(values) 
    result = upshot(list_data)  
    get_result(result) 
    log_save()  
    context.bot.send_message(update.effective_chat.id, f'Ваш ответ: {result}')

def end(update, context):
    context.bot.send_message(update.effective_chat.id, 'Окончание работы. Для возобновления нажмите /start')
    return ConversationHandler.END

start_handler = CommandHandler('start', start)
receiving_data_handler = MessageHandler(Filters.text & (~Filters.command), taking_values)
end_handler = CallbackQueryHandler(end)

conv_handler = ConversationHandler(entry_points=[start_handler],
                                    states={start_calc: [receiving_data_handler]},
                                    fallbacks=[end_handler])

dispatcher.add_handler(conv_handler)

updater.start_polling()
updater.idle()

if __name__ == '__main__':
    start()