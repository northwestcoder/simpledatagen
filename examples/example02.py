import time

import example01

# let's use a low tech timer to see how long the data gen takes
t_start = time.time()

test = example01.createData(headers=True, rows=50000, transactions=False)

with open('output.csv', 'w') as f:
	f.write(test)
	print("finished")

t_end = time.time()
totaltime = t_end-t_start
print(str(totaltime) + " seconds")