import mysql.connector
import Utils

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="db437"
)
cr = mydb.cursor()

def get_offer_full_info(offer_id):


    offering_query = "SELECT userid, quantityamount, description FROM offering WHERE offeringid = " + str(offer_id)
    cr.execute(offering_query)
    offer = cr.fetchall()[0]

    user_offering_id = offer[0]
    quantityamount = offer[1]
    description = offer[2]

    user_offering_location_query = "SELECT addresslatitude, addresslongitude FROM user WHERE userid = " + str(user_offering_id)
    cr.execute(user_offering_location_query)
    user_offering_location = cr.fetchall()[0]

    user_offering_lati = user_offering_location[0]
    user_offering_long = user_offering_location[1]
    offer_full_info = [quantityamount, description, user_offering_lati, user_offering_long]
    print(offer_full_info)
    return offer_full_info


def get_need_full_info(need_id):
    need_query = "SELECT userid, quantityamount, description FROM need WHERE needid = " + str(need_id)
    cr.execute(need_query)
    need = cr.fetchall()[0]

    user_need_id = need[0]
    quantityamount = need[1]
    description = need[2]
    
    user_need_location_query = "SELECT addresslatitude, addresslongitude FROM user WHERE userid = " + str(user_need_id)
    cr.execute(user_need_location_query)
    user_need_location = cr.fetchall()[0]

    user_need_lati = user_need_location[0]
    user_need_long = user_need_location[1]
    need_full_info = [quantityamount, description, user_need_lati, user_need_long]
    return need_full_info

def Offer_isMatched( offerid ) -> bool:                 # check if there are any needs matched with this offer

    offering_query = "SELECT needID FROM donationlog WHERE offeringID = " + str(offerid)
    cr.execute(offering_query)
    needs = cr.fetchall()
    if needs.__len__() == 0:
        return False
    return True


def get_MatchedNeeeds( offerid) :                  # get needs matched with this offer

    offering_query = "SELECT needID FROM donationlog WHERE offeringID = " + str(offerid)
    cr.execute(offering_query)
    needs = cr.fetchall()
    text = ""
    print(needs)
    for need in needs :
        needID = need[0]
        need_info = get_need_full_info(needID)
        Need_as_text = "" \
        "  ** MATCHED NEED  : " + "\n" \
        "        Need ID =  " + str(needID) + "\n" \
        "        Quantity Amount: " + str(need_info[0]) + "\n" \
        "        Description: " + need_info[1] + "\n" \
        "        Latitude: " + str(need_info[2] ) + "\n" \
        "        Longitude: " + str(need_info[3]) + "\n" \
        "--------------------------------------------------------"+ "\n\n"
        
        text += Need_as_text

    return text


def text_for_Offer( offerID):        # gets offers UNpickied up with matched needs

    offer_info = get_offer_full_info(offerID)
    Offer_as_text = "" \
        "  *** Offering: " + "\n" \
        "        OFFER ID =  " + str(offerID) + "\n" \
        "        Quantity Amount: " + str(offer_info[0]) + "\n" \
        "        Description: " + str(offer_info[1]) + "\n" \
        "        Latitude: " + str(offer_info[2]) + "\n" \
        "        Longitude: " + str(offer_info[3] )+ "\n" \

    if Offer_isMatched(offerID):
        matchedNeeds = get_MatchedNeeeds(offerID)
        Offer_as_text +=  matchedNeeds

    return Offer_as_text


def text_for_need(needID):        

    offer_info = get_need_full_info(needID)
    Need_as_text = "" \
        "  ***  NEED : " + "\n" \
        "        Need ID =  " + str(needID) + "\n" \
        "        Quantity Amount: " + str(offer_info[0]) + "\n" \
        "        Description: " + str(offer_info[1]) + "\n" \
        "        Latitude: " + str(offer_info[2]) + "\n" \
        "        Longitude: " + str(offer_info[3] ) + "\n" \
        "---------------------------------------------------------------"
    
    # if Offer_isMatched(needID):
    #     matchedNeeds = get_MatchedNeeeds(needID)
    #     Need_as_text +=  matchedNeeds


    return Need_as_text


def get_UnpickedUpOffers() :                      # Get offers unpicked up  and unassigned for vilunteers to see

    query = " SELECT offeringID from offering WHERE isPickedUp = 0 and Assigned = 0"
    cr.execute(query)
    offerIDs = cr.fetchall()
    fulltext = ""
    for offerid in offerIDs :
        id = offerid[0]
        fulltext += text_for_Offer(id)
        fulltext += "-----------------------------------------------"'\n'
    return fulltext


def details_of_user(userid):

    query = "SELECT * from user WHERE userid =" + str(userid)
    cr.execute(query)
    details = cr.fetchall()
    text = "First name: "+details[0][1]+'\n'+"Last name: "+details[0][2]+'\n'+"Phonenumber: "+details[0][4]+'\n'+"Address: "+details[0][7]
    return text


def update_offer_assigned(offerID, userID) :

    query = "UPDATE offering SET Assigned = 1 WHERE offeringID = "+ str(offerID)
    cr.execute(query)
    mydb.commit()

    query2 = "SELECT offer_pickup_id from volunteer WHERE userid =  " + str(userID)
    cr.execute(query2)
    offerIDs = cr.fetchall()[0][0]
    offerIDs = str(offerIDs)+ ","+ str(offerID)    # add offers in the following matter : "id1 , id2 , id3..."
    updated = offerIDs.replace( 'None' +",", "")

    query3 = "UPDATE volunteer SET offer_pickup_id = '{}', state = 3 WHERE userID = " + str(userID)
    cr.execute(query3.format(updated))
    mydb.commit()

def cancel_offer_assigned(offerID,userid) :

    query = "UPDATE offering SET Assigned = 0 WHERE offeringID = " + str(offerID)
    cr.execute(query)
    mydb.commit()

    query2 = "SELECT offer_pickup_id from volunteer WHERE userid =  " + str(userid)
    cr.execute(query2)
    offerIDs = cr.fetchall()[0][0]
    updated = offerIDs.replace( str(offerID) +",", "")

    query3 = "UPDATE volunteer SET offer_pickup_id = '{}' , state =1 WHERE userID = " + str(userid)
    cr.execute(query3.format(updated))
    mydb.commit()



# update_offer_assigned(3, 1448273288 )
# cancel_offer_assigned(3, 1448273288 )
# print( get_UnpickedUpOffers() )

def show_assignedOffers( userid):

    query = "SELECT offer_pickup_id from volunteer WHERE userid =  " + str(userid)
    cr.execute(query)
    IDs = cr.fetchall()
    print(IDs)
    ids = IDs[0][0].split(",")
    print(ids)
    fulltext = ""
    for ID in ids :
        if( ID != 'None') and ( not Utils.is_pickedup(ID )):
            fulltext += text_for_Offer(ID)

    return fulltext
    

def show_assignedNeeds( userid):

    query = "SELECT NeedTodeliver_id from volunteer WHERE userid =  " + str(userid)
    cr.execute(query)
    IDs = cr.fetchall()
    print(IDs)
    ids = IDs[0][0].split(",")
    print(ids)
    fulltext = ""
    for ID in ids :

        if ( ( ID != 'None') and ( not Utils.is_delivered(ID )) ) :
            fulltext += text_for_need(ID)

    return fulltext

def set_offer_pickedup(offerid, volunteerID):

    query = "UPDATE offering SET isPickedUp = 1 WHERE offeringID = " + str(offerid)
    cr.execute(query)
    mydb.commit()

    query2 = "SELECT PickedUp_offersID from volunteer WHERE userid =  " + str(volunteerID)
    cr.execute(query2)
    offerIDs = cr.fetchall()[0][0]
    offerIDs = str(offerIDs)+ ","+ str(offerid)    # add offers in the following matter : "id1 , id2 , id3..."
    updated = offerIDs.replace( 'None' +",", "")

    query3 = "UPDATE volunteer SET PickedUp_offersID = '{}', state = 5 WHERE userID = " + str(volunteerID)
    cr.execute(query3.format(offerIDs))
    mydb.commit()


def get_UndeliveredNeeds():

    offering_query = "SELECT needID FROM need WHERE isActive = 1 and Assigned = 0 "
    cr.execute(offering_query)
    needs = cr.fetchall()
    text = ""
    print(needs)
    for need in needs :
        needID = need[0]
        need_info = get_need_full_info(needID)
        Need_as_text = "" \
        "  ** NEED  : " + "\n" \
        "        Need ID =  " + str(needID) + "\n" \
        "        Quantity Amount: " + str(need_info[0]) + "\n" \
        "        Description: " + need_info[1] + "\n" \
        "--------------------------------------------------------"+ "\n\n"
        
        text += Need_as_text

    return text

def update_need_assigned(needID, userID):
    
    query = "UPDATE need SET Assigned = 1 WHERE needID = " + str(needID)
    cr.execute(query)
    mydb.commit()

    query2 = "SELECT NeedTodeliver_id from volunteer WHERE userid =  " + str(userID)
    cr.execute(query2)
    needIDs = cr.fetchall()[0][0]
    needIDs = str(needIDs) + "," + str(needID)  # add needs in the following matter : "id1 , id2 , id3...", make sure need ID is valid
   
    if (str(needIDs).__contains__('None')):
        needIDs = needIDs.replace('None,', "")
   
    query = "UPDATE volunteer SET NeedTodeliver_id = '{}', state = 4 WHERE userID = " + str(userID)
    cr.execute(query.format(needIDs))
    mydb.commit()




def set_need_delivered(needid, volunteerID):

    query = "UPDATE need SET isActive = 0 WHERE needID = " + str(needid)
    cr.execute(query)
    mydb.commit()

    query2 = "SELECT DeliveredNeeds_id from volunteer WHERE userid =  " + str(volunteerID)
    cr.execute(query2)
    needIDs = cr.fetchall()[0][0]
    needIDs = str(needIDs)+ ","+ str(needid)    # add needss in the following matter : "id1 , id2 , id3..."
    needIDs = needIDs.replace('None,', "")
    
    query3 = "UPDATE volunteer SET DeliveredNeeds_id = '{}' WHERE userID = " + str(volunteerID)
    cr.execute(query3.format(needIDs))
    mydb.commit()


def cancel_delivery_assigned(needID,userid) :

    query = "UPDATE need SET Assigned = 0 WHERE needID = " + str(needID)
    cr.execute(query)
    mydb.commit()

    query2 = "SELECT NeedTodeliver_id from volunteer WHERE userid =  " + str(userid)
    cr.execute(query2)
    offerIDs = cr.fetchall()[0][0]
    updated = offerIDs.replace( str(needID) +",", "")

    query3 = "UPDATE volunteer SET NeedTodeliver_id = '{}' WHERE userID = " + str(userid)
    cr.execute(query3.format(updated))
    mydb.commit()



def DeliveredNeeds_receivers() :        # return list of tuples = [ (chatID , 'Need description), (ChatID , 'Need description')]

    dict = []
    query = "SELECT userID, description from need WHERE IsActive = 1 and confirmed =0  "         # get needs set as delivered, and get userIDs to confirm that they received
    cr.execute(query)
    ids_description = cr.fetchall()
    for info in ids_description :
        chatid = get_chatID(info[0])[0][0]
        dict.append( (int(chatid), info[1]) )
    return dict


def update_confirmation(userID , needID, value) :      # if needy person confirmed receival : set value = 1 , if No set = 2

    query = " UPDATE need SET confirmed = {} where userid = %s and needid = %s" % (userID,needID)
    cr.execute(query.format(int(value)))
    mydb.commit()


def requested_needs(user_id): #returns the needs the user requested return list of tuples = [ (needID , 'Need description), (needID , 'Need description')]
    list = []
    query = "SELECT needid, description from need WHERE confirmed = 0 and userid = " + str(user_id)
    cr.execute(query)
    ids_description = cr.fetchall()
    for info in ids_description :
        list.append( (int(info[0]), info[1]) )
    return list

#print(show_assignedNeeds(1470290214))