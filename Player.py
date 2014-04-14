from ShotZone import ShotZone

Zones = [[0, 1, 2, 3, 4], [5, 6, 7, 8, 9], [10, 11, 12, 13, 14], [15,15,15,15,15]]

class Player:

	def __init__(self, name):
		self.name = name
		self.shot_zones = []

		for i in range(16):
			zone = ShotZone(i)
			self.shot_zones.append(zone)


	def add_shot(self, x, y, shot_type, make):
		zone = self.get_zone(x,y)
		self.shot_zones[zone].shot(shot_type, make)


	def get_attempts_makes(self, x, y, shot_type):
		zone = self.get_zone(x,y)
		return self.shot_zones[zone].get_attempts_makes(shot_type)

	def get_zone(self, x, y):
		y_index = 0
		if y > 30:
			y_index = 3
		else:
			y_index = y / 10
		x_index = min(4, x / 10)
		
		return Zones[y_index][x_index]

	def __str__(self):
		outstring = "Player: " + self.name + "\n"
		for zone in self.shot_zones:
			outstring += str(zone)

		return outstring


