from telegram.ext import ConversationHandler, MessageHandler, CommandHandler, Filters, CallbackContext, Updater
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, Update
from bot_actions import *
from telegram import Location
import telegram.ext
import telegram

def create_start_handler():

    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # BOT TOKEN is a token unique for each bot. This Token cannot be shared because it will allow anyone to control the bot



    start_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start),
                      CommandHandler('deliver', deliver)
                      ],
        states = {
            CHOOSING: [
                MessageHandler(Filters.regex('^Cancel$'), cancel),
                MessageHandler(Filters.regex('^Yes! All good$'), phone_number),
            ],
            PHONE_NUMBER: [
                MessageHandler(Filters.regex('^Cancel$'), done),
                MessageHandler(Filters.text, phone_number_text),
            ],
            PHONE_NUMBER_YN: [
                MessageHandler(Filters.regex('^Yes$'), birthdate ),
                MessageHandler(Filters.regex('^No$'), phone_number),
                MessageHandler(Filters.regex('^Cancel$'), done),
            ],
            BIRTHDATE: [
                MessageHandler(Filters.regex('^Cancel$'), done),
                MessageHandler(Filters.text, birthdate_text),
            ],
            BIRTHDATE_YN: [
                MessageHandler(Filters.regex('^Yes$'), address ),
                MessageHandler(Filters.regex('^No$'), birthdate),
                MessageHandler(Filters.regex('^Cancel$'), done),
            ],
            ADDRESS: [
                MessageHandler(Filters.regex('^Cancel$'), done),
                MessageHandler(Filters.text, address_text),
            ],
            ADDRESS_YN: [
                MessageHandler( Filters.regex('^Yes$'), ask_location),
                MessageHandler( Filters.regex('^No$'), address),
                MessageHandler(Filters.regex('^Cancel$'), done),
            ],
            LOCATION: [
                MessageHandler(Filters.regex('^Cancel$'), done),
                MessageHandler( Filters.location, location),
            ],
            CONCLUDE: [
                MessageHandler(Filters.regex('^Cancel$'), cancel),
                MessageHandler(Filters.regex('^Sure!$'), received_information),
            ],
            MENU: [
                MessageHandler(Filters.regex('^Ok, Sounds Good!$'),actions),
                MessageHandler(Filters.regex('^Later$'), done),
            ],
            WELCOME: [
                MessageHandler(Filters.regex('^Menu$'), actions),
                MessageHandler(Filters.regex('^Exit$'), done),
            ],
            ACTIONS: [
                MessageHandler(Filters.regex('^Donate$'), donation_type ),
                MessageHandler(Filters.regex('^Request$'), request_type),
                MessageHandler(Filters.regex('^Volunteer$') | Filters.regex('^Register as Volunteer$'), new_volunteer),
                MessageHandler(Filters.regex('^deliver$') | Filters.regex('^Deliver$'), deliver) ,
                MessageHandler(Filters.regex('^Update Pickup$'), ask_for_offerid ),
                MessageHandler(Filters.regex('^Show Offers$'), pickup_offers),
                MessageHandler(Filters.regex('^Show Needs$'), show_needs),
                MessageHandler(Filters.regex('^Update on Delivered Needs$'), ask_for_needid),
                MessageHandler(Filters.regex('^Nothing$') | Filters.regex('^Done$'), done),
                MessageHandler(Filters.regex('^Create Campaign$'), start_campaign),
            ],
            REQUEST_TYPE: [
                MessageHandler(Filters.regex('^Cancel$'), done),
                MessageHandler(Filters.text, request_description),
            ],
            REQUEST_DESCRIPTION: [
                MessageHandler(Filters.regex('^Cancel$'), done),
                MessageHandler(Filters.text, request_quantity),
            ],
            REQUEST_QUANTITY: [
                MessageHandler(Filters.regex('^Cancel$'), done),
                MessageHandler(Filters.text, request_noted),
            ],
            REQUEST_NOTED: [
                MessageHandler(Filters.regex('^done$') | Filters.regex('^Done$'), done),
                MessageHandler(Filters.text, offer_registered),
            ],
            OFFER_TYPE: [
                MessageHandler(Filters.regex('^Cancel$'), done),
                MessageHandler(Filters.text, donation_type),
            ],
            OFFER_DESCRIPTION: [
                MessageHandler(Filters.regex('^Cancel$'), done),
                MessageHandler( Filters.text, donation_description),
            ],
            OFFER_QUANTITY: [
                MessageHandler(Filters.regex('^Cancel$'), done),
                MessageHandler(Filters.text, donation_quantity),
            ],
            OFFER_done: [
                MessageHandler(Filters.regex('^done$') | Filters.regex('^Done$'), done),
                MessageHandler( Filters.text, offer_registered),
            ],
            NEW_VOLUNTEER: [
                MessageHandler(Filters.regex('^Yes$'), added_volunteer),
                MessageHandler(Filters.regex('^No$'), actions),
                MessageHandler(Filters.regex('^Cancel$'), done),
            ],
            START_DELIVERY: [
                MessageHandler(Filters.regex('^I want to deliver items$'), start_delivering),
                MessageHandler(Filters.regex('^Succeeded in delivering an item$'), delivery_success_id),
                MessageHandler(Filters.regex('^Failed in delivering an item$'), delivery_failure_id),
                MessageHandler(Filters.regex('^Register as Volunteer$'), new_volunteer),
                MessageHandler(Filters.regex('^Cancel$'), done),

            ],
            CHOOSE_DONATION: [
                MessageHandler(Filters.regex('^Cancel$'), done),
                MessageHandler(Filters.text, volunteer_chose_donation),
            ],
            DELIVERY_SUCCESS: [
                MessageHandler(Filters.regex('^Cancel$'), done),
                MessageHandler(Filters.text, mark_delivery_as_success),
            ],
            DELIVERY_FAILURE: [
                MessageHandler(Filters.regex('^Cancel$'), done),
                MessageHandler(Filters.text, mark_delivery_as_failure),
            ],
            CHOOSE_OFFER: [
                MessageHandler(Filters.regex('^Yes$'), choose_offer),
                MessageHandler(Filters.regex('^Cancel$'), done)
            ],
            SAVE_OFFER: [
                MessageHandler(Filters.regex('^Cancel$'), done),
                MessageHandler(Filters.text, save_offer),
            ],
            ASK_OFFER_ID: [
                MessageHandler(Filters.regex('^Cancel$'), done),
                MessageHandler(Filters.text, update_pickup),
            ],
            DELIVER_NEEDS: [
                MessageHandler(Filters.regex('^Yes$'), choose_need),
                MessageHandler(Filters.regex('^Cancel$'), done)
            ],
            UPDATE_NEED: [
                MessageHandler(Filters.regex('^Cancel$'), done),
                MessageHandler(Filters.text, update_need),
            ],
            ASK_NEED_ID: [
                MessageHandler(Filters.regex('^Cancel$'), done),
                MessageHandler(Filters.text, update_need_pickedup),
            ],
            NEW_DONATION_TYPE: [
                MessageHandler(Filters.regex('^Cancel$'), done),
                MessageHandler(Filters.text, new_donation_type),
            ],
            ESTIMATING_NEW_DONATION_VALUE: [
                MessageHandler(Filters.regex('^Cancel$'), done),
                MessageHandler(Filters.text, estimating_new_donation_value),
            ],
            NEW_REQUEST_TYPE: [
                MessageHandler(Filters.regex('^Cancel$'), done),
                MessageHandler(Filters.text, new_request_type),
            ],
            ESTIMATING_NEW_NEED_VALUE: [
                MessageHandler(Filters.regex('^Cancel$'), done),
                MessageHandler(Filters.text, estimating_new_need_value),
            ],
            GO_MENU: [
                MessageHandler(Filters.regex('^Menu$'), actions),
                MessageHandler(Filters.regex('^Exit$'), done)
            ],
            START_CAMP: [
                MessageHandler(Filters.regex('^Sounds good, let\'s go!$'), camp_name),
                MessageHandler(Filters.regex('^Exit$'), done)
            ],
            CAMP_NAME: [
                MessageHandler(Filters.regex('^Cancel$'), done),
                MessageHandler(Filters.text, camp_name_text),
            ],
            CAMP_D: [
                MessageHandler(Filters.regex('^Cancel$'), done),
                MessageHandler(Filters.text, camp_description),
            ],
            CAMP_L: [
                MessageHandler(Filters.regex('^Cancel$'), done),
                MessageHandler( Filters.location,camp_location),
            ],
            CONCLUDE_CAMP: [
                MessageHandler(Filters.regex('^Sure!$'), received_information_camp),
                MessageHandler(Filters.regex('^Cancel$'), cancel_camp),
            ]
        },
        fallbacks = [
            MessageHandler(Filters.regex('^cancel$')| Filters.regex('^Cancel$'), cancel),
            MessageHandler(Filters.regex('^done$') | Filters.regex('^Done$'), done),
            MessageHandler(Filters.regex('^deliver$'), deliver),
            CommandHandler('deliver', deliver)
        ],
    )



    return start_handler


def create_update_handler():
    update_handler = ConversationHandler(
        entry_points=[CommandHandler('update', update)],
        states = {
            CHOOSE_VALUES_TO_UPDATE: [
                MessageHandler( Filters.regex('^Nothing$'), nothing_to_update),
                MessageHandler( Filters.regex('^Location$'), update_location_bot),
                MessageHandler( Filters.regex('^Address$'), update_address_bot),
                MessageHandler(Filters.regex('^Register as Volunteer$'), new_volunteer),
                MessageHandler(Filters.regex('^Cancel$'), done),
                # MessageHandler(Filters.regex('^Add need$'), u_address)
            ],
            U_ADDRESS: [
                MessageHandler(Filters.regex('^Cancel$'), done),
                MessageHandler(Filters.text, update_address_bot_text),
            ],
            U_LOCATION: [
                MessageHandler(Filters.regex('^Cancel$'), done),
                MessageHandler(Filters.location, update_location_bot_text),
            ],
        },
        fallbacks=[MessageHandler(Filters.regex('^Done$'), done)],
    )
    return update_handler

def create_delivery_handler():
    deliver_handler = ConversationHandler(
        entry_points=[CommandHandler('deliver', deliver)],
        states = {
            START_DELIVERY: [
                MessageHandler(Filters.regex('^I want to deliver items$'), start_delivering),
                MessageHandler(Filters.regex('^Succeeded in delivering an item$'), delivery_success_id),
                MessageHandler(Filters.regex('^Failed in delivering an item$'), delivery_failure_id),
                MessageHandler(Filters.regex('^Register as Volunteer$'), new_volunteer),
                MessageHandler(Filters.regex('^Cancel$'), done),

            ],
            CHOOSE_DONATION: [
                MessageHandler(Filters.regex('^Cancel$'), done),
                MessageHandler(Filters.text, volunteer_chose_donation),
            ],
            DELIVERY_SUCCESS: [
                MessageHandler(Filters.regex('^Cancel$'), done),
                MessageHandler(Filters.text, mark_delivery_as_success),
            ],
            DELIVERY_FAILURE: [
                MessageHandler(Filters.regex('^Cancel$'), done),
                MessageHandler(Filters.text, mark_delivery_as_failure),
            ]
        },
        fallbacks=[MessageHandler(Filters.regex('^Done$'), done)],
    )
    return deliver_handler

def create_pickup_handler():
    
    pickup_handler = ConversationHandler(
        entry_points=[CommandHandler('Offers', pickup_offers)],
        
        states = {
            CHOOSE_OFFER: [
                MessageHandler(Filters.regex('^Yes$'), choose_offer),
                MessageHandler(Filters.regex('^Cancel$'), done)
            ],
            SAVE_OFFER: [
                MessageHandler(Filters.regex('^Cancel$'), done),
                MessageHandler(Filters.text, save_offer),
            ]

        },
        fallbacks=[MessageHandler(Filters.regex('^Done$'), done)],
    )
    return pickup_handler

def create_update_pickup_handler():
    update_pickup_handler = ConversationHandler(
        entry_points=[CommandHandler('Update_Pickup', ask_for_offerid)],
        states = {
            ASK_OFFER_ID: [
                MessageHandler(Filters.regex('^Cancel$'), done),
                MessageHandler(Filters.text, update_pickup),
            ]
        },
        fallbacks=[MessageHandler(Filters.regex('^Done$'), done)],
    )
    return update_pickup_handler

def create_need_handler():
    
    need_handler = ConversationHandler(
        entry_points=[CommandHandler('Needs', show_needs)],
        
        states = {
            DELIVER_NEEDS: [
                MessageHandler(Filters.regex('^Yes$'), choose_need),
                MessageHandler(Filters.regex('^Cancel$'), done)
            ],
            UPDATE_NEED: [
                MessageHandler(Filters.regex('^Cancel$'), done),
                MessageHandler(Filters.text, update_need),
            ]

        },
        fallbacks=[MessageHandler(Filters.regex('^Done$'), done)],
    )
    return need_handler

def create_update_need_handler():
    
    update_need_handler = ConversationHandler(
        entry_points=[CommandHandler('Update_Need', ask_for_needid)],
        
        states = {
            ASK_NEED_ID: [
                MessageHandler(Filters.regex('^Cancel$'), done),
                MessageHandler(Filters.text, update_need_pickedup),
            ]

        },
        fallbacks=[MessageHandler(Filters.regex('^Done$'), done)],
    )
    return update_need_handler

# def create_cancel_handler():
#     cancel_handler = ConversationHandler(
#         entry_points=[CommandHandler('Cancel', )],
#         states = {
#         },
#         fallbacks=[MessageHandler(Filters.regex('^Done$'), done)],
#     )
#     return cancel_handler

def create_confirm_delivery_handler():
    
    confirm_delivery_handler = ConversationHandler(
        entry_points=[CommandHandler('Confirm_Delivery',confirm_delivery )],
        
        states = {
            CHOOSE_CONFIRM: [
                MessageHandler(Filters.regex('^I received the delivery$'), delivery_received),
                MessageHandler(Filters.regex('^I haven\'t received the deilvery$'),delivery_not_received),
                MessageHandler(Filters.regex('^Cancel$'), done),
            ],
            RECEIVED_NEED: [
                MessageHandler(Filters.regex('^Cancel$'), done),
                MessageHandler(Filters.text, delivery_received_DB),
            ],
            NOT_RECEIVED_NEED: [
                MessageHandler(Filters.regex('^Cancel$'), done),
                MessageHandler(Filters.text, delivery_not_received_DB),
            ]
        
        },
        fallbacks=[MessageHandler(Filters.regex('^Done$'), done)],
    )
    return confirm_delivery_handler