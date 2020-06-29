import json

import example01




thedata = example01.createData(False,10,False)


temparray = []
for line in thedata.split("\n"):
		temparray.append(line)

#print(temparray)

test = json.dumps(temparray)

print(test)