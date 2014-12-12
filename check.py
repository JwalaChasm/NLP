import sys
import re
import numpy as np
f = open(sys.argv[1],'r')
f1 = open(sys.argv[2],'r')
x = f1.readline()
t = []
t = re.findall('-*[0-9]+\.[0-9]+',x)
x = []
a = []
ent_samp_class = [] 
for i in t:
     x.append(float(i))
a.append(x)
    

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
       print temp
       for k in temp:
           temp1.append(float(k))
       w1.append(temp1)
print w1
for i in w1:
   	i.insert(0,1.0)
   	ent_samp_class.append(i)
print ent_samp_class
for k in ent_samp_class:
    y = np.array(k)[np.newaxis]
    print y 
    product = np.dot(a,y.T)
    if product > 0:
       print "True\n"
    else:
       print "False\n"
       

   
