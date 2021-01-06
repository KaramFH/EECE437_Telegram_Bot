
class Campaign():

	def __init__(self,name=0,ownerID=0,description=0,latitude=0,longitude=0):
		self.name = name
		self.ownerID = ownerID
		self.description = description
		self.latitude = latitude
		self.longitude = longitude

	def reset(self):
		self.name = 0
		self.ownerID = 0
		self.description = 0
		self. latitude = 0
		self.longitude = 0
