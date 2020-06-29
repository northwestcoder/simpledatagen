import time
import buildcsv_people


# let's use a low tech timer to see how long the data gen takes
t_start = time.time()

args = (True, 1000, False, 0)
test = buildcsv_people.createData(*args)

# just to remind, createDate returns two elements in an array,
# one for customers and one for their transactions

with open('customers.csv', 'w') as f:
	f.write(test[0])
	print("finished writing customers")

with open('customers_transactions.csv', 'w') as f:
	f.write(test[1])
	print("finished writing customer transactions")


t_end = time.time()
totaltime = t_end-t_start
print(str(totaltime) + " seconds")