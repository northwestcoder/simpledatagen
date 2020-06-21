
import numpy as np
import random
import datetime 

import helpers
import example01
import transactions

import time

# let's use a low tech timer to see how long the data gen takes
t_start = time.time()

args = (True, 300, True, 2000)
test = example01.createData(*args)

with open('customers.csv', 'w') as f:
	f.write(test[0])
	print("finished writing customers")

with open('customers_transactions.csv', 'w') as f:
	f.write(test[1])
	print("finished writing customer transactions")


t_end = time.time()
totaltime = t_end-t_start
print(str(totaltime) + " seconds")