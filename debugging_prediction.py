import sys, json
import csv
import cv2
import numpy as np
import os.path
import time
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import csv
from sklearn.externals import joblib
from sklearn.preprocessing import Imputer
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn import preprocessing
from sklearn.metrics import roc_curve, auc
from numpy import genfromtxt, savetxt
number = preprocessing.LabelEncoder()
print 3
rf=joblib.load('model/m1.pkl')
print 4
def convert(data):
	number = preprocessing.LabelEncoder()
	data['st'] = number.fit_transform(data.st)
	data['lat'] = number.fit_transform(data.lat)
	data['long'] = number.fit_transform(data.long)
	data['y'] = number.fit_transform(data.y)
	data['x'] = number.fit_transform(data.x)
	data['weekno'] = number.fit_transform(data.weekno)
	data['weekday'] = number.fit_transform(data.weekday)
	data['hr'] = number.fit_transform(data.hr)
	data['min'] = number.fit_transform(data.min)
	data=data.fillna(0)
	return data
	
cols = ['st', 'lat', 'long', 'y','x','weekno','weekday','hr','min'] 
colsRes = ['pixel']
#with open('model/m1', 'wb') as f:
 #   cPickle.dump(rf, f)
print 10
'''
with open('test/1713.csv','r') as csv1:	
		spamreader = csv.reader(csv1, delimiter=';', quotechar='|')
		
		a=[]
		for row in spamreader:
			l=row[0].strip("''").split(',')
			#print row
			a.append(l)
'''
import numpy as np
#test1=np.genfromtxt('test/1713.csv', dtype= None)
test = pd.read_csv("test/test_data.csv")
#test1=test.fillna('')
#test=convert(test)
#test = genfromtxt(open('test/1713.csv','r'), delimiter=';', dtype='f8')
testArr = test.as_matrix(cols)
print 5
#testArr= Imputer().fit_transform(testArr)
results = rf.predict(test)
print "off"
# something I like to do is to add it back to the data frame, so I can compare side-by-side
#test['predictions'] = results
#test.head()
#result_f = open('result.txt', 'a')


print "fuck"


'''for i in results:
	print i'''
print 6

print 7

'''if(x>=0 and x<=59):
			if(y>=100 and y<=255):
				if(z>=176 and z<=255):
					img[j,i]=[75,54,33]
'''
img=cv2.imread("demo.jpeg");	
for i in range(0,1200):
	for j in range(0,1000):

		x,y,z=img[j,i]
		
		
		if(x>=0 and x<=40):
			if(y>=0 and y<=40):
				if(z>=50 and z<=255):
					img[j,i]=[75, 54, 33]

					#green
		if(x>=60 and x<=150):
			if(y>=100 and y<=255):
				if(z>=0 and z<=175):
					img[j,i]=[75, 54, 33]
		if(x>=0 and x<=59):
			if(y>=100 and y<=255):
				if(z>=176 and z<=255):
					img[j,i]=[75,54,33]
		
																																																																																																												
cv2.imread("out.jpeg");
print 8																																																																																																																																																																																																		
c=0
for m in l:																																																																																																																																																																																																																																																			 																																																																																																																																																																																																																																																																											
	if(m[0]==12):
		print m[0]
			
		for k in m[3]:	
			#print(img[k[3],k[2]])\
			print k
			if(results[c]==1):
				img[k[3],k[2]]=[3,0,236]
			elif(results[c]==2):
				img[k[3],k[2]]=[79,204,130]
			elif(results[c]==3):
				img[k[3],k[2]]=[0,122,244]
			c=c+1		
cv2.imwrite("out2.jpeg",img);

print "out2.jpeg"

#st', 'lat', 'long', 'y','x','weekno','weekday','hr','min'
