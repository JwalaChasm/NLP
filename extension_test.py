import sys
import re
import numpy as np
from math import sqrt
f = open(sys.argv[1],'r')
meanT = [4.5606060606060606, 4.621212121212121, 4.5606060606060606]
meanF = [2.769230769230769, 3.076923076923077, 2.8461538461538463]
lst1 = [[8.0, 9.0, 0.0], [2.0, 2.0, 1.0], [6.0, 11.0, 3.0], [1.0, 0.0, 0.0], [4.0, 10.0, 2.0], [7.0, 7.0, 0.0], [2.0, 1.0, 0.0], [6.0, 12.0, 2.0], [6.0, 7.0, 0.0], [5.0, 9.0, 1.0], [3.0, 1.0, 1.0], [6.0, 14.0, 1.0], [8.0, 14.0, 5.0], [6.0, 6.0, 0.0], [5.0, 9.0, 0.0], [3.0, 2.0, 0.0], [3.0, 6.0, 0.0], [4.0, 7.0, 0.0], [8.0, 13.0, 2.0], [3.0, 1.0, 0.0], [7.0, 11.0, 2.0], [7.0, 7.0, 1.0], [3.0, 3.0, 0.0], [6.0, 8.0, 1.0]]
lst2 = [[2.0, 1.0, 0.0], [4.0, 3.0, 0.0], [2.0, 1.0, 1.0], [4.0, 2.0, 0.0], [3.0, 2.0, 0.0], [2.0, 3.0, 0.0]]
#f1 = open(sys.argv[2],'r')
#x = f1.readline()
#t = []
#t = re.findall('-*[0-9]+\.[0-9]+',x)
v1 = []
w1 = []
sample = []
for line in f:
        line = line.rstrip("\n")
        v1.append(line)
for l in v1:
       temp = []
       temp1 = []
       temp = re.findall('-*[0-9]+\.[0-9]+',l)
       for k in temp:
           temp1.append(float(k))
       w1.append(temp1)
for i in w1:
   dist_T =sqrt( ((i[0]-meanT[0])*(i[0]-meanT[0])) + ((i[1]-meanT[1])*(i[1]-meanT[1])) + ((i[2]-meanT[2])*(i[2]-meanT[2])) )
   dist_F =sqrt( ((i[0]-meanF[0])*(i[0]-meanF[0])) + ((i[1]-meanF[1])*(i[1]-meanF[1])) + ((i[2]-meanF[2])*(i[2]-meanF[2])) )
   #print dist_T
   #print dist_F
   count1 = 0.0
   count2 = 0.0
   for j in lst1:
      d1 =sqrt( ((i[0]-j[0])*(i[0]-j[0])) + ((i[1]-j[1])*(i[1]-j[1])) + ((i[2]-j[2])*(i[2]-j[2])) )
      if dist_T < d1:
           count1 = count1 + 3
      else:
           count1 = count1 + 1
   for k in lst2:
      d1 =sqrt( ((i[0]-k[0])*(i[0]-k[0])) + ((i[1]-k[1])*(i[1]-k[1])) + ((i[2]-k[2])*(i[2]-k[2])) )
      #print dist_F,d1
      if dist_F < d1:
           count2 = count2 + 3
      else:
           count2 = count2+ 1

   if count1 > count2:
      	print "TRUE"
   else:
        print "False"
   
'''for i in w1:
    pro = 4*i[0]+ 4*i[1] + 2*i[2]
    if pro > mean:
        print "True"
    else:
        print "False"'''
