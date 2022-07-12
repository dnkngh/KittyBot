from telegram.ext import Updater, Filters, MessageHandler, CommandHandler
from telegram import ReplyKeyboardMarkup


updater = Updater(token='5238714299:AAELBpT-x8lgcqpa45FqNirgE66HhON0W28')
chat_id = 1021239845


def say_hi(update, context):
    chat = update.effective_chat
    context.bot.send_message(chat_id=chat.id, text='Привет, я KittyBot!')


def wake_up(update, context):
    chat = update.effective_chat
    name = update.message.chat.first_name
    buttons = ReplyKeyboardMarkup([
        ['Показать фото котика'],
        ['Который час?', 'Определи мой ip'],
        ['/random_digit'],
    ])
    context.bot.send_message(chat_id=chat.id,
                             text='Спасибо, что вы включили меня, {}!'.format(name),
                             reply_markup=buttons
                             )


updater.dispatcher.add_handler(CommandHandler('start', wake_up))
updater.dispatcher.add_handler(MessageHandler(Filters.text, say_hi))

updater.start_polling(poll_interval=20.0)
updater.idle()
