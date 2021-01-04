import Utils as db_utilities
from datetime import datetime
import mysql.connector
import time

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="db437"
)
cr = mydb.cursor()

def find_matched_items():

    while True:
        time.sleep(3600) # Each 1 hour, the bot sends notificatoins to all the volunteers
        matched_items_query = "SELECT * FROM DonationLog WHERE is_being_delivered=0 AND is_delivered=0"
        cr.execute(matched_items_query)
        matched_items = cr.fetchall()
        if matched_items.__len__() >= 1:
            volunteers_query = "SELECT chatID FROM volunteers"
            cr.execute(volunteers_query)
            volunteers = cr.fetchall()
            if volunteers_query.__len__() >= 1:
                for volunteer in volunteers:
                    chat_id = volunteer[0]
                    message = "There are pending items need to be delivered. Please run the /deliver command for more info"
                
                    # Send message Here:
                    # bot.send_message_to_chat(chat_id, message)
                    # Note from A.Y: the 'bot.send_message_to_chat' should be somewhere in the telegram API,
                    # But I did not find it. Once someone finds it, just use it here.
                    # Everything else works well