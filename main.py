import svr_lib as svr
from replay import Replay

from p_lib import get_match_raw_str
from modify_website import modify_url

import json
import time

total_matches = svr.get_num_matches() + svr.get_num_matches('One')

'''
What affects score:
	- number of cores on board
	- number of units spawned in a single turn (max)
	- dramatic drop in score
'''

n = 2000
scores = {}

print ('Checking replays:')
start = time.clock()
for i,ID in enumerate(range(total_matches, total_matches-n, -1)):
	try:
		print ('\t{}.......{}\t\t\t\r'.format(i,ID), end='')
		raw_str = get_match_raw_str(ID, prefix=False)
		str_data = svr.get_page_content(raw_str)
		scores[ID] = Replay(ID, str_data).get_score()
	except json.decoder.JSONDecodeError as e:
		print ('Failed with id: {}...skipping'.format(ID))

print ()
print ('Time elapsed: {}'.format(time.clock()-start))
print ()

# print ('Scores:')
# for k,v in scores.items():
# 	print ('\t{: <7} : {}'.format(str(k),str(v)))

print ()
match_str= svr.get_match_str(max(scores.keys(), key=lambda k: scores[k]))
print ('Match link: {}'.format(match_str))
print ()

modify_url(match_str)
