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
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Simple command-line example for Custom Search.
Command-line application that does a search.
"""

import pdb
from googleapiclient.discovery import build

# http://code.google.com/apis/console to get API key for your app.
mykey = open('apikey.txt', 'r').read().splitlines()[0]

def main():
  # Documentation for customsearch API:
  # https://developers.google.com/resources/api-libraries/documentation/customsearch/v1/python/latest/
  service = build("customsearch", "v1",
            developerKey=mykey)
  #pdb.set_trace()
  # x.cse().list(...) are the only instance methods you can call.
  res = service.cse().list( 
      q='ffffuuuu',
      cx='001893756405173909803:zmyrda2qwcc',
      # custom search engine ID. This is CS curriculum.
      # https://cse.google.com/cse/publicurl?cx=017576662512468239146:omuauf_lfve
    ).execute()
  print int(res['searchInformation']['totalResults'])

if __name__ == '__main__':
  main()

# Check out:     u'totalResults': u'62400000'
