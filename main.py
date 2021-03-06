#!/usr/bin/env python

# Copyright 2015 Andrew J. Zimolzak
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""What is more common: FFFFUUUU, or FFUUUUU, or FFFFFUUU, etc.?"""

from googleapiclient.discovery import build
mykey = open('apikey.txt', 'r').read().splitlines()[0]
mycx = '001893756405173909803:zmyrda2qwcc' #knowyourmeme + cheezburger + reddit
service = build("customsearch", "v1", developerKey=mykey)

print "Fs,Us,count" #csv header

for fs in range(1,8):
    for us in range(1,13):
        query = ("f" * fs) + ("u" * us)
        res = service.cse().list(q=query, cx=mycx).execute()
        c = res['searchInformation']['totalResults']
        print str(fs) + "," + str(us) + "," + c
