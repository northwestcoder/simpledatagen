import numpy as np
import random
import datetime 

import helpers
import transactions

DataColumns = [
'customer_id',
'name_prefix',
'name_first',
'name_last',
'gender',
'email',
'account_status',
'addr_ln_1_txt',
'city',
'state',
'postal_code',
'birth_dt',
'employment',
'job_title',
'phone']

## Do not recommend changing anything below this line?? maybe?

quote = "\""
quotecomma = "\","
newline = "\n"

birthday_start_date = datetime.date.today() - datetime.timedelta(days=27300)
birthday_end_date = datetime.date.today() - datetime.timedelta(days=5096)
time_between_dates = birthday_end_date - birthday_start_date
birthday_days_between_dates = time_between_dates.days


def createData(headers: bool, rows: int, buildtransactions: bool, *args) -> str:



	listOfNewRows = ""
	listOfNewTransactions = ""

	if headers:
		for idx, item in enumerate(DataColumns):
			listOfNewRows+=quote + item + quote
			if idx+1 != len(DataColumns):
				listOfNewRows+=","
		listOfNewRows+="\n"


	if buildtransactions:
		for idx, item in enumerate(transactions.transColumnData):
			listOfNewTransactions += quote + item + quote
			if idx+1 != len(transactions.transColumnData):
				listOfNewTransactions += ","
		listOfNewTransactions += "\n"		

	rowcount = 0
	for newrow in range(rows):
		
		#our temp row array for append
		newid = helpers.id_generator()
		newrow = ""
		newrow+= quote + newid + quotecomma
		
		tempEmployer = random.choice(helpers.df_companies)
		# some squirrel to create gender based names
		
		if helpers.randomlySelected(6, 11):  # construct female name slightly more often (54% of the time)
			tempFirstName = random.choice(helpers.df_firstnames_female)
			tempLastName = random.choice(helpers.df_lastnames)
			newrow+= quote + (random.choice(helpers.df_prefix_female)) + quotecomma
			newrow+= quote + (tempFirstName) + quotecomma
			newrow+=( quote + tempLastName) + quotecomma
			newrow+= quote + ("F") + "," + quotecomma
		else:
			tempFirstName = random.choice(helpers.df_firstnames_male) + str(random.randint(100,999)-1)
			tempLastName = random.choice(helpers.df_lastnames) + str(random.randint(100,999)-1)
			newrow+= quote + (random.choice(helpers.df_prefix_male)) + quotecomma
			newrow+= quote + (tempFirstName) + quotecomma
			newrow+= quote + (tempLastName) + quotecomma
			newrow+= quote + ("M") + "," + quotecomma
		
		tempEmail = helpers.genEmail(tempFirstName, tempLastName, tempEmployer)
		
		newrow+= quote + (tempEmail) + quotecomma
		newrow+= quote + (random.choice(helpers.df_account_types)) + quotecomma
		newrow+= quote + (str(random.randint(100,9999)) + " " + random.choice(helpers.df_streetnames)) + quotecomma

		tempCityStateCombo = random.choice(helpers.df_us_cities_states_counties).split(',')
		whichStateType = np.random.randint(2)
		
		newrow+= quote + (tempCityStateCombo[0]) + quotecomma
		newrow+= quote + (tempCityStateCombo[whichStateType+1]) + quotecomma

		newrow+= quote + (random.choice(helpers.df_postalcodes)) + quotecomma
		random_number_of_days = random.randrange(birthday_days_between_dates)
		random_date = birthday_start_date + datetime.timedelta(days=random_number_of_days)		
		newrow+= quote + str(random_date) + quotecomma

		newrow+= quote + (tempEmployer) + quotecomma
		newrow+= quote + (random.choice(helpers.df_jobs)) + quotecomma
		newrow+= quote + (random.choice(helpers.df_phones)) + quote
		
		if rowcount != rows:			
			newrow+= newline
		
		listOfNewRows+= newrow

		# if transactions were requested, we do that here
		if buildtransactions:
			maxrows = int(args[0])
			listOfNewTransactions += transactions.generateTransactions(newid, maxrows)



		rowcount+=1

	return listOfNewRows, listOfNewTransactions




#test = createData(True, 10, True, 422)

# some customers
#print(test[1])

# and their transactions
#print(test[1])
