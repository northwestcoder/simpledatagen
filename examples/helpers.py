import string
import random
import numpy as np
import random
import os

import core


extrahandlers = {
"account_type" : "AccountHandler",
"phone_number" : "PhoneHandler",
"job_type" : "JobTypeHandler"
		}




def AccountHandler():
	return random.choice(core.df_account_types)

def PhoneHandler():
	return random.choice(core.df_phones)

def JobTypeHandler():
	return random.choice(core.df_jobs)



def extraHandlerMap(type):
	return globals()[extrahandlers.get(type)]()

