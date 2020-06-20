import string
import random
import numpy as np
import random
import os

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

def id_generator(size=16, chars=string.ascii_lowercase + string.digits):
    uniqueid = ''.join(random.choice(chars) for _ in range(size))
    return uniqueid

# gender selected, females slightly more often than males
def randomlySelected(chanceof, range):
	# e.g. if 6 out of 13 chance odds
	if np.random.randint(range) < chanceof:
		return True
	else:
		return False


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