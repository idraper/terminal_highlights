import json

# Stores data from a single replay and creates the Algo classes
class Replay:
	def __init__(self, ID, data):
		self.ID = ID;
		self.ref = None
		self.turns = {}
		self.valid_turns = []

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

		for line in str_data.split('\\n'):
			line = line.replace("\\n", "")
			line = line.replace("\\t", "")
			if (line != ''):
				data = json.loads(line)

				try:
					data['debug']
					self.ref = data
				except:
					turn_num = data['turnInfo'][1]
					frame_num = data['turnInfo'][2]
					self.turns[(turn_num, frame_num)] = data
					if (turn_num, frame_num) not in self.valid_turns:
						self.valid_turns.append((turn_num, frame_num))

	def get_cores_on_board(self, filters, encryptors, destructors):
		return len(filters) + len(encryptors) * 4 + len(destructors) * 3

	def unpack_data(self, algos):
		try:
			self.algo1, self.algo2 = self.create_algos(algos)

			for t, f in self.get_valid_turns():
				turn = self.get_turn(t, f)

				turn_info = turn['turnInfo']
				events = turn['events']
				spawn = events['spawn']

				p1_stats = turn['p1Stats']
				p1_units = turn['p1Units']

				p2_stats = turn['p2Stats']
				p2_units = turn['p2Units']

				self.add_data_to_algo(self.algo1, t, f, p1_stats, p1_units, spawn)
				self.add_data_to_algo(self.algo2, t, f, p2_stats, p2_units, spawn)

			self.algo1.recored_final_data(self.ID, self.algo2)
			self.algo2.recored_final_data(self.ID, self.algo1)
			self.algo1.add_end_stats(self.ID, self.turns[self.valid_turns[-1]]['endStats']['player1'])
			self.algo2.add_end_stats(self.ID, self.turns[self.valid_turns[-1]]['endStats']['player2'])
		except Exception as e:
			sys.stderr.write(str(e))

	def get_valid_turns(self):
		return self.valid_turns
	def get_turns(self):
		return self.turns
	def get_turn(self, turn, frame=-1):
		return self.turns[(turn, frame)]
