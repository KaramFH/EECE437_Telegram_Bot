from enum import Enum
import db_utilities

class Admin(Person):
    # not consistent with current database design
    def __init__(self, name , address, contactinfo):
        self.name = name
        self.Address = address
        self.contactinfo = contactinfo
        db_utilities.create_new_admin(name, address)

class User:
	def __init__(self, UserID=0, FirstName=0, LastName=0,Birthdate=0, PhoneNumber=0, AddressLatitude=0, AddressLongitude=0, AddressDescription=0, CreationDate=0, ChatID=0):
		self.UserID = UserID
		self.FirstName = FirstName
		self.LastName = LastName
		self.Birthdate = Birthdate
		self.PhoneNumber = PhoneNumber
		self.AddressLatitude = AddressLatitude
		self.AddressLongitude = AddressLongitude
		self.AddressDescription = AddressDescription
		self.CreationDate = CreationDate
		self.ChatID = ChatID

	def update_AddressDescription(self, newAddress):
		self.AddressDescription = newAddress

	def update_AddressLatitude(self,lat):
		self.AddressLatitude = lat

	def update_AddressLongitude(self,lon):
		self.AddressLongitude = lon

	def reset(self):
		self.UserID = 0
		self.FirstName = 0
		self.LastName = 0
		self.Birthdate = 0
		self.PhoneNumber = 0
		self.AddressLatitude = 0
		self.AddressLongitude = 0
		self.AddressDescription = 0
		self.CreationDate = 0
		self.ChatID = 0

class Volunteer(User):
	def __init__(self, firstname, lastname ,dateofbirth, address, contactinfo, state):
		self.state = state

	def set_state(self , newState):
		self.state = newState

	def donate(self, Donation):
		pass

class VolunteerState(Enum):
    FREE = 1                    # volunteer is not assigned any task
    PENDING_ACK = 2 
    PENDING_PICKUP = 3            # volunteer has been assignedd a task
    PENDING_DELV = 4            # pending confirmation that deliviry has been made
    RESTING = 5                # volunteer has been assigned too many tasks and needs to rest

class Offer :
    def __init__(self):
        self.type = None
        self.userID = None
        self.description = None
        self.QuantityAmount = None
        self.QuantityRemaining = None
        self.isActive = 1