import json

# Stores data from a single replay and creates the Algo classes
class Replay:
	def __init__(self, ID, data):
		self.ID = ID;
		self.turns = {}
		self.valid_turns = []
		self.score = 0

		self.load_data(data)				# handles loading all the data from file into python variables
		# self.unpack_data(algos)		# stores relevant data after it has been loaded

	def __eq__(self, other):
		return self.ID == other.ID
	def __string(self):
		return self.ID
	def __str__(self):
		return self.__string()
	def __repr__(self):
		return self.__string()

	def load_data(self, str_data):
		# print (str_data)

		p1 = {
				'maxFilters' : 0,
				'maxEncryptors' : 0,
				'maxDestructors' : 0,
				'maxPings' : 0,
				'maxScramblers' : 0,
				'maxEmps' : 0,
				'maxRemoves' : 0
		}
		p2 = {
				'maxFilters' : 0,
				'maxEncryptors' : 0,
				'maxDestructors' : 0,
				'maxPings' : 0,
				'maxScramblers' : 0,
				'maxEmps' : 0,
				'maxRemoves' : 0
		}

		i = 0
		for line in str_data.split('\\n'):
			line = line.replace('\\n', '')
			line = line.replace('\\t', '')
			if (line != ''):
				data = json.loads(line)

				try:
					self.checkUnitMaxes(p1, data, 'p1Units')
					self.checkUnitMaxes(p2, data, 'p2Units')

				except KeyError as e:
					# print (e)
					pass

				# if i == 3:
				# 	print ('breaking')
				# 	break

				i += 1

		for k,v in zip(p1.items(),p2.items()):
			print ('{: <30}{}'.format(str(k),str(v)))

	def checkUnitMaxes(self, player, data, key):
		self.replaceIfMax(player, 'maxFilters', len(data[key][0]))
		self.replaceIfMax(player, 'maxEncryptors', len(data[key][1]))
		self.replaceIfMax(player, 'maxDestructors', len(data[key][2]))
		self.replaceIfMax(player, 'maxPings', len(data[key][3]))
		self.replaceIfMax(player, 'maxScramblers', len(data[key][4]))
		self.replaceIfMax(player, 'maxEmps', len(data[key][5]))
		self.replaceIfMax(player, 'maxRemoves', len(data[key][6]))

	def replaceIfMax(self, player, key, val):
		if player[key] < val: player[key] = val

	def get_cores_on_board(self, filters, encryptors, destructors):
		return len(filters) + len(encryptors) * 4 + len(destructors) * 3

	def get_valid_turns(self):
		return self.valid_turns
	def get_turns(self):
		return self.turns
	def get_turn(self, turn, frame=-1):
		return self.turns[(turn, frame)]

	def get_score(self):
		return self.score
