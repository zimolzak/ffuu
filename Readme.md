FFFFFFFUUUUUUUUUUUU-
========

What is more common: FFFFUUUU, or FFUUUUU, or FFFFFUUU, etc.?

The original comic uses the text
"FFFFFFFFFFFFFFFFFFFFFFFUUUUUUUUUUUUUUUUUUUUUU-", which is to say,
f23u22. Somehow f7u12 got promulgated too. Others are pretty easy to
type. So construct a matrix where the (i,j) element is the search
count of "F" repeated i times concatenated with "U" repeated j times.

**To do:** Change the makefile so that `main.py` creates the CSV from
live data, rather than `fake.py` creating the CSV from static data.
Once my quota renews :). `main.py` will have to be rewritten a little
to print an "unrolled" rather than square matrix (easy).

Partially inspired by: https://xkcd.com/467/

Example
--------
![Map of Fs versus Us](https://dl.dropboxusercontent.com/u/38640281/github_img/ffuu_map.png)


Admin boringness/links
--------

Go to http://code.google.com/apis/console to get API key for your app.
Also read
https://developers.google.com/console/help/new/?hl=en_US#apikeybestpractices

Documentation for customsearch API:
https://developers.google.com/resources/api-libraries/documentation/customsearch/v1/python/latest/

This documentation reveals that `x.cse().list(...)` are the only
instance methods you can call.

Sample code:
https://github.com/google/google-api-python-client/blob/master/samples/customsearch/main.py

Some other JSON-y thing:
https://developers.google.com/custom-search/json-api/v1/overview
