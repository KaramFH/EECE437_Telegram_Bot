import utilities
from volunteerstate import VolunteerState as states
from donation_types import donation_types
from datetime import datetime
from utilities import *
import mysql.connector

from geopy import distance #library that deals with coordinates and geographical distances

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="db437"
)
cr = mydb.cursor()

def create_new_user(userID1, firstname, lastname, birthdate, PhoneNumber,latitude, longitude,address, chatID):
    query = "INSERT into user (userID, firstname, lastname, birthdate, PhoneNumber, addresslatitude, addresslongitude, addressdescription, chatID) VALUES ( " \
            " %d, '%s', ' %s', '%s','%s','%s','%s','%s', %d)" % (int(userID1) , firstname, lastname, birthdate, PhoneNumber,latitude,longitude,address, chatID)
    # q1 = query.format(userID1, firstname, lastname, birthdate, PhoneNumber, chatID)
    print(query)
    cr.execute(query)
    mydb.commit()
    print("user %s added " % firstname)

def get_phonenumber(userid):
    query = "SELECT phonenumber FROM user WHERE userid = " + str(userid)
    cr.execute(query)
    p = cr.fetchall()
    return p[0][0]


def add_volunteer(userID, firstname, lastname, chatid):
    state = states.FREE.value			# use enum for volunteer state
    query_template = "INSERT into volunteer (userID, chatid, firstname, Lastname, state) VALUES (%d, %d, '%s', '%s', %d )"
    query = query_template % (int(userID), int(chatid), firstname, lastname, state)
    print(query)
    cr.execute(query)
    mydb.commit()
    print("done executing")


def get_type_id_from_type_name(typename):
    query = "SELECT donationtypeid FROM donationtype WHERE donationtypename = %s" % typename
    cr.execute(query)
    return cr.fetchall()[0]

def add_offer(typename, userID, description ,QtAmount):
    # A.Y: I deleted the below line because we no longer need the donation_types
    # typeID  =  donation_types.get(typename)
    typeID = get_type_id_from_type_name(typename)
    print('lets see what we got...')
    print(typeID, userID, description, QtAmount)
    query = "INSERT into offering (userID, DonationTypeID, description, QuantityAmount, quantityremaining, isActive) " \
            "VALUES " \
            "(%d,%d,' %s ', %d,%d ,%d ) " % ( int(userID) , int(typeID), description, int(QtAmount), int(QtAmount), 1)
    print(query)
    cr.execute(query)
    mydb.commit()
    print("done executing")

def add_need(userID, donation_type_name, description, cashValue, quantityAmount):  # by default db sets active = 1
    # A.Y on 3-1-2020 same as add_offer function above.
    # typeID = donation_types.get(donation_type_name)
    typeID = get_type_id_from_type_name(donation_type_name)
    query_template = "INSERT into need (Donationtypeid, userID, description, cashValue, quantityAmount, quantityremaining) VALUES (" \
            "{}, {}, '{}', {}, {}, {})"
    query = query_template.format(typeID, userID, description, cashValue, quantityAmount, quantityAmount)
    cr.execute(query)
    mydb.commit()
    print("done adding request")

def is_registered(id, firstname) -> bool:
    query = "SELECT firstname from user where userid = " + str(id)
    cr.execute(query)
    users = cr.fetchall()
    if users.__len__() >= 1 and (users[0][0].lower() == firstname.lower()):
        print("yes, %s is registered" % (firstname))
        return True
    return False

def get_all_types_as_list():
    query = "SELECT donationtypename FROM donationtype"
    cr.execute(query)
    donation_types = cr.fetchall()
    donation_types_names = []
    for d_type in donation_types:
        donation_types_names.append([d_type[0]])
    donation_types_names.append(['other'])
    #print("donation_types = " + donation_types)
    return donation_types

# A.Y: create new donation type:
def create_new_donationtype(donation_type_name, estimated_value):
    query = "INSERT INTO donationtype (donationtypename, value, isvalidated) VALUES (%s, %s)" \
            % (donation_type_name, str(estimated_value), 0)
    cr.execute(query)
    mydb.commit()
    print("new donation type inserted.")

def get_user_by_id(id):
    query = "SELECT userid, firstname, chatId from user where userid <= " + str(id)
    cr.execute(query)
    users = cr.fetchall()
    print(users[1][0])
    return (users)

def get_volunteer_by_id(id):
    query = "SELECT userid, name, contactinfo from volunteer where userid = " + str(id)
    cr.execute(query)
    users = cr.fetchall()
    print(users[0][0])
    return (users[0][0])

# Admin Queries:
def create_new_admin(name, address):
    query = "INSERT into admins (Name, Address) VALUES (%s, %s)" % (name, address)
    cr.execute(query)
    mydb.commit()
    print("Created a new admin with name %s and address %s" % (name, address))

def add_user(name, address, contactinfo):
    query = "INSERT into user (Name, Address, phonenumber) VALUES (%s, %s, %s)"
    values = (name, address, contactinfo)
    cr.execute(query % values)
    mydb.commit()
    print("New user created successfully")

def remove_user(userid) :
    query = "DELETE FROM user WHERE usreid = " + str(userid)
    cr.execute(query)
    mydb.commit()
    print("A user was removed successfully")


def remove_volunteer(id):
    query = "DELETE FROM volunteer WHERE volunteerID = " + str(id)
    cr.execute(query)
    mydb.commit()
    print("A volunteer was removed successfully")


def update_location(userid , longitude , latitude ):

    query = " UPDATE user SET addresslongitude = '{}', addresslatitude = '{}' WHERE userid = {} " 
    q = query.format(longitude, latitude,userid)
    cr.execute(q)
    mydb.commit() 

def update_address(userid , address ):
    query = " UPDATE user SET addressdescription = '{}' WHERE userid = {} " 
    q = query.format(address, userid)
    cr.execute(q)
    mydb.commit() 

########################################################################################################

def fetch_all_needs_of_type(typeID) :

    query = "SELECT NeedID, userID, DonationtypeID, CashValue, QuantityRemaining FROM need " \
            "WHERE " \
            "donationtypeid = {} ORDER " \
            "BY QuantityRemaining " \
            "DESC "
    cr.execute(query.format(typeID))
    needs = cr.fetchall()
    return needs

def get_offers_of_type(typeID):
    query = "SELECT offeringID, donationtypeID,  quantityAmount, QuantityRemaining FROM " \
            "offering where donationtypeID = {} AND isActive = 1 ORDER BY " \
            "Quantityremaining DESC"
    cr.execute(query.format(typeID))
    offers = cr.fetchall()
    return offers

def get_all_monetary_offers():
    monetaryTypeID = 1
    query = "SELECT offerID, userID, donationtypeID, QuantityRemaining " \
            "FROM offering where donationtypeID = {} ORDER BY quantityremaining ASC".format(monetaryTypeID)
    cr.execute(query)
    cash_offers = cr.fetchall()
    return cash_offers

def set_matched(needID, offerID) :

    query = "INSERT into donationlog ( offeringID, NeedID, isdelivered) VALUES ({}, {},  0)"
    now = datetime.now()
    query = query.format(needID, offerID, now)
    print (query)
    cr.execute(query)
    print("matching made, added entry to table donation")
    mydb.commit()

# A.Y
def user_is_volunteer(user_id):
    query = "SELECT * FROM volunteer WHERE userid = " + str(user_id)
    cr.execute(query)
    return cr.fetchall().__len__() >= 1

def set_volunteer_assignedTask( userid) :
    query = "UPDATE volunteer set state = 2 WHERE userid = "+ str(userid)
    cr.execute(query)
    mydb.commit()


def set_volunteer_delivering(userid):
    query = "UPDATE volunteer set state = 3 WHERE userid = " + str(userid)
    cr.execute(query)
    mydb.commit()



def get_all_undelivered_items():
    query = "SELECT donationid, offeringid, needid from donationlog WHERE isDelivered = 0"
    cr.execute(query)
    undelivered_items = cr.fetchall()
    undelivered_full_list = []
    for undelivered_offer in undelivered_items:
        offer_full_list = get_offer_full_info(undelivered_offer[1]) # quantityamount, description, user_offering_lat, user_offering_long
        need_full_list =  get_need_full_info(undelivered_offer[2]) # quantityamount, description, user_need_lat,
        # user_need_long
        donation_id = undelivered_offer[0]
        undelivered_full_list.append(donation_id)
        undelivered_full_list.append(offer_full_list)
        undelivered_full_list.append(need_full_list)

    return undelivered_full_list


def set_donation_as_being_delivered(delivery_id):
    query = "UPDATE donationlog set is_being_delivered=1 WHERE donationid = " + delivery_id
    cr.execute(query)
    mydb.commit()
    print("Updated Donation")

def mark_delivery_as_success(delivery_id):
    query = "UPDATE donationlog set isdelivered=1 WHERE donationid = " + delivery_id
    cr.execute(query)
    mydb.commit()
    print("Updated Donation")

def mark_delivery_as_failure(delivery_id):
    query = "UPDATE donationlog set is_being_delivered=0, isdelivered=0, WHERE donationid = " + delivery_id
    cr.execute(query)
    mydb.commit()
    print("Updated Donation")


def find_nearby_volunteers(lat,lon):
    query = "SELECT userID FROM volunteer WHERE State = 1 "
    cr.execute(query)
    available_volunteers = cr.fetchall()
    nearby_available_volunteers = []
    for x in available_volunteers:
         u_query = "SELECT addresslatitude, addresslongitude FROM user WHERE userid =" + str(x[0])
         cr.execute(u_query)
         available_volunteers_coor = cr.fetchall()
         a = (lat,lon)
         b = available_volunteers_coor[0]
         if distance.distance(a,b).km < 7:
            nearby_available_volunteers.append(x[0])
    return nearby_available_volunteers

def get_donorid_from_offer(offerid):
    query = "SELECT userid from offering where offeringid =" + str(offerid)
    cr.execute(query)
    a = cr.fetchall()
    return a[0][0]

def get_victimid_from_need(needid):
    query = "SELECT userid from need where needid =" + str(needid)
    cr.execute(query)
    a = cr.fetchall()
    return a[0][0]

def check_if_type_exists(new_type_name):
    query = "SELECT * FROM donationtype WHERE donationtypename=%s" % new_type_name
    cr.execute(query)
    type_exists =  cr.fetchall().__len__() > 0
    print("Does this type exist? -> " + type_exists)
    return type_exists

