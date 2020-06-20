# simpledatagen - lightweight data generator for various uses


## example01.py

This happy little guy was an experiment in not using pandas, and not even using csv readers and writers. It generates a CSV formatted string, and just returns that string. It's up to the caller to specify how much data, as well as whether or not to use the column headers.

## example02.py

For instance, in example02.py we call into example01 and specify a row count and headers. You can start to imagine interating for all kinds of performance reasons, and not wanting the headers on the 2nd or Nth call.