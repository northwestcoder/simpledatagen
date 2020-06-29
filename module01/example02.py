import time
import os

import buildcsv_people


# let's use a low tech timer to see how long the data gen takes
t_start = time.time()

test = buildcsv_people.createData(headers=True, rows=1000, buildtransactions=False)

with open('output.csv', 'w') as f:
	f.write(test[0])
	print("finished")

t_end = time.time()
totaltime = t_end-t_start
print(str(totaltime) + " seconds")