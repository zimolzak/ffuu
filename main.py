#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright 2014 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0

"""What is more common: FFFFUUUU, or FFUUUUU, or FFFFFUUU, etc.?

http://code.google.com/apis/console to get API key for your app.

Documentation for customsearch API:
https://developers.google.com/resources/api-libraries/documentation/customsearch/v1/python/latest/

x.cse().list(...) are the only instance methods you can call.
"""

import pdb
from googleapiclient.discovery import build
mykey = open('apikey.txt', 'r').read().splitlines()[0]
service = build("customsearch", "v1", developerKey=mykey)
res = service.cse().list(q='ffffuuuu',
    cx='001893756405173909803:zmyrda2qwcc').execute()
print int(res['searchInformation']['totalResults'])
