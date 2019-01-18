import svr_lib as svr
from p_lib import get_match_raw_str
from replay import Replay
import json

import time

total_matches = svr.get_num_matches() + svr.get_num_matches('One')

# print (total_matches)

'''
What affects score:
	- number of cores on board
	- number of units spawned in a single turn (max)
	- dramatic drop in score
'''

n = 10
scores = {}

# 10 matches ~= 1 sec
start = time.clock()
for ID in range(total_matches, total_matches-n, -1):
	raw_str = get_match_raw_str(ID, prefix=False)
	# print (raw_str)

	# start1 = time.clock()
	str_data = svr.get_page_content(raw_str)
	# print ('Web time: {}'.format(time.clock()-start1))


	# start1 = time.clock()
	# replay = Replay(ID, str_data)
	scores[ID] = Replay(ID, str_data).get_score()
	# print ('Class time: {}'.format(time.clock()-start1))

	# print (replays[ID])

print ()
print ('Time elapsed: {}'.format(time.clock()-start))
print ()

print ('Scores:')
for k,v in scores.items():
	print ('\t{: <7} : {}'.format(str(k),str(v)))

print ()
print (svr.get_match_str(max(scores.keys(), key=lambda k: scores[k])))
