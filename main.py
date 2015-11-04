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

import pdb
from googleapiclient.discovery import build
from fu_utilities import matrix2csv
mykey = open('apikey.txt', 'r').read().splitlines()[0]
mycx = '001893756405173909803:zmyrda2qwcc' # knowyourmeme + cheezburger + reddit
service = build("customsearch", "v1", developerKey=mykey)

n = 24 # Max number of Fs or Us.
M = []
T = []

for i in range(n):
    M.append([])
    T.append([])
    for j in range(n):
        query = ("f" * (i+1)) + ("u" * (j+1))
        # fixme - print M if error in next line so we don't lose queries
        res = service.cse().list(q=query, cx=mycx).execute()
        c = int(res['searchInformation']['totalResults'])
        M[i].append(c)
        T[i].append(query)

print ','.join(map(lambda x: "u"+str(x.count('u')), T[0])) # header 1,2,3,...
print matrix2csv(M)
