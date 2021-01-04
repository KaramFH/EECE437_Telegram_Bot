from telegram.ext import ConversationHandler, MessageHandler, CommandHandler, Filters, CallbackContext, Updater
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, Update
from datetime import datetime
from telegram import Location
from user import User
from typing import Dict
from Offer import Offer
import Utils
import telegram.ext
import utilities
import telegram
import logging
import matcher

#karam hasan was here

#context.bot.send_message(chat_id=chat_id, text='Hi User, Add Fund to your account to start trading')

##############################################################################################################################################################################
# Start command
##############################################################################################################################################################################    

# This is the Start command (/start).
# In the Start Command, the bot will ask the user about his basic information which include:
# firstname, lastname, birthdate, phonenumber, address, location
# these info will be stored in a Class User and then they will be stored in the database

# Class User
u1 = User()
offer = Offer()
request = []

# These are the states  of the Start command
CHOOSING, PHONE_NUMBER, PHONE_NUMBER_YN, BIRTHDATE, BIRTHDATE_YN, ADDRESS, ADDRESS_YN, LOCATION, CONCLUDE , MENU, WELCOME, ACTIONS, \
OFFER_TYPE, OFFER_DESCRIPTION, OFFER_QUANTITY, OFFER_done, REQUEST_TYPE, REQUEST_DESCRIPTION, REQUEST_QUANTITY, REQCASH_ESTIMATE, \
REQUEST_NOTED, NEW_VOLUNTEER, CHOOSE_VALUES_TO_UPDATE, U_ADDRESS, U_LOCATION, START_DELIVERY, DELIVERY_SUCCESS, DELIVERY_FAILURE, CHOOSE_DONATION, \
CHOOSE_OFFER, SAVE_OFFER, ASK_OFFER_ID, DELIVER_NEEDS, UPDATE_NEED, ASK_NEED_ID = \
    range(35)


def actions(update: Update, context: CallbackContext) -> int:
    reply_keyboard = [['Donate'],['Volunteer'],['Request'],
                      ['Nothing'],['Deliver'],['Show Offers'],['Update Pickup'],['Show Needs'],['Update on picked up needs']]
    update.message.reply_text(
        "Please choose what you want to do.",
        reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True),
    )
    return ACTIONS

def start(update: Update, context: CallbackContext) -> int:

    reply_keyboard = [['Yes! All good', 'Cancel']]
    user = update.message.from_user
    u1.FirstName = user.first_name
    u1.LastName = user.last_name
    u1.ChatID = update.message.chat.id
    u1.UserID = user.id
    u1.CreationDate = datetime.now()

    # in case user is already registered , do not take him through the registration steps
    if Utils.is_registered(user.id, user.first_name) :
        return Welcome_back(update, context)

    #usual registration process taken
    else :
        update.message.reply_text(
            "Hi! My name is Matcher Bot. I will help you during your crisis.\n"
            "First let's see if the information I know about you are correct.\n"
            "First Name: " f'{user.first_name}''\n'
            "Last Name: " f'{user.last_name}''\n'
            "Username: " f'{user.username}''\n'
            "If they are not true please press Cancel and change them in the settings of the telegram app",
            reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True),
        )
        return CHOOSING

# function that asks the user about his phone number
def phone_number(update: Update, context: CallbackContext) -> int:
    update.message.reply_text(
        'All right, please send me your phone number'
    )
    return PHONE_NUMBER

# function that stores the phone number of the user and sends a conformation message
def phone_number_text(update: Update, context: CallbackContext) -> int:
    reply_keyboard = [['Yes', 'No']]
    text = update.message.text
    u1.PhoneNumber = text
    update.message.reply_text(f'Your number is: {text.lower()}? Please make sure',
                              reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True), )

    return PHONE_NUMBER_YN

# function that asks the user about his birthdate
def birthdate(update: Update, context: CallbackContext) -> int:
    update.message.reply_text(
        'Please give me your birthdate in DD/MM/YY format.'
    )
    return BIRTHDATE

# function that stores the birthdate of the user and sends a conformation message
def birthdate_text(update: Update, context: CallbackContext) -> int:
    reply_keyboard = [['Yes', 'No']]
    text = update.message.text
    u1.Birthdate = text
    update.message.reply_text(f'Your birthdate is: {text.lower()}? Please make sure',
                              reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True), )
    return BIRTHDATE_YN

# function that asks the user about his address
def address(update: Update, context: CallbackContext) -> int:
    update.message.reply_text(
        'Alright, please send me your address'
    )

    return ADDRESS

# function that stores the address of the user and sends a conformation message
def address_text(update: Update, context: CallbackContext) -> int:

    reply_keyboard = [['Yes', 'No']]
    text = update.message.text
    u1.AddressDescription = text
    update.message.reply_text(f'Your address is: {text.lower()}? Please make sure',
                              reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True), )

    return ADDRESS_YN

# function that asks the user about his location
def ask_location(update: Update, context: CallbackContext) -> int:
    update.message.reply_text(
        'Now, send me your location please'
    )
    print("asked for location")
    return LOCATION

# function that stores the users location in the user class and sends him a thankyou message
def location(update: Update, context: CallbackContext) -> int:
    reply_keyboard = [['Sure!', 'Cancel']]
    user = update.message.from_user
    user_location = update.message.location
    u1.AddressLatitude = str(user_location.latitude)
    u1.AddressLongitude = str(user_location.longitude)
    update.message.reply_text(
        'Thank you! your information will now be saved in the database to help with your needs. Press Cancel to delete everything',
        reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True),
    )
    #Utils.create_new_user(u1.UserID, u1.FirstName, u1.LastName, u1.Birthdate, u1.PhoneNumber, u1.ChatID)
    return CONCLUDE

# Function that sends a reply to the user summarizing the information sent from the user
def received_information(update: Update, context: CallbackContext) -> int:
    # add_to_DB(u1) this function adds the user to the database after the user gave us all the information about him
    # This fuction is still being constructed
    # When finished it will be imported and used in the bot
    reply_keyboard = [ ['Ok, Sounds Good!'], ['Later'] ]
    update.message.reply_text(
        "Thank you for signing up! These are the information you gave us about you: \n"
        "First Name: "f'{u1.FirstName}''\n'
        "Last Name: "f'{u1.LastName}''\n'
        "Birthdate: "f'{u1.Birthdate}''\n'
        "Address: "f'{u1.AddressDescription}''\n'
        "Phone Number: "f'{u1.PhoneNumber}''\n'
        "Address Latitude: "f'{u1.AddressLatitude}''\n'
        "Address Longitude: "f'{u1.AddressLongitude}''\n''\n'
        "You will now be directed to the main menu to choose what you want to do."'\n'
        "You can press 'Later' if you wish to do this later.",
        reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
    )
    now = datetime.now()
    Utils.create_new_user(u1.UserID, u1.FirstName, u1.LastName, u1.Birthdate, u1.PhoneNumber,u1.AddressLatitude,u1.AddressLongitude,u1.AddressDescription, u1.ChatID)
    return MENU

    # if the user is already in the Database, we will raise an error and inform the user about it
    # this will be implemented after we connect the bot to the database

def Welcome_back(update: Update, context: CallbackContext) -> int:
    reply_keyboard = [['Menu'], ['Exit']]
    update.message.reply_text(
        'Nice to see you again, feel free to choose what do you want to do',
        reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True),
    )
    return WELCOME

# function cancel that cancels the process and deletes the information about the user
def cancel(update: Update, context: CallbackContext) -> int:
    u1.reset()
    update.message.reply_text(
        "Until next time!"
    )
    return ConversationHandler.END

def done(update: Update, context: CallbackContext) -> int:
    update.message.reply_text(
        "Until next time! stay safe..."'\n'
        "Remember, if you want to call me just type '/start' I'll be happy to help!"
    )
    return ConversationHandler.END

###########################################################################################################################################################
# UPDATE COMMAND
###########################################################################################################################################################
# this command will allow the user to update the information about themselves.
# the user can update the information about himself only if he completed the start phase

def update(update: Update, context: CallbackContext) -> int:
    user = update.message.from_user
    if not Utils.is_registered(user.id, user.first_name) :
        update.message.reply_text(
        "You are not registered. Please type '/start' to register yourself"
        )
        return ConversationHandler.END
    else:   
        reply_keyboard = [['Location', 'Address', 'Nothing']]
        update.message.reply_text(
            "What info would you like to update? Please choose one:",
            reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True),
        )
        return CHOOSE_VALUES_TO_UPDATE

def update_address_bot(update: Update, context: CallbackContext) -> int:
    update.message.reply_text(
        "Please write your new address."
    )
    return U_ADDRESS
def update_address_bot_text(update: Update, context: CallbackContext) -> int:
    text = update.message.text
    user = update.message.from_user
    userid = user.id
    Utils.update_address(userid, text)
    update.message.reply_text(
        "Thank you. Your address have been updated to: "f'{text}'
    )
    return ConversationHandler.END

def update_location_bot(update: Update, context: CallbackContext) -> int:
    update.message.reply_text(
        "Please send me your new location"
    )
    return U_LOCATION

def update_location_bot_text(update: Update, context: CallbackContext) -> int:
    user = update.message.from_user
    userid = user.id
    user_location = update.message.location
    lon = str(user_location.longitude)
    lat = str(user_location.latitude)
    Utils.update_location(userid , lon, lat)
    update.message.reply_text(
        "Thank you. Your location have been updated to: "f'{lat,lon}'
    )
    return ConversationHandler.END

def nothing_to_update(Update: Update, context: CallbackContext) -> int:
    update.message.reply_text(
        "Feel free to update your info anytime!"
    )
    return ConversationHandler.END

###########################################################################################################################################################
# RECORDING OFFER
###########################################################################################################################################################

def donation_type(update: Update, context: CallbackContext) -> int:
    reply_keyboard = [['monetary'], ['medical'],['home essentials'],['clothes'],['academic essentials']]
    update.message.reply_text(
        'God bless you, please choose what type of donation you are willing to offer',
        reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
    )
    return OFFER_DESCRIPTION

def donation_description(update: Update, context: CallbackContext)-> int:
    type1 = update.message.text
    print(type1)
    offer.type = type1
    offer.userID = u1.UserID
    update.message.reply_text(
        'Great! please provide a description of your donation',
    )
    return OFFER_QUANTITY

def donation_quantity(update: Update, context: CallbackContext)-> int:
    desc = update.message.text
    offer.description = desc
    print(desc)
    reply_keyboard = [['1', '5', '15', '20', '50']]
    update.message.reply_text(
        'Thanks, can you specify the quantity/amount you will be providing in integers, ex: 5 (unit)',
        reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
    )
    return OFFER_done

def offer_registered( update: Update, context: CallbackContext)-> int:
    qt = update.message.text
    offer.QuantityAmount = qt
    Utils.add_offer(offer.type, offer.userID, offer.description, offer.QuantityAmount)
    update.message.reply_text(
        'Hope is never lost with a community such as yours, can you deliver this donation yourself to the nearest '
        'center or do you need someone to pick it up when possible ',
    )
    return ConversationHandler.END

###########################################################################################################################################################
# RECORDING NEED/REQUEST
###########################################################################################################################################################

def request_type ( update: Update, context: CallbackContext)-> int:
    request.append(u1.UserID)
    request.append(u1.ChatID)
    reply_keyboard = [['monetary'], ['medical'],['home essentials'],['clothes'],['academic essentials']]
    update.message.reply_text(
        'We will assist you if god wills, please choose what type of need you want to request...',
        reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
    )
    return REQUEST_TYPE

def request_description( update: Update, context: CallbackContext)-> int:
    request_type = update.message.text
    request.append(request_type)
    update.message.reply_text(
        'please provide us with a description of your need...'
    )
    return REQUEST_DESCRIPTION

def request_quantity ( update: Update, context: CallbackContext)-> int:
    print(request)
    description = update.message.text
    request.append(description)
    reply_keyboard = [['1','10','20','100'],['NA']]
    update.message.reply_text(
        'Please provide the quantity or amount needed if your need is quantifiable...',
        reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
    )
    return REQUEST_QUANTITY

# this stage will be used to estimate cash amount needed for non-monetary needs, exp: medicine,laptops,books...
#for now we will skip this stage

##################################~~~~~~~~~~~~~~~~~~~~~~~~~~#############################################################
def ReqCash_estimate(update: Update, context: CallbackContext) -> int:
    reply_keyboard = [['50', '100','200' ,'500','1000'],[' > 1000']]
    update.message.reply_text(
        'can you estimate the amount of cash in thousands LBP necessary to fulfill your need...',
        reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
    )
    return REQUEST_QUANTITY
##################################~~~~~~~~~~~~~~~~~~~~~~~~~~#############################################################

def request_noted(update: Update, context: CallbackContext)-> int:
    quantity = update.message.text
    request.append(quantity)
    print(request)
    reply_keyboard = [['Request'], ['donate'], ['done']]
    update.message.reply_text(
        'Your request has been well received. We are checking if there\'s someone who already donated the item you requested.',
        reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
    )
    user_id = request[0] 
    donation_type_id = request[2]
    request_description = request[3]
    cash_value = 0
    quantity = request[4]
    Utils.add_need(user_id, donation_type_id, request_description, cash_value, quantity)
    return ACTIONS

###########################################################################################################################################################
# REGISTERING A VOLUNTEER
###########################################################################################################################################################

def new_volunteer( update: Update, context: CallbackContext ) -> int  :
    reply_keyboard = [['Yes', 'No']]
    update.message.reply_text(
        "Are you sure you want to be registered as a volunteer ?",
        reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
    )
    return NEW_VOLUNTEER

def added_volunteer(update: Update, context: CallbackContext) -> int :
    reply_keyboard = [['request task'], ['Adieus'],['done']]
    update.message.reply_text(
        "God bless you, you have been added to the list of volunteers. If you want to start delivering items" \
        "to people in need, run the /deliver command.",
        reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
    )
    Utils.add_volunteer(u1.UserID, u1.FirstName, u1.LastName, u1.ChatID)
    return ACTIONS

###########################################################################################################################################################
# DELIVERING ITEMS A.Y
###########################################################################################################################################################

def deliver(update: Update, context: CallbackContext) -> int:

    reply_keyboard = [['I want to deliver items', 'Succeeded in delivering an item', 'Failed in delivering an item'],
                      ['Register as Volunteer']]
    user = update.message.from_user
    if Utils.user_is_volunteer(user.id):
        update.message.reply_text(
            "Welcome back, volunteer! What did you come here for?",
            reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
        )

        return START_DELIVERY
    else:
        reply_keyboard1= [['Register as Volunteer']]
        update.message.reply_text(
            "You cannot deliver any items unless you become a volunteer. If you wish so, Please run the /start " \
            "command and choose the 'Register as Volunteer' action in order for you to register.",
            reply_markup = ReplyKeyboardMarkup(reply_keyboard1, one_time_keyboard=True)
        )
    return ACTIONS

def start_delivering(update: Update, context: CallbackContext) -> int:
    undelivered_items = Utils.get_all_undelivered_items()
    reply = "Below are all the matched items that you can deliver. Choose the Donation ID that mostly suits you:\n"
    for undelivered_item in undelivered_items:
        reply = reply + utilities.create_text_for_donation(undelivered_item)
    update.message.reply_text(reply)
    return CHOOSE_DONATION

def volunteer_chose_donation(update: Update, context: CallbackContext) -> int:
    donation_id = update.message.text
    Utils.set_donation_as_being_delivered(donation_id)
    update.message.reply_text(
        "Thanks for choosing the Donation " + donation_id + " to deliver. God bless you!" 
    )
    return ACTIONS

def delivery_success_id(update: Update, context: CallbackContext) -> int:
    update.message.reply_text(
        "Please enter the delivery_id we provided you to mark it in our DB as successful"   
    )
    return DELIVERY_SUCCESS


def delivery_failure_id(update: Update, context: CallbackContext) -> int:
    update.message.reply_text(
        "Please enter the delivery_id we provided you to mark it in our DB as failure. But don't worry, there are "\
        "Many good people like you who are willing to help, and they will deliver the items!"   
    )
    return DELIVERY_FAILURE


def mark_delivery_as_success(update: Update, context: CallbackContext) -> int:
    delivery_id = update.message.text
    Utils.mark_delivery_as_success(int(delivery_id))
    update.message.reply_text(
        "Thanks for helping people.. God bless you!"   
    )
    return START_DELIVERY


def mark_delivery_as_failure(update: Update, context: CallbackContext) -> int:
    delivery_id = update.message.text
    Utils.mark_delivery_as_failure(int(delivery_id))
    update.message.reply_text(
        "Thanks for trying. We will reset this delivery so that someone else may do it. Thanks for your time!"   
    )
    return START_DELIVERY

###########################################################################################################################################################
# PICKUP
###########################################################################################################################################################

def pickup_offers(update: Update, context: CallbackContext) -> int:
    user = update.message.from_user
    user_id = user.id
    if not Utils.user_is_volunteer(user_id):
        update.message.reply_text(
             "Your are not registerd as a volunteer. Please type '/start' to register as one."
         )
        return ConversationHandler.END
    else:
        reply_keyboard = [['Yes', 'Cancel']]
        a = utilities.get_UnpickedUpOffers()
        update.message.reply_text(
            "These are the offers that are available for pickup:"
         )
        update.message.reply_text(
            a
         )
        update.message.reply_text(
            "Do you want to pickup one of the offers?",
            reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True),
         )
        return CHOOSE_OFFER

def choose_offer(update: Update, context: CallbackContext) -> int:
    update.message.reply_text(
             "Please type the offer ID that you want to pickup."
         )
    return SAVE_OFFER

def save_offer(update: Update, context: CallbackContext) -> int:    
    user = update.message.from_user
    user_id = user.id
    text = update.message.text

    offerid = int(text)
    chatid = Utils.get_donorid_from_offer(offerid)
    pn = Utils.get_phonenumber(user_id)

    context.bot.send_message(chat_id= chatid,text = "A Volunteer will pickup your offer.")
    context.bot.send_message(chat_id= chatid,text = "The Volunteer's information are:")
    msg1 = "First name: "+str(user.first_name)
    context.bot.send_message(chat_id= chatid,text = msg1)
    msg2 = "Last name: "+str(user.last_name)
    context.bot.send_message(chat_id= chatid,text = msg2)
    msg3 = "Phone number: "+str(pn)
    context.bot.send_message(chat_id= chatid,text = msg3)

    utilities.update_offer_assigned(offerid, user_id)

    donor_details= utilities.details_of_user(chatid)
    update.message.reply_text(
             "Thankyou! The Donor of the offer have been informed. You should also contact the donor to take the offer from him."'\n'
             "These are the donor\'s details: "'\n'
         )
    update.message.reply_text(
             donor_details
         )

    return ConversationHandler.END

###########################################################################################################################################################
# UPDATE_PICKUP
###########################################################################################################################################################

def ask_for_offerid(update: Update, context: CallbackContext) -> int:
    user = update.message.from_user
    user_id = user.id
    a = utilities.show_assignedOffers( user_id)

    update.message.reply_text(
             "If you have picked up an offer, please provide me with it\'s offer ID"
         )
    update.message.reply_text(
            "These are your assigned offers: "
         )
    update.message.reply_text(
            a
         )
    return ASK_OFFER_ID

def update_pickup(update: Update, context: CallbackContext) -> int:
    user = update.message.from_user
    user_id = user.id
    text = update.message.text

    offerid = int(text)

    utilities.set_offer_pickedup(offerid, user_id)

    update.message.reply_text(
             "Thank you! We are now up-to-date with you."
         )
    return ConversationHandler.END

###########################################################################################################################################################
# NEEDS
###########################################################################################################################################################

def show_needs(update: Update, context: CallbackContext) -> int:
    user = update.message.from_user
    user_id = user.id
    if not Utils.user_is_volunteer(user_id):
        update.message.reply_text(
             "Your are not registerd as a volunteer. Please type '/start' to register as one."
         )
        return ConversationHandler.END

    else:
        reply_keyboard = [['Yes', 'Cancel']]
        a = utilities.get_UndeliveredNeeds()
        update.message.reply_text(
            "These are the undelivered needs that you can deliver:"
        )
        update.message.reply_text(
            a
        )
        update.message.reply_text(
            "Do you want to deliver one of the needs?",
            reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True),
        )

        return DELIVER_NEEDS

def choose_need(update: Update, context: CallbackContext) -> int:
    update.message.reply_text(
             "Please type the need ID that you want to deliver"
     )       

    return UPDATE_NEED

def update_need(update: Update, context: CallbackContext) -> int:
    user = update.message.from_user
    user_id = user.id
    text = update.message.text

    needid = int(text)
    chatid = Utils.get_victimid_from_need(needid)
    pn = Utils.get_phonenumber(user_id)

    context.bot.send_message(chat_id= chatid,text = "A Volunteer will deliver to you your need.")
    context.bot.send_message(chat_id= chatid,text = "The Volunteer's information are:")
    msg1 = "First name: "+str(user.first_name)
    context.bot.send_message(chat_id= chatid,text = msg1)
    msg2 = "Last name: "+str(user.last_name)
    context.bot.send_message(chat_id= chatid,text = msg2)
    msg3 = "Phone number: "+str(pn)
    context.bot.send_message(chat_id= chatid,text = msg3)

    utilities.update_need_assigned(needid, user_id)

    victim_details= utilities.details_of_user(chatid)
    update.message.reply_text(
             "Thankyou! The person in need have been informed. You should also contact this person to deliver his need to him."'\n'
             "These are the person\'s details: "'\n'
         )
    update.message.reply_text(
             victim_details
         )

    update.message.reply_text(
             "Thank you! You have been assigned this need."
         )
    return ConversationHandler.END

###########################################################################################################################################################
# upadtes_Delivered_needs
###########################################################################################################################################################

def ask_for_needid(update: Update, context: CallbackContext) -> int:
    user = update.message.from_user
    user_id = user.id

    a = utilities.show_assignedNeeds(user_id)

    update.message.reply_text(
             "If you have picked up a need to deliver, please provide me with it\'s need ID"
         )
    update.message.reply_text(
            "These are your assigned needs to deliver: "
         )
    update.message.reply_text(
            a
         )
    return ASK_NEED_ID

def update_need_pickedup(update: Update, context: CallbackContext) -> int:
    user = update.message.from_user
    user_id = user.id
    text = update.message.text

    needid = int(text)

    utilities.set_need_delivered(needid, user_id)

    update.message.reply_text(
            "Thank you! We are now up-to-date with you."
        )

    return ConversationHandler.END



