import string
import random
import numpy as np
import random
from io import BytesIO, StringIO
import csv
import os
import datetime 
from datetime import timedelta



## Do not recommend changing anything below this line?? maybe?

for filename in os.listdir("inputs"):
	#first, if we want current dates, regen this file prior to loading into memory
	if filename.endswith(".csv") or filename.endswith(".txt"): 
		arrayname = os.path.join(filename[:-4])
		globals()["df_"+arrayname] = 0
		with open("inputs/" + filename, "r") as file:
			globals()["df_"+arrayname] = file.read().split('\n')
			file.close()
	else:
		continue


def genEmail(first_name, last_name, employ):

	temptld = random.choice(df_tld)

	# out of 100, what are we going to do for a variety of emails?
	dice = random.randint(1,100)
	if dice >= 75:
		# email gen random word plus first name
		fragment0 = ''.join(random.choice(df_randowords)) + "_"
		fragment1 = first_name.lower() + "@" + ''.join(e for e in employ if e.isalnum()).lower() + '.' + temptld
		return (fragment0 + fragment1)
	elif dice >= 50:
		# FIRST AND LAST NAME
		fragment0 = first_name.lower() + last_name.lower() + "@" + ''.join(e for e in employ if e.isalnum()).lower() + '.' + temptld
		return (fragment0)
	elif dice >= 25:
		#FIRST INITIAL, LAST NAME, AND A INTEGER
		fragment0 = first_name[0].lower() + last_name.lower() + str(random.randint(100,999)-1) + "@" + ''.join(e for e in employ if e.isalnum()).lower() + '.' + temptld
		return (fragment0)
	else:
		# FIRST INITIAL AND LAST NAME
		fragment0 = first_name[0].lower() + last_name.lower() + "@" + ''.join(e for e in employ if e.isalnum()).lower() + '.' + temptld
		return (fragment0)




DataColumns = ['customer_id','name_prefix','name_first','name_last','gender','email',
'account_status','addr_ln_1_txt','city','state','postal_code','birth_dt','employment','job_title','phone']

birthday_start_date = datetime.date.today() - timedelta(days=27300)
birthday_end_date = datetime.date.today() - timedelta(days=5096)
time_between_dates = birthday_end_date - birthday_start_date
birthday_days_between_dates = time_between_dates.days

def randomlySelected(chanceof, range):
	# e.g. if 6 out of 13 chance odds
	if np.random.randint(range) < chanceof:
		return True
	else:
		return False



def id_generator(size=16, chars=string.ascii_lowercase + string.digits):
    uniqueid = ''.join(random.choice(chars) for _ in range(size))
    return uniqueid


def createData(maxrows: int, output: str) -> str:

	io_output = StringIO()


	listOfNewRows = ""

	for idx, item in enumerate(DataColumns):
		listOfNewRows+="\"" + item + "\""
		if idx+1 != len(DataColumns):
			listOfNewRows+=","
	listOfNewRows+="\n"		

	rowcount = 0
	for newrow in range(maxrows):
		#our temp row array for append
		newrow = ""
		newrow+= "\"" + (id_generator()) + "\","
		tempEmployer = random.choice(df_companies)
		# some squirrel to create gender based names
		if randomlySelected(6, 11):  # construct female name slightly more often (54% of the time)
			tempFirstName = random.choice(df_firstnames_female)
			tempLastName = random.choice(df_lastnames)
			newrow+= "\"" + (random.choice(df_prefix_female)) + "\","
			newrow+= "\"" + (tempFirstName) + "\","
			newrow+=( "\"" + tempLastName) + "\","
			newrow+= "\"" + ("F") + ","
		else:
			tempFirstName = random.choice(df_firstnames_male) + str(random.randint(100,999)-1)
			tempLastName = random.choice(df_lastnames) + str(random.randint(100,999)-1)
			newrow+= "\"" + (random.choice(df_prefix_male)) + "\","
			newrow+= "\"" + (tempFirstName) + "\","
			newrow+= "\"" + (tempLastName) + "\","
			newrow+= "\"" + ("M") + ","
		tempEmail = genEmail(tempFirstName, tempLastName, tempEmployer)
		newrow+= "\"" + (tempEmail) + "\","
		newrow+= "\"" + (random.choice(df_account_types)) + "\","
		newrow+= "\"" + (str(random.randint(100,9999)) + " " + random.choice(df_streetnames)) + "\","
		tempCityStateCombo = random.choice(df_us_cities_states_counties).split(',')
		whichStateType = np.random.randint(2)
		newrow+= "\"" + (tempCityStateCombo[0]) + "\","
		newrow+= "\"" + (tempCityStateCombo[whichStateType+1]) + "\","

		newrow+= "\"" + (random.choice(df_postalcodes)) + "\","
		random_number_of_days = random.randrange(birthday_days_between_dates)
		random_date = birthday_start_date + datetime.timedelta(days=random_number_of_days)		
		newrow+= "\"" + str(random_date) + "\","

		newrow+= "\"" + (tempEmployer) + "\","
		newrow+= "\"" + (random.choice(df_jobs)) + "\","
		newrow+= "\"" + (random.choice(df_phones)) + "\""
		if rowcount != maxrows:			
			newrow+=("\n")
		listOfNewRows+=newrow
		rowcount+=1

	writer = csv.writer(io_output, quoting=csv.QUOTE_NONNUMERIC)
	writer.writerow(listOfNewRows)

	if output == "csv":
		return listOfNewRows


test = createData(100000, "csv")

print(test)