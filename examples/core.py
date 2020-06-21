import random
import datetime 
import string
import os

# does two things: 1. creates an identity bundle, 2. creates a geolocation bundle

CoreDataColumns = [
'customer_id',
'gender',
'name_prefix',
'name_first',
'name_last',
'email',
'employment',
'address',
'city',
'county',
'state',
'postal_code',
'birth_dt'
]


handlers = {
"customer_id" : "coreNextCustomerID",
"identity_bundle" : "coreIdentityBundle",
"geolocation_bundle" : "coreGeolocationBundle",
"birth_dt" : "fuzzyBirthDateHandler"
		}


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

def randomlySelected(chanceof, range):
	# e.g. if 6 out of 13 chance odds
	if random.randrange(range) < chanceof:
		return True
	else:
		return False

#static and relative dates for the duration of the program operation
birthday_start_date = datetime.date.today() - datetime.timedelta(days=27300)
birthday_end_date = datetime.date.today() - datetime.timedelta(days=5096)
time_between_dates = birthday_end_date - birthday_start_date
birthday_days_between_dates = time_between_dates.days

# generates a 16 char random key
def coreNextCustomerID(size=16, chars=string.ascii_lowercase + string.digits):
	uniqueid = ''.join(random.choice(chars) for _ in range(size))
	return uniqueid



#  generates an identity bundle, defined as: "Gender, Prefix, First Name, Last Name, Email, Employer"
def coreIdentityBundle():

	gender, prefix, firstname, lastname, email, employer = [""]*6
	identity = []
	
	gender = "F" if randomlySelected(6, 11) else "M"
	identity.append(gender)

	prefix = random.choice(df_prefix_female) if gender == "F" else random.choice(df_prefix_male)
	identity.append(prefix)

	firstname = random.choice(df_firstnames_female) if gender == "F" else random.choice(df_firstnames_male)
	identity.append(firstname)

	lastname = random.choice(df_lastnames)
	identity.append(lastname)
	
	employ = random.choice(df_companies)
	temptld = random.choice(df_tld)

	# out of 100, what are we going to do for a variety of emails?
	dice = random.randint(1,100)
	if dice >= 75:
		# email gen random word plus first name
		email = ''.join(random.choice(df_randowords)) + "_" + firstname.lower() + "@" + ''.join(e for e in employ if e.isalnum()).lower() + '.' + temptld
	elif dice >= 50:
		# FIRST AND LAST NAME
		email = firstname.lower() + lastname.lower() + "@" + ''.join(e for e in employ if e.isalnum()).lower() + '.' + temptld
	elif dice >= 25:
		#FIRST INITIAL, LAST NAME, AND A INTEGER
		email = firstname[0].lower() + lastname.lower() + str(random.randint(100,999)-1) + "@" + ''.join(e for e in employ if e.isalnum()).lower() + '.' + temptld
	else:
		# FIRST INITIAL AND LAST NAME
		email = firstname[0].lower() + lastname.lower() + "@" + ''.join(e for e in employ if e.isalnum()).lower() + '.' + temptld

	identity.append(email)
	identity.append(employ)
	
	return identity

#  generates an geolocation bundle, defined as: "address, city, state, postalcode"
def coreGeolocationBundle():
	geolocation = []
	geolocation.append( str(random.randint(100,9999)) + " " + random.choice(df_streetnames))
	citystatecombo = random.choice(df_city_county_state).split(',')
	geolocation.append(citystatecombo[0])
	geolocation.append(citystatecombo[1])
	geolocation.append(citystatecombo[2])
	geolocation.append(random.choice(df_postalcodes))
	return geolocation


def fuzzyBirthDateHandler():
	random_number_of_days = random.randrange(birthday_days_between_dates)
	random_date = birthday_start_date + datetime.timedelta(days=random_number_of_days)		
	return random_date


def handlerMap(type):
	return globals()[handlers.get(type)]()



#test = handlerMap("customer_id")
#print(test)

#test2 = handlerMap("identity_bundle")
#print(test2)


#test3 = handlerMap("geolocation_bundle")
#print(test3)

#test = randomlySelected(6, 13)
#print(test)

