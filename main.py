import svr_lib as svr
from p_lib import get_match_raw_str
import json

total_matches = svr.get_num_matches() + svr.get_num_matches('One')

print (total_matches)

r = 100

for ID in range(total_matches, total_matches-r, -1):
	print (get_match_raw_str(ID))
