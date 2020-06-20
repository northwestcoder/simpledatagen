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

import example01

app = Flask(__name__)


staticdata = example01.createData(headers=True, rows=1000, transactions=False)

@app.route('/randompayload')
def randompayload():

	payload = example01.createData(headers=True, rows=1000, transactions=False)
	return payload


# this one uses a var created outside of the route, so it will remain stable for the lifetime of the flask invocation
@app.route('/staticpayload')
def staticpayload():

	return staticdata