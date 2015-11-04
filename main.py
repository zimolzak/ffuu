#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0

"""What is more common: FFFFUUUU, or FFUUUUU, or FFFFFUUU, etc.?"""

import pdb
from googleapiclient.discovery import build
from fu_utilities import matrix2csv
mykey = open('apikey.txt', 'r').read().splitlines()[0]
mycx = '001893756405173909803:zmyrda2qwcc'
service = build("customsearch", "v1", developerKey=mykey)

n = 24 # Max number of Fs or Us.
M = []
T = []

for i in range(n):
    M.append([])
    T.append([])
    for j in range(n):
        query = ("f" * (i+1)) + ("u" * (j+1))
        res = service.cse().list(q=query, cx=mycx).execute()
        c = int(res['searchInformation']['totalResults'])
        M[i].append(c)
        T[i].append(query)

# T = [['fu', 'fuu', 'fuuu'],
#      ['ffu', 'ffuu', 'ffuuu'],
#      ['fffu', 'fffuu', 'fffuuu']]

# M = [[711000, 56600, 7290], 
#      [20800, 636, 623],
#      [392, 253, 1480]]

print ','.join(map(lambda x: "u"+str(x.count('u')), T[0])) # header row 1,2,3,...
print matrix2csv(M)
