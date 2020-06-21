# simpledatagen - lightweight data generator for various uses


## example01.py

This happy little guy was an experiment in not using pandas, and not even using csv readers and writers. It generates a CSV formatted string, and just returns that string. It's up to the caller to specify how much data, as well as whether or not to use the column headers.

## example02.py

For instance, in example02.py we call into example01 and specify a row count and headers. You can start to imagine interating for all kinds of performance reasons, and not wanting the headers on the 2nd or Nth call.

## example03.py

Using flask (you will need to _pip install flask_ in your python environment), we create two simple endpoints "/staticpayload" and "/randompayload" - which will both autogenerate 1,000 lines of fake data by calling example01. For the static endpoint, the data is generated once per lifetime of the flask run. For the random endpoint, each refresh / page call to the endpoint will regen the data.

## example04.py

If you were looking closely at our original createData() definition, you may have noticed a "buildtransactions" boolean flag. Example04 shows this in action. When you run this example, we output two csv files, one for customers and a second with transactions for them, using the customer ID to seed a random set of transactions (random from 1 to 10 transactions per customer).