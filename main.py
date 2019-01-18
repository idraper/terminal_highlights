import svr_lib as svr
from p_lib import get_match_raw_str
from replay import Replay
import json

import time

total_matches = svr.get_num_matches() + svr.get_num_matches('One')

# print (total_matches)

n = 1
replays = {}
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
	replay = Replay(ID, str_data)
	# print ('Class time: {}'.format(time.clock()-start1))
	# replays[ID] = 

	# print (replays[ID])


print ('Time elapsed: {}'.format(time.clock()-start))
