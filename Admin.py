# from person import Person
import utilities.db_utilities as db_utilities

class Admin(Person) :

    # not consistent with current database design
    def __init__(self, name , address, contactinfo):
        self.name = name
        self.Address = address
        self.contactinfo = contactinfo
        db_utilities.create_new_admin(name, address)


