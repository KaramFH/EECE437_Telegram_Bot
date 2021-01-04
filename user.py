from volunteerstate import VolunteerState as states

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

# User.add_offer('medical',9,' i will be giving coronavirus vaccines for free',20)
# User.add_User(21,'hassan','sha7sh7','07/17/99','7892868722',123)
# g = User.is_registered(10, 'abbas')
# print(g)