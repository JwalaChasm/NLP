import sys
import re
import numpy as np
from math import sqrt
f = open(sys.argv[1],'r')
meanT = [3.4177924217462934, 3.4177924217462934, 3.4191103789126855]
meanF = [2.1187139323990105, 2.1187139323990105, 2.1187139323990105]
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
   if dist_T < dist_F:
      print "True"
   else:
      print "False"
   
'''for i in w1:
    pro = 4*i[0]+ 4*i[1] + 2*i[2]
    if pro > mean:
        print "True"
    else:
        print "False"'''
