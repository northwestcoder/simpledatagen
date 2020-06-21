import time

import example01

# let's use a low tech timer to see how long the data gen takes
t_start = time.time()

test = example01.createData(headers=True, rows=1000, buildtransactions=False)

with open('output.csv', 'w') as f:
	f.write(test[0])
	print("finished")

t_end = time.time()
totaltime = t_end-t_start
print(str(totaltime) + " seconds")


print(test)