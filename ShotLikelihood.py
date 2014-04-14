from Player import Player
import os

# CSV file format notes
# column 13 is player action
# column 23 is player involved in action
# column 27 is missed or made
# column 29 is type
# column 30,31 are x,y

class ShotLikelihood:

	def __init__(self):
		self.years = {}
		directory = "../2006-2007.regular_season/"
		directory_size = len(os.listdir(directory))
		count = 0
		players = {}
		for file_name in os.listdir(directory):
			with open(directory+file_name) as f:
				content = f.readlines()
				for line in content:
					cells = line.split(',')

					# read cell information
					action = cells[13]
					if action != "shot":
						continue

					player = cells[23]
					x = cells[30]
					y = cells[31]
					if x and y:
						x = int(x)
						y = int(y)
					else:
						continue
					
					make = False
					if cells[27] == "made":
						make = True

					shot_type = cells[29]

					# add player if player not in player table
					if player not in players:
						players[player] = Player(player)

					players[player].add_shot(x,y,shot_type, make)
					

			# Show status in iterating through game files
			count += 1
			print str(count) + " Files out of " + str(directory_size) + "Finished"

		self.years[2006] = players

		directory = "../2007-2008.regular_season/"
		directory_size = len(os.listdir(directory))
		count = 0
		players = {}
		for file_name in os.listdir(directory):
			with open(directory+file_name) as f:
				content = f.readlines()
				for line in content:
					cells = line.split(',')

					# read cell information
					action = cells[13]
					if action != "shot":
						continue

					player = cells[23]
					x = cells[30]
					y = cells[31]
					if x and y:
						x = int(x)
						y = int(y)
					else:
						continue
					
					make = False
					if cells[27] == "made":
						make = True

					shot_type = cells[29]

					# add player if player not in player table
					if player not in players:
						players[player] = Player(player)

					players[player].add_shot(x,y,shot_type, make)
					

			# Show status in iterating through game files
			count += 1
			print str(count) + " Files out of " + str(directory_size) + "Finished"

		self.years[2007] = players

		directory = "../2008-2009.regular_season/"
		directory_size = len(os.listdir(directory))
		count = 0
		players = {}
		for file_name in os.listdir(directory):
			with open(directory+file_name) as f:
				content = f.readlines()
				for line in content:
					cells = line.split(',')

					# read cell information
					action = cells[13]
					if action != "shot":
						continue

					player = cells[23]
					x = cells[30]
					y = cells[31]
					if x and y:
						x = int(x)
						y = int(y)
					else:
						continue
					
					make = False
					if cells[27] == "made":
						make = True

					shot_type = cells[29]

					# add player if player not in player table
					if player not in players:
						players[player] = Player(player)

					players[player].add_shot(x,y,shot_type, make)
					

			# Show status in iterating through game files
			count += 1
			print str(count) + " Files out of " + str(directory_size) + "Finished"

		self.years[2008] = players



	def get_likelihood(self, x, y, year_range=[2006], shot_type=None, player=None):
		attempts_makes = [0,0]
		if not player:
			for year in year_range:
				players = self.years[year]
				for player in players:
					temp = players[player].get_attempts_makes(x,y,shot_type)
					attempts_makes[0] += temp[0]
					attempts_makes[1] += temp[1]

			print attempts_makes[1], attempts_makes[0]
			return float(attempts_makes[1]) / attempts_makes[0]

		for year in year_range:
			temp = self.years[year][player].get_attempts_makes(x,y,shot_type)
			attempts_makes[0] += temp[0]
			attempts_makes[1] += temp[1]

		print attempts_makes[1], attempts_makes[0]
		return float(attempts_makes[1]) / attempts_makes[0]

	def show_player(self, year, player):
		return "Year: " + str(year) + "\n" + str(self.years[year][player])

shot = ShotLikelihood()
# print shot.get_likelihood(25,25,player='Dwyane Wade')
# print shot.get_likelihood(25,25)
# print shot.get_likelihood(25,5,player='Dwyane Wade')
# print shot.get_likelihood(25,5)
print shot.show_player(2006, 'Dwyane Wade')
print shot.show_player(2007, 'Dwyane Wade')
print shot.show_player(2008, 'Dwyane Wade')



