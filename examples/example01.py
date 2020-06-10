import pandas as pd
import string
import sys as sys
import random
import numpy as np
import random
from io import BytesIO, StringIO
from csv import writer 
import time


DataColumns = ['customer_id','name_prefix','name_first','name_last','gender','email',
'account_status','addr_ln_1_txt','city','state','postal_code','birth_dt','employment','job_title','phone','dtUpdateDate']


## Do not recommend changing anything below this line

def PopulatePrimaryCustomers(filename: str) -> pd.DataFrame():

	output = StringIO()
	csv_writer = writer(output)

	columns = DataColumns
	customerStaging = pd.DataFrame(columns=columns)
	customerStaging.astype(str)

	listOfNewRows = []
	for newrow in range(1000):
		#our temp row array for append
		newrow = []
		newrow.append(str(ampwriter.nextCustomerID()) + "-" + r.id_generator())
		tempEmployer = random.choice(r.staticdata.companies())
		# some squirrel to create gender based names
		if r.randomlySelected(6, 11):  # construct female name slightly more often (54% of the time)
			tempFirstName = random.choice(r.staticdata.firstnames_female())
			tempLastName = random.choice(r.staticdata.lastnames())
			newrow.append(random.choice(r.staticdata.prefix_female()))
			newrow.append(tempFirstName)
			newrow.append(tempLastName)
			newrow.append("F")
		else:
			tempFirstName = random.choice(r.staticdata.firstnames_male())
			tempLastName = random.choice(r.staticdata.lastnames())
			newrow.append(random.choice(r.staticdata.prefix_male()))
			newrow.append(tempFirstName)
			newrow.append(tempLastName)
			newrow.append("M")
		tempEmail = r.genEmail(tempFirstName, tempLastName, tempEmployer)
		newrow.append(tempEmail)
		newrow.append(random.choice(r.typeAccountStatus))
		newrow.append(str(random.randint(100,9999)) + " " + random.choice(r.staticdata.streetnames()))
		
		# starting in June 2019, we decided to get real cities and states
		# as the risk of accidentally generating a real human is pretty low... 
		tempCityStateCombo = random.choice(r.staticdata.city_state_combos()).split(',')
		whichStateType = np.random.randint(2)
		newrow.append(tempCityStateCombo[0])
		newrow.append(tempCityStateCombo[whichStateType+1])
		newrow.append(random.choice(r.staticdata.postalcodes()))
		newrow.append(random.choice(r.staticdata.birthdates()))
		newrow.append(tempEmployer)
		newrow.append(random.choice(r.staticdata.jobs()))
		newrow.append(random.choice(r.staticdata.phones()))
		newrow.append(s.dtUpdateDate)
		listOfNewRows.append(newrow)



	return customerStaging