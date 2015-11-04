T = [['fu', 'fuu', 'fuuu'],
     ['ffu', 'ffuu', 'ffuuu'],
     ['fffu', 'fffuu', 'fffuuu']]

M = [[711000, 56600, 7290], 
     [20800, 636, 623],
     [392, 253, 1480]]

from fu_utilities import matrix2csv

print ','.join(map(lambda x: "u"+str(x.count('u')), T[0])) # header row 1,2,3,...
print matrix2csv(M)
