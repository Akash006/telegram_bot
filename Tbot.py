from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters

updater = Updater(token='634661342:AAEnmZa-BC5MljutbdAjRAlocikd0wTE0RA', use_context=True)
dispatcher = updater.dispatcher

def echo(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")

def caps(update, context):
    text_caps = ' '.join(context.args).upper()
    context.bot.send_message(chat_id=update.effective_chat.id, text=text_caps)

def pic(update, context):
    context.bot.send_photo(chat_id=update.effective_chat.id, photo=open('test.png', 'rb'))

def report(update, context):
    context.bot.send_document(chat_id=update.effective_chat.id, document=open('log.txt', 'rb'))

def log(update, context):
    print("Enterd into log")
    with open('log.txt', 'r+') as f:
        for data in f:
            print("in for loop line")
            context.bot.sendMessage(chat_id=update.message.chat_id, text=data)

log_handler = CommandHandler('log', log)
dispatcher.add_handler(log_handler)

report_handler = CommandHandler('report', report)
dispatcher.add_handler(report_handler)

pic_handler = CommandHandler('pic', pic)
dispatcher.add_handler(pic_handler)

caps_handler = CommandHandler('caps', caps)
dispatcher.add_handler(caps_handler)

echo_handler = MessageHandler(Filters.text, echo)
dispatcher.add_handler(echo_handler)

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

updater.start_polling()
updater.idle()
