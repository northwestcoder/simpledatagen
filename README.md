# simpledatagen - lightweight data generator for various uses

Inputs for random data are in the 'inputs' dir. Some examples/exampleNN.py files have commented tests at the bottom, e.g. uncomment and run "python example04.py"

## [buildcsv_people.py](https://github.com/northwestcoder/simpledatagen/blob/master/buildcsv_people.py)

This happy little guy was an experiment in not using pandas, and not even using csv readers and writers. It generates a CSV formatted string, and just returns that string. It's up to the caller to specify how much data, as well as whether or not to use the column headers.

If you dig in, you'll see that we have two types of data: "core" data and "extra" data. The core info is related to Identity and Geolocation. The "Extra" data is defined in helpers.py - in this buildcsv_people example we then merge this into a single CSV string output as an array with two elements: the people element and the transactions element. 

## [example02.py](https://github.com/northwestcoder/simpledatagen/blob/master/example02.py)

For instance, in example02.py we call into example01 and specify a row count and headers. You can start to imagine iterating for all kinds of performance reasons, and not wanting the headers on the 2nd or Nth call.

## [example03.py](https://github.com/northwestcoder/simpledatagen/blob/master/example03.py)

Using flask (you will need to _pip install flask_ in your python environment), we create two simple endpoints "/staticpayload" and "/randompayload" - which will both autogenerate 1,000 lines of fake data by calling example01. For the static endpoint, the data is generated once per lifetime of the flask run. For the random endpoint, each refresh / page call to the endpoint will regen the data.

## [example04.py](https://github.com/northwestcoder/simpledatagen/blob/master/example04.py)

If you were looking closely at our original createData() definition, you may have noticed a "buildtransactions" boolean flag. Example04 shows this in action. When you run this example, we output two csv files, one for customers and a second with transactions for them, using the customer ID to seed a random set of transactions (random from 1 to 10 transactions per customer). The transactions.py is somewhat hardwired and meant as an example of how you can call out to a second data generator using the "parent ID" (called customer_id here).

## [example05.py](https://github.com/northwestcoder/simpledatagen/blob/master/example05.py)

If we want to build really large data files, it might not be a good idea to attempt to load them into memory first like we are doing, and then try to write all at once. This example creates an iteration and batch size for the customers/transactions. The first loop we will write the column headers, but not the 2nd or Nth. *Because we've tried to use native pythonic strings and arrays throughout, we can write 2 million rows of data in about a minute on our late-model mac!*