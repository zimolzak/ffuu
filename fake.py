T = [['fu', 'fuu', 'fuuu'],
     ['ffu', 'ffuu', 'ffuuu'],
     ['fffu', 'fffuu', 'fffuuu']]

M = [[711000, 56600, 7290], 
     [20800, 636, 623],
     [392, 253, 1480]]

print "Fs,Us,count"
for i in range(len(M)):
    for j in range(len(M[i])):
        print str(i+1) + "," + str(j+1) + "," + str(M[i][j])
