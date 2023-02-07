from random import randint
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import config_task2 as c2

updater = Updater(token = c2.TOKEN)
dispatcher = updater.dispatcher

def start(update, context):
    context.bot.send_message(chat_id = update.effective_chat.id, text = f'Здравстуйте!, {update.effective_user.first_name}. Это игра "Конфеты".')
    context.bot.send_message(chat_id = update.effective_chat.id, text = 'Правила игры. На столе лежат 120 конфет. Игроки по очереди берут конфеты со стола.\
За один ход можно взять от 1 до 28 конфет. Побеждает игрок, забравший конфеты последним.')
    context.user_data['count_candy'] = 120
    select_player = randint(1, 2)
    if select_player == 1:
        move_text(update, context, select_player)
    else:
        move_text(update, context, select_player)
        bot_move(update, context)

def move_text(update, context, select_player):
    count_candy = context.user_data.get('count_candy')
    if select_player == 1:
        name = f'{update.effective_user.first_name}, Ваш ход.'
    else:
        name = 'Ход бота.'
    context.bot.send_message(chat_id = update.effective_chat.id, text = f'{name} На столе осталось {count_candy} конф.')

def cancel(update, context):
    del context.user_data['count_candy']
    update.message.reply_text('Конец игры. Чтобы начать заново, нажмите /start')

    context.user_data.clear()

def human_move(update, context):
    count_candy = context.user_data.get('count_candy')
    if count_candy == 0 or count_candy == None:
        context.bot.send_message(chat_id = update.effective_chat.id, text = 'Для начала игры нажмите /start')
        context.bot.send_message(chat_id = update.effective_chat.id, text = 'Чтобы завершить игру, нажмите /end')
        return
    try:
        user_text = int(update.message.text)
        if 0 < user_text < 29:
            move = user_text
            context.bot.send_message(chat_id = update.effective_chat.id, text = f'Вы берете {move} конф. На столе осталось {count_candy - move} конф.')
        else:
            if count_candy < 29:
                message = f'Число должно быть от 1 до {count_candy}. Попробуйте еще раз!'
            else:
                message = "Число должно быть от 1 до 28. Попробуйте еще раз!"
            context.bot.send_message(chat_id = update.effective_chat.id, text = message)
            return
    except Exception:
        context.bot.send_message(chat_id = update.effective_chat.id, text = 'Нужно ввести число. Попробуйте еще раз!')
    count_candy -= move
    if count_candy == 0:
        context.bot.send_message(chat_id = update.effective_chat.id, text = 'Победа! \nДля начала игры нажмите /start')
        return
    context.user_data['count_candy'] = count_candy
    bot_move(update,context)

def bot_move(update, context):
    count_candy = context.user_data.get('count_candy')
    if count_candy > 116:
        move = count_candy - 116
    elif count_candy == 116 or count_candy == 87 or count_candy == 58 or count_candy == 29:
        move = randint(1, 28)
    elif 87 < count_candy <= 115:
        move = count_candy - 87
    elif 58 < count_candy <= 86:
        move = count_candy - 58    
    elif 29 < count_candy <= 57:
        move = count_candy - 29
    elif 0 < count_candy <= 28:
        move = count_candy
    context.bot.send_message(chat_id = update.effective_chat.id, text = f'Бот берет {move} конф.')
    count_candy -= move
    if count_candy == 0:
        context.bot.send_message(chat_id = update.effective_chat.id, text='Победил Бот! \nДля начала игры нажмите /start')    
        del context.user_data['count_candy']
        context.user_data.clear()
        return
    context.user_data['count_candy'] = count_candy
    move_text(update,context,1)


start_game = CommandHandler('start', start)
user_move = MessageHandler(Filters.text, human_move)
end_game = CommandHandler('end', cancel)

dispatcher.add_handler(start_game)
dispatcher.add_handler(end_game)
dispatcher.add_handler(user_move)

updater.start_polling()
updater.idle()