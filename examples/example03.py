from flask import Flask

import example01

app = Flask(__name__)

@app.route('/payload')
def hello_world():

	payload = example01.createData(headers=True, rows=1000)
	return payload