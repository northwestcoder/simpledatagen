
import numpy as np
import random
import datetime 

import helpers


transColumnData = ['customer_id','orderid','purchasedatetime','transactiontotal','numberofitems','productcode','productcategory']

def createTransactionData(headers: bool, maxtrans: int) -> str:
