import telegram.ext
import pandas_datareader as web

with open('token.txt', 'r') as f:
  TOKEN= T.read()

def start (update, context):
  update.message.reply_text("Hello! Welcome To NeuralBot!")

def help (update, context):

 update.message.reply_text("""

The following commands are available:

/start -> Welcome Message

/help-> This Message

/contact-> Information About Contact

/content -> Information About NeuralNine Content""")

updater = telegram.ext.Updater (TOKEN, use_context=True)

disp = updater.dispatcher

def content (update, context):

  update.message.reply_text("We have videos and books! Watch and read them!")

def contact (update, context):

  update.message.reply_text("You can contact Florian on the Discord server.")

def stock(update, context):
    updater = telegram.ext.Updater (TOKEN, use_context=True)

disp = updater.dispatcher

disp.add_handler(telegram.ext.CommandHandler("start", start))

disp.add_handler(telegram.ext.CommandHandler("help", help))

disp.add_handler(telegram.ext.CommandHandler("content", content))

disp.add_handler(telegram.ext.MessageHandler(telegram.ext.Filters.text,handler_message))

updater.start_polling()

updater.idle()