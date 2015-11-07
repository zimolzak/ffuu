FFFFFFFUUUUUUUUUUUU-
========

What is more common: FFFFUUUU, or FFUUUUU, or FFFFFUUU, etc.?

The original comic uses the text
"FFFFFFFFFFFFFFFFFFFFFFFUUUUUUUUUUUUUUUUUUUUUU-", which is to say,
f23u22. Somehow f7u12 got promulgated too. But other variations are
probably easier to type. So use Google Custom Search API to construct
a matrix where the (i,j) element is the search count of "F" repeated i
times concatenated with "U" repeated j times.

Partially inspired by: https://xkcd.com/467/

Example
--------
![Map of Fs versus Us](https://dl.dropboxusercontent.com/u/38640281/github_img/ffuu_map.png)

To do
--------
* Extend out to about 23 x 23. Maybe I will pay 5 bucks to Google.

Usage
--------

1. May have to `sudo pip install --upgrade google-api-python-client`.
Or maybe `easy_install` instead of `pip`.

2. Get your developer key at http://code.google.com/apis/console . Put
  it in `apikey.txt` because
  https://developers.google.com/console/help/new/?hl=en_US#apikeybestpractices

3. Also depends on python, R, and ggplot2

4. `make`

5. Look at pretty picture of silly Internet semi-swear-word meme.

6. If you are me, then `make github`, otherwise don't.

7. `make clean` if you no longer want the pictures.


Admin boringness/links
--------

Documentation for customsearch API:
https://developers.google.com/resources/api-libraries/documentation/customsearch/v1/python/latest/

This documentation reveals that `x.cse().list(...)` are the only
instance methods you can call.

Sample code:
https://github.com/google/google-api-python-client/blob/master/samples/customsearch/main.py
