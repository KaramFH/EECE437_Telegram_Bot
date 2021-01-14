import handlers_factory
from bot_actions import *
import logging
from typing import Dict
import telegram
import telegram.ext
from telegram.ext import ConversationHandler, MessageHandler, CommandHandler, Filters, CallbackContext, Updater
from telegram import Location
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, Update
import mysql.connector
from Offer import Offer
from datetime import datetime
from user import User
from typing import Dict
import _thread

import os
PORT = int(os.environ.get('PORT', 5000))

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="db437"
)
cr = mydb.cursor()

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
logger = logging.getLogger(__name__)

###########################################################################################################################################################
# MAIN
###########################################################################################################################################################
def main() -> None:

    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # the bot token is unique for every bot

    # This Token cannot be shared because it will allow anyone to control the bot
    BOT_TOKEN = '1482964213:AAGTff1gihMYgQbB7Gx38KENrzZG-Jc8h1M'
    updater = Updater(BOT_TOKEN, use_context=True)

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher
    dispatcher.add_handler(handlers_factory.create_start_handler())
    dispatcher.add_handler(handlers_factory.create_update_handler())
    dispatcher.add_handler(handlers_factory.create_delivery_handler())
    dispatcher.add_handler(handlers_factory.create_pickup_handler())
    dispatcher.add_handler(handlers_factory.create_update_pickup_handler())
    #dispatcher.add_handler(handlers_factory.create_cancel_handler())
    dispatcher.add_handler(handlers_factory.create_need_handler())
    dispatcher.add_handler(handlers_factory.create_update_need_handler())
    dispatcher.add_handler(handlers_factory.create_confirm_delivery_handler())
    # _thread.start_new_thread(manager.find_matched_items, ())
    # _thread.start_new_thread(matcher.run_matcher, ())

    # Start the Bot
    updater.start_polling()
    
    # Use this webhook instead of updater.start_polling() inorder to deploy the bot on a Heroku server.
    
#     updater.start_webhook(listen="0.0.0.0",
#                            port=int(PORT),
#                            url_path=TOKEN)
#     updater.bot.setWebhook('https://yourherokuappname.herokuapp.com/' + TOKEN)

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()

if __name__ == '__main__':
    main()
