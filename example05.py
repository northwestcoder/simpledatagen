import time
import buildcsv_people


# let's use a low tech timer to see how long the data gen takes
t_start = time.time()


iterations = 10
batchsize = 10

for i in range(iterations):
	# if batch 1, then use columns headers
	if i == 0:

		args = (True, batchsize, True, 5)
		test = buildcsv_people.createData(*args)
		with open('customers.csv', 'w') as f:
			f.write(test[0])
		with open('customers_transactions.csv', 'w') as f:
			f.write(test[1])

	# no column headers
	else:
		args = (False, batchsize, True, 5)
		test = buildcsv_people.createData(*args)
		with open('customers.csv', 'a') as f:
			f.write(test[0])
		with open('customers_transactions.csv', 'a') as f:
			f.write(test[1])

t_end = time.time()
totaltime = t_end-t_start
print(str(totaltime) + " seconds")