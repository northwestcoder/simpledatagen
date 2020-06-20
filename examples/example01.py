import numpy as np
import random
import datetime 

import helpers


DataColumns = ['customer_id','name_prefix','name_first','name_last','gender','email',
'account_status','addr_ln_1_txt','city','state','postal_code','birth_dt','employment','job_title','phone']

## Do not recommend changing anything below this line?? maybe?

quote = "\""
quotecomma = "\","

birthday_start_date = datetime.date.today() - datetime.timedelta(days=27300)
birthday_end_date = datetime.date.today() - datetime.timedelta(days=5096)
time_between_dates = birthday_end_date - birthday_start_date
birthday_days_between_dates = time_between_dates.days


def createData(headers: bool, rows: int, transactions: bool) -> str:

	listOfNewRows = ""

	if headers:
		for idx, item in enumerate(DataColumns):
			listOfNewRows+=quote + item + quote
			if idx+1 != len(DataColumns):
				listOfNewRows+=","
		listOfNewRows+="\n"		

	rowcount = 0
	for newrow in range(rows):
		
		#our temp row array for append
		newrow = ""
		newrow+= quote + (helpers.id_generator()) + quotecomma
		
		tempEmployer = random.choice(helpers.df_companies)
		# some squirrel to create gender based names
		
		if helpers.randomlySelected(6, 11):  # construct female name slightly more often (54% of the time)
			tempFirstName = random.choice(helpers.df_firstnames_female)
			tempLastName = random.choice(helpers.df_lastnames)
			newrow+= quote + (random.choice(helpers.df_prefix_female)) + quotecomma
			newrow+= quote + (tempFirstName) + quotecomma
			newrow+=( quote + tempLastName) + quotecomma
			newrow+= quote + ("F") + ","
		else:
			tempFirstName = random.choice(helpers.df_firstnames_male) + str(random.randint(100,999)-1)
			tempLastName = random.choice(helpers.df_lastnames) + str(random.randint(100,999)-1)
			newrow+= quote + (random.choice(helpers.df_prefix_male)) + quotecomma
			newrow+= quote + (tempFirstName) + quotecomma
			newrow+= quote + (tempLastName) + quotecomma
			newrow+= quote + ("M") + ","
		
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
			newrow+=("\n")
		listOfNewRows+=newrow
		
		rowcount+=1

	return listOfNewRows


#test = createData(true, 1000, false)
#print(test)