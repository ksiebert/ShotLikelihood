# Class to represent a shotzone
# stores a map of all different shot types occuring in zone
class ShotZone:

	def __init__(self, zone):
		self.shots = {} # {type: [attempts, makes]}
		self.zone = zone

	# Adds a shot of shot type
	# make indicates whether or not shot was made
	def shot(self, shot_type, make):
		# add potentially new shot type
		if shot_type not in self.shots:
			self.shots[shot_type] = [0,0]

		if make:
			self.shots[shot_type][0] += 1
			self.shots[shot_type][1] += 1
		else:
			self.shots[shot_type][0] += 1
		return

	# gets all shots of shot type in the zone
	# returns array of format [attempts, makes]
	def get_attempts_makes(self, shot_type):
		if not shot_type:
			output = [0,0]
			for shot in self.shots:
				output[0] += self.shots[shot][0]
				output[1] += self.shots[shot][1]
			return output
		return self.shots[shot_type]

	# format shot zone class to string
	def __str__(self):
		outstring = ''
		outstring += 'Zone: ' + str(self.zone) + '\n'
		outstring += "Shots: \n"
		outstring += str(self.shots)
		return outstring
