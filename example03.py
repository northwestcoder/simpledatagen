#
# for this example, you will need to pip install flask
# and/or read the docs on flask: https://flask.palletsprojects.com/en/1.1.x/
#
# this example builds on the previous example01 by providing 
# a payload URL for fake data
#
# from this directory, you would start flask from the command line like so:
#   $export FLASK_APP=example03.py
#   $flask run
#
# it will then say
# "Running on http://127.0.0.1:5000/"
# 
# and if you go to http://127.0.0.1:5000/randompayload
# you should see 1,000 lines of randomly generated data
#
# each time you refresh the page the data will be rebuilt :) 


from flask import Flask

import buildcsv_people

app = Flask(__name__)

staticdata = buildcsv_people.createData(headers=True, rows=1000, buildtransactions=False)

# this next route generates a var each time the route is called
@app.route('/randompayload')
def randompayload():

	payload = buildcsv_people.createData(headers=True, rows=1000, buildtransactions=False)
	return payload


# this one uses 'staticdata' created outside of the route, 
# so it will remain stable for the lifetime of the flask invocation
@app.route('/staticpayload')
def staticpayload():

	return staticdata