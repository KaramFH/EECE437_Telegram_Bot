# from person import Person
import utilities.db_utilities as db_utilities

class Admin(Person) :

    # not consistent with current database design
    def __init__(self, name , address, contactinfo):
        self.name = name
        self.Address = address
        self.contactinfo = contactinfo
        db_utilities.create_new_admin(name, address)


elhosn = Admin( "abess 4" , "bir hassan" , "79100605")
elhosn.add_user( "sh71" , "bir hassan" , "79100605")
elhosn.add_user( "sh72" , "bir hassan" , "79100605")
elhosn.add_user( "sh73" , "bir hassan" , "79100605")