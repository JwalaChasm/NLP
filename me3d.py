import pylab
import pylab as pl
import random
import numpy as np
import matplotlib.pyplot as plt
import time
import sys
import re
#w1 = [[1,2]]
#w2 = [[2,1]]

def batch(ent_samp_class,a):
   misclasf = []
   for i in ent_samp_class:
    	y = np.array(i)[np.newaxis]
    	#print "sample:",
    	#print y
    	#print a
    	product = np.dot(a,y.T)
    	#print product
    	if product < 0:
        	misclasf.append(y)
   return misclasf
   #new_a = update(misclasf,a,ent_samp_class)
   #batch(ent_samp_class,new_a)
def update(misclasf,a,ent_samp_class):
        #if len(misclasf) > 13:
        for i in misclasf:
   	      a = a + i
        return a
                #batch(ent_samp_class,a)
        #if len(misclasf)==0:
        '''else:
               print a
               g = open("3d_vec.txt",'w')
               g.write(str(a))
               #plot_graph(a)'''
def plot_graph(a):
        #print "gvjhvku"
        #print a
	x = random.randint(0,50)
	x_coords = []
	y_coords = []
	for i in range(100):
  		x = random.randint(0,50)
  		y = (-((x*a[0][1])) -a[0][0])/a[0][2]
  		x_coords.append(x)
  		y_coords.append(y)
	plt.plot(x_coords,y_coords)
	plt.show()
def func1():
    v1 = []
    v2 = []
    w1 = []
    w2 = []
    f = open(sys.argv[1],'r')
    for line in f:
        line = line.rstrip("\r\n")
        lst = []
        lst = line.split('\t')
        print lst
        if lst[1] == 'True':
        	v1.append(lst[0])
        else:
		v2.append(lst[0])
    print v1,v2
        
    for l in v1:
       temp = []
       temp1 = []
       temp = re.findall('-*[0-9]+\.*[0-9]*',l)
       for k in temp:
           temp1.append(float(k))
       w1.append(temp1)
    for l in v2:
       temp = []
       temp1 = []
       temp = re.findall('-*[0-9]+\.*[0-9]*',l)
       for k in temp:
           temp1.append(float(k))
       w2.append(temp1)
       
         
       
 
    #w1 = [[1, 6], [7, 2], [8, 9], [9, 9], [4, 8], [8, 5]]
    #w2 = [[2, 1], [3, 3], [2, 4], [7, 1], [1, 3], [5, 2]]
    a = np.array([(random.randint(1,9))*0.1, (random.randint(1,9))*0.1, (random.randint(1,9))*0.1, (random.randint(1,9))*0.1])[np.newaxis]
    print "Initial a:",
    print a
    print w1,w2
    ent_samp_class = []
    misclasf = []
    '''X1 = []
    Y1 = []
    Z1 = []
    X2 = []
    Y2 = []
    Z2 = []      
    for i in w1:
   	X1.append(i[0])
   	Y1.append(i[1])
        Z1.append(i[2])
    for j in w2:
    	X2.append(j[0])
    	Y2.append(j[1])
        Z2.append(j[2])
    pylab.xlim([0,10])
    pylab.ylim([0,10])
    pylab.zlim([0,10])
    pl.plot(X1,Y1,Z1,'go')
    pl.plot(X2,Y2,Z2,'bo')'''
    for j in w2:
        for k in range(len(j)):
                j[k] = j[k] * (-1)
    #x = pl.show()
    #a = 3*[1*[random.random()]]
    #a = np.array([random.randint(1,10), random.randint(1,10), random.randint(1,10)])[np.newaxis]
    #print a
    #print a.T
    for i in w1:
   	i.insert(0,1)
   	ent_samp_class.append(i)
    for i in w2:
   	i.insert(0,-1)
   	ent_samp_class.append(i)
    #print ent_samp_class
    miscl = batch(ent_samp_class,a)
    p = len(miscl)
    q = len(miscl)
    # = batch(ent_samp_class,a)
    while (p >= q):
        print p,q
        q = p
        a = update(miscl,a,ent_samp_class)
        miscl = batch(ent_samp_class,a)
        p = len(miscl)
        print p
    print "final",a



func1()
