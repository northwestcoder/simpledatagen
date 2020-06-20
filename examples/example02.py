import time

import example01

t0 = time.time()

test = example01.createData(headers=True, rows=50000)

with open('output.csv', 'w') as f:
	f.write(test)
	print("finished")

t1 = time.time()

totaltime = t1-t0
print(str(totaltime) + " seconds")