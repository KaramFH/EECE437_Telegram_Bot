from utilities import db_utilities, general_utilities, bot_states
from telegram import ReplyKeyboardMarkup

def run_cancel_command(update: Update, context: CallbackContext) -> int:
    reply_keyboard = [['Cancel Offer', 'Cancel Need']]
    user = update.message.from_user
    if db_utilities.user_is_volunteer(user.id):
        reply_keyboard.append('Cancel Pickup')
        reply_keyboard.append('Cancel Delivery')

    update.message.reply_text(
        "Please choose which action do you wish to cancel.",
        reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True),
    )
    
    return bot_states.CANCEL_OPTION_CHOSEN

def cancel_offer_chosen(update: Update, context: CallbackContext) -> int:
    user = update.message.from_user
    # The offer should be not picked up in order for the user to cancel it
    # Ma ma3e ldatabase ljdid. 3mala enta :*
    user_offers = db_utilities.get_all_offers_of_user()
    if user_offers.__len__ == 0:
        update.message.reply_text(
            'You don\'t have any offerings for now. Please choose another action to cancel, or type "Done".',
        )
        return bot_states.CANCEL_OPTION_CHOSEN
    else:
        offers_display = general_utilities.build_user_friendly_offers(user_offers)
        update.message.reply_text(
            "Please choose the ID of the offering you wish to cancel: \n" + offers_display,
        )
        return bot_states.CANCEL_OFFERING_ID_CHOSEN

def cancel_offering_by_id(update: Update, context: CallbackContext) -> int:
    try:
        offering_id = int(update.message.text)
        db_utilities.delete_offering(offering_id)
        update.message.reply_text(
            "Your offering of ID: " + offering_id + " is deleted successfully",
        )
    except:
        update.message.reply_text(
            "It seems you entered an invalid ID. Please try again.",
        )
        return bot_states.CANCEL_OFFER_CHOSEN
        # 2. If the offer is assigned to a volunteer, send a message to the volunteer to update
        # him about the offer and update his info in the db.
        # Ma fhemta

    pass

def cancel_need_chosen(update: Update, context: CallbackContext) -> int:
    # Cancel Need
    # 1. Give the user the needs he had posted so he can choose which one he wants to
    # cancel. (not done)
    # If he didn’t post any need, tell him so.
    # The need should not be delivered in order for the victim to cancel it
    # 2. If the need is assigned to a volunteer, send a message to the volunteer to update
    # him about the need and update his info in the db.
    # 3. Change the database entries related to the action
    pass

def cancel_pickup_chosen(update: Update, context: CallbackContext) -> int:
    # Cancel Pickup
    # 2. Give the user his assigned offers to pick up so he can choose which offer he wants to
    # cancel pick up (already done)
    # 3. Change the database entries related to the action
    pass

def cancel_delivery_chosen(update: Update, context: CallbackContext) -> int:
    # Cancel Delivery
    # 2. Give the user his assigned needs to deliver so he can choose which need he wants to
    # cancel delivery (already done)
    # 3. Change the database entries related to the action

    pass