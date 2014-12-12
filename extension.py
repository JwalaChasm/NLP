from decimal import *
import re
import sys
from math import sqrt
f = open(sys.argv[1],'r')
v1 = []
v2 = []
w1 = []
w2 = []
for line in f:
        line = line.rstrip("\r\n")
        lst = []
        lst = line.split('\t')
        #print lst
        if lst[1] == 'True':
        	v1.append(lst[0])
        else:
		v2.append(lst[0])
    #print v1,v2
        
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
#print w1,w2
t_dict ={}
f_dict = {}
'''for i in w1:
    pro = 4*i[0]+ 4*i[1] + 2*i[2]
    t_dict[str(i)] = pro
for i in w2:
    pro = 4*i[0]+ 4*i[1] + 2*i[2]
    f_dict[str(i)] = pro    
print t_dict
print f_dict
t_list = []
f_list = []
for i in t_dict:
    t_list.append(t_dict[i])
for i in f_dict:
    f_list.append(f_dict[i])'''
x_cord = 0.0
y_cord = 0.0
z_cord = 0.0
s_T = float(len(w1))
s_F = float(len(w2))
for i in w1:
   x_cord = x_cord + i[0]
   y_cord = x_cord + i[1]
   z_cord = x_cord + i[2]
meanT = [x_cord/s_T, y_cord/s_T, z_cord/s_T]
x_cord = 0.0
y_cord = 0.0
z_cord = 0.0
for i in w2:
   x_cord = x_cord + i[0]
   y_cord = x_cord + i[1]
   z_cord = x_cord + i[2]
meanF = [x_cord/s_F, y_cord/s_F, z_cord/s_F]
print meanT
print meanF
dist = sqrt( ((meanF[0]-meanT[0])*(meanF[0]-meanT[0])) + ((meanF[1]-meanT[1])*(meanF[1]-meanT[1])) + ((meanF[2]-meanT[2])*(meanF[2]-meanT[2])) )
lst = []
x1 = {}
x2 = {}
for i in w1:
     tem =sqrt( ((i[0]-meanT[0])*(i[0]-meanT[0])) + ((i[1]-meanT[1])*(i[1]-meanT[1])) + ((i[2]-meanT[2])*(i[2]-meanT[2])) )
     x1[tem] =i
     lst.append(tem)
lst.sort()
lst = lst[len(lst)/2:len(lst)]
lst2 = []
for i in w2:
     tem = sqrt( ((i[0]-meanF[0])*(i[0]-meanF[0])) + ((i[1]-meanF[1])*(i[1]-meanF[1])) + ((i[2]-meanF[2])*(i[2]-meanF[2])) )
     x2[tem]  = i
     lst2.append(tem)
lst2.sort()
lst2 = lst2[len(lst2)/2:len(lst2)]
true = []
false = []
for i in x1: 
   if i in lst:
      true.append(x1[i])
for i in x2: 
   if i in lst2:
      false.append(x2[i])    
print true
print false
'''dist_dict = {}
for i in w1:
     for k in w2:
         dist_dict[(i,k)] =sqrt( (i[0] -k[0])*(i[0] -k[0])

print dist_dict lst2
#min_ele = min(t_list)
#max_ele = max(f_list)
#mean = (min_ele + max_ele)/2
#print mean'''
   
