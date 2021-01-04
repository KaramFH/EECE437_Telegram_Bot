from telegram.ext import ConversationHandler, MessageHandler, CommandHandler, Filters, CallbackContext, Updater
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, Update
from actions.cancel_actions import *
from bot_states import *
from actions.bot_actions import *
from telegram import Location
import telegram.ext
import telegram

def create_start_handler():

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
                MessageHandler(Filters.text, phone_number_text)
            ],
            PHONE_NUMBER_YN: [
                MessageHandler(Filters.regex('^Yes$'), birthdate ),
                MessageHandler(Filters.regex('^No$'), phone_number),
            ],
            BIRTHDATE: [
                MessageHandler(Filters.text, birthdate_text)
            ],
            BIRTHDATE_YN: [
                MessageHandler(Filters.regex('^Yes$'), address ),
                MessageHandler(Filters.regex('^No$'), birthdate),
            ],
            ADDRESS: [
                MessageHandler(Filters.text, address_text)
            ],
            ADDRESS_YN: [
                MessageHandler( Filters.regex('^Yes$'), ask_location),
                MessageHandler( Filters.regex('^No$'), address),
            ],
            LOCATION: [
                MessageHandler( Filters.location, location)
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
                MessageHandler(Filters.regex('^Update on picked up needs$'), ask_for_needid),
                MessageHandler(Filters.regex('^done$') | Filters.regex('^Done$'), done)
            ],
            REQUEST_TYPE: [
                MessageHandler(Filters.text, request_description)
            ],
            REQUEST_DESCRIPTION: [
                MessageHandler(Filters.text, request_quantity)
            ],
            REQUEST_QUANTITY: [
                MessageHandler(Filters.text, request_noted)
            ],
            REQUEST_NOTED: [
                MessageHandler(Filters.text, offer_registered),
                MessageHandler(Filters.regex('^done$') | Filters.regex('^Done$'), done)
            ],
            OFFER_TYPE: [
                MessageHandler(Filters.text, donation_type)
            ],
            OFFER_DESCRIPTION: [
                MessageHandler( Filters.text, donation_description)
            ],
            OFFER_QUANTITY: [
                MessageHandler(Filters.text, donation_quantity)
            ],
            OFFER_done: [
                MessageHandler( Filters.text, offer_registered),
                MessageHandler(Filters.regex('^done$') | Filters.regex('^Done$'), done)
            ],
            NEW_VOLUNTEER: [
                MessageHandler(Filters.regex('^Yes$'), added_volunteer),
                MessageHandler(Filters.regex('^No$'), actions)
            ],
            START_DELIVERY: [
                MessageHandler(Filters.regex('^I want to deliver items$'), start_delivering),
                MessageHandler(Filters.regex('^Succeeded in delivering an item$'), delivery_success_id),
                MessageHandler(Filters.regex('^Failed in delivering an item$'), delivery_failure_id),
                MessageHandler(Filters.regex('^Register as Volunteer$'), new_volunteer)

            ],
            CHOOSE_DONATION: [
                MessageHandler(Filters.text, volunteer_chose_donation)
            ],
            DELIVERY_SUCCESS: [
                MessageHandler(Filters.text, mark_delivery_as_success)
            ],
            DELIVERY_FAILURE: [
                MessageHandler(Filters.text, mark_delivery_as_failure)
            ],
            CHOOSE_OFFER: [
                MessageHandler(Filters.regex('^Yes$'), choose_offer),
                MessageHandler(Filters.regex('^Cancel$'), done)
            ],
            SAVE_OFFER: [
                MessageHandler(Filters.text, save_offer)
            ],
            ASK_OFFER_ID: [
                MessageHandler(Filters.text, update_pickup)
            ],
            DELIVER_NEEDS: [
                MessageHandler(Filters.regex('^Yes$'), choose_need),
                MessageHandler(Filters.regex('^Cancel$'), done)
            ],
            UPDATE_NEED: [
                MessageHandler(Filters.text, update_need)
            ],
            ASK_NEED_ID: [
                MessageHandler(Filters.text, update_need_pickedup)
            ],
            NEW_DONATION_TYPE: [
                MessageHandler(Filters.text, new_donation_type)
            ],
            ESTIMATING_NEW_DONATION_VALUE: [
                MessageHandler(Filters.text, estimating_new_donation_value)
            ],
            NEW_REQUEST_TYPE: [
                MessageHandler(Filters.text, new_request_type)
            ],
            ESTIMATING_NEW_NEED_VALUE: [
                MessageHandler(Filters.text, estimating_new_need_value)
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
                MessageHandler(Filters.regex('^Register as Volunteer$'), new_volunteer)
                # MessageHandler(Filters.regex('^Add need$'), u_address)
            ],
            U_ADDRESS: [
                MessageHandler(Filters.text, update_address_bot_text)
            ],
            U_LOCATION: [
                MessageHandler(Filters.location, update_location_bot_text)
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
                MessageHandler(Filters.regex('^Register as Volunteer$'), new_volunteer)

            ],
            CHOOSE_DONATION: [
                MessageHandler(Filters.text, volunteer_chose_donation)
            ],
            DELIVERY_SUCCESS: [
                MessageHandler(Filters.text, mark_delivery_as_success)
            ],
            DELIVERY_FAILURE: [
                MessageHandler(Filters.text, mark_delivery_as_failure)
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
                MessageHandler(Filters.text, save_offer)
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
                MessageHandler(Filters.text, update_pickup)
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
                MessageHandler(Filters.text, update_need)
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
                MessageHandler(Filters.text, update_need_pickedup)
            ]

        },
        fallbacks=[MessageHandler(Filters.regex('^Done$'), done)],
    )
    return update_need_handler

def create_cancel_handler():
    cancel_handler = ConversationHandler(
        entry_points=[CommandHandler('Cancel', run_cancel_command)],
        states = {
            CANCEL_OPTION_CHOSEN: [
                MessageHandler(Filters.regex('^Cancel Offer$'), cancel_offer_chosen),
                MessageHandler(Filters.regex('^Cancel Need$'), cancel_need_chosen),
                MessageHandler(Filters.regex('^Cancel Pickup$'), cancel_pickup_chosen),
                MessageHandler(Filters.regex('^Cancel Delivery$'), cancel_delivery_chosen)
            ],
            CANCEL_OFFERING_ID_CHOSEN: [
                MessageHandler(Filters.text, cancel_offering_by_id)
            ],
        },
        fallbacks=[MessageHandler(Filters.regex('^Done$'), done)],
    )
    return cancel_handler