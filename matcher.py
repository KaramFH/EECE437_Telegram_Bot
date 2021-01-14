import Utils as utils
from datetime import datetime
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="db437"
)
cr = mydb.cursor()


def run_matcher():
    
    types =[1,2,3,4,5,6]    # should have a fct. to get all type ids actively
    for  typeID in types  :

        for need in utils.fetch_all_needs_of_type(typeID):

            print("got themmmmmmm") 

            needID = need[0]
            qtneeded = need[4]

            offers_sameType = utils.get_offers_of_type(typeID)

            if offers_sameType.__len__() >= 1:
                qtOfferedIndex = 3
                offerID = offers_sameType[0][0]
                qtoffered = offers_sameType[0][qtOfferedIndex]

                if ( qtneeded <=  qtoffered ) :                                      # found offer with greater quantity
                    utils.set_matched( offerID, needID)                              # we found a medical match
                    print("MATCH FOUND for type %d !!" % typeID)
                    qtremaining = qtoffered - qtneeded
                    update_qtoffered(offerID,needID,qtremaining)

                else :                                                               # found offer with lesser quantity
                    utils.set_matched(offerID, needID)                               # we found a medical match
                    print("MATCH FOUND for type %d  , needID = %d , offerID = %d!!" % (typeID, needID,offerID ) )
                    qtremaining = qtneeded - qtoffered
                    update_qtneeded(offerID, needID, qtremaining)




            else:                                            #No match with this type found, match with monetary offers
                cashValueIndex = 3
                cashValue_perUnit = need[cashValueIndex]
                cash_needed = cashValue_perUnit * need[4]         # unit value* qt needed = total amount needed

                monetary_offers = utils.get_all_monetary_offers()
                print("cash in need : ", cash_needed)

                for cash_offer in monetary_offers:
                    cash_offer_id = cash_offer[0]
                    cash_offered = cash_offer[3]

                    if cash_needed >= cash_offered:
                        # set as matched and set offer to inactive
                        utils.set_matched(needID, cash_offer_id)
                        cash_needed = cash_needed - cash_offered
                        query = "UPDATE offering SET isActive = 0, QuantityRemaining = 0 WHERE offerID = " + \
                                str(cash_offer_id)
                        cr.execute(query)
                        mydb.commit()

                        if (cash_needed == 0):
                            break
                    elif cash_needed < cash_offered:
                        utils.set_matched(needID, cash_offer_id)
                        query = "UPDATE offering SET  QuantityRemaining = {} WHERE offeringID = " + \
                                str(cash_offer_id)
                        cr.execute(query.format(cash_offered - cash_needed))
                        mydb.commit()
                        cash_needed = 0
                        fquery = " UPDATE need SET isActive = 0, QuantityRemaining = {} WHERE needID = " + str(needID)
                        cr.execute(fquery.format(cash_needed))
                        mydb.commit()
                        break





def update_qtoffered ( offerid, needid , qtremaining) :

    query = "UPDATE offering SET  QuantityRemaining = {} WHERE offeringID = " + str(offerid)
    cr.execute( query.format(qtremaining))
    mydb.commit()
    Nquery = " UPDATE need SET Matched = 1, QuantityRemaining = 0 WHERE needID = " + str(needid)
    cr.execute( Nquery)
    mydb.commit()

def update_qtneeded ( offerid, needid , qtremaining) :

    query = "UPDATE need SET  QuantityRemaining = {} WHERE needID = " + str(needid)
    cr.execute( query.format(qtremaining))
    mydb.commit()
    Nquery = " UPDATE offering SET isActive = 0, QuantityRemaining = 0 WHERE offeringID = " + str(offerid)
    cr.execute( Nquery)
    mydb.commit()

