from user import  User

class Volunteer(User):

	def __init__(self, firstname, lastname ,dateofbirth, address, contactinfo, state ):
		self.state = state

	def set_state(self , newState):
		self.state = newState

	def donate(self, Donation):
		pass