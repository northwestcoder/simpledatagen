
import numpy as np
import random
import datetime 
import helpers

quote = "\""
quotecomma = "\","
newline = "\n"

transColumnData = [
'customer_id',
'orderid',
'purchasedatetime',
'transactiontotal',
'numberofitems',
'productcode',
'productcategory']

trans_start_date = datetime.date.today() - datetime.timedelta(days=1800)
trans_end_date = datetime.date.today() - datetime.timedelta(days=1)
time_between_dates = trans_end_date - trans_start_date
trans_days_between_dates = time_between_dates.days



def generateTransactions(customerid: str, maxtrans: int):


	rowcount = 0
	transactions = ""

	for newrow in range(random.randint(1,maxtrans)):   # for each customer we gen 1-N transactions, change as desired
		newrow = ""
		transtotal = random.triangular(100, 2000) # triangular is awesome and creates a nice normal distro of values
		numitems = random.randint(1,15)

		newrow += quote + customerid + quotecomma
		newrow += quote + helpers.id_generator() + quotecomma

		random_number_of_days = random.randrange(trans_days_between_dates)
		random_date = trans_start_date + datetime.timedelta(days=random_number_of_days)		
		newrow += quote + str(random_date) + quotecomma

		newrow += quote + str(transtotal) + quotecomma
		newrow += quote + str(numitems) + quotecomma		

		prodcode = random.randint(700000000,900000000)
		newrow += quote + str(prodcode) + quotecomma		
		newrow += quote + ("PR" + str(prodcode)[:3]) + quote	

		if rowcount != maxtrans:			
			newrow += newline

		transactions += newrow

		rowcount+=1

	return(transactions)



#print(generateTransactions("test",5))