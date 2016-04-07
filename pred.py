
# First let's import the dataset, using Pandas.
import pandas as pd
import csv
import glob	
from sklearn.ensemble import RandomForestClassifier
from sklearn.externals import joblib
import os

l = os.listdir("train")
#print len(l)
# make sure you're in the right directory if using iPython!


rf = RandomForestClassifier(n_estimators=100) # initialize
filenames = glob.glob("train/*.csv")
print(len(filenames))
for i in filenames:
	try:
		print i
		cols = ['st', 'lat', 'long', 'y','x','weekno','weekday','hr','min'] 
		colsRes = ['pixel']
		train1 = pd.read_csv(i)
		#train2 = pd.read_csv("d1_1_out.csv")
		#test = pd.read_csv("data3_chunk10.csv")

		train1.head()
		#train2.head()


		# if you don't have the packages installed for this,
		# you will get an error.

		# the data have to be in a numpy array in order for
		# the random forest algorithm to accept it!
		# Also, output must be separated.

		trainArr1 = train1.as_matrix(cols) #training array
		trainRes1 = train1.as_matrix(colsRes) # training results

		#trainArr2 = train2.as_matrix(cols) #training array
		#trainRes2 = train2.as_matrix(colsRes) # training results

		## Training!

		rf.fit(trainArr1, trainRes1) # fit the data to the algorithm
		#rf.fit(trainArr2, trainRes2) # fit the data to the algorithm
		# note - you might get an warning saying you entered a 2 column
		# vector..ignore it. If you know how to get around this warning,
		# please comment! The algorithm seems to work anyway.
		## Testing!
		# put the test data in the same format!
		print i

	except Exception:
		print 'hai'

joblib.dump(rf, 'model/m1.pkl')
	#with open('model/m1', 'wb') as f:
	 #   cPickle.dump(rf, f)
	#testArr = test.as_matrix(cols)
	#results = rf.predict(testArr)
	# something I like to do is to add it back to the data frame, so I can compare side-by-side
	#test['predictions'] = results
	#test.head()
	#result_f = open('result.txt', 'a')
	#for i in results:
	#	print(i)