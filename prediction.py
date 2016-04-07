import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import csv
from sklearn.externals import joblib
rf=joblib.load('model/m1.pkl')
cols = ['st', 'lat', 'long', 'y','x','weekno','weekday','hr','min'] 
colsRes = ['pixel']
#with open('model/m1', 'wb') as f:
 #   cPickle.dump(rf, f)
test = pd.read_csv("1713.csv")
testArr = test.as_matrix(cols)
results = rf.predict(testArr)
# something I like to do is to add it back to the data frame, so I can compare side-by-side
#test['predictions'] = results
#test.head()
#result_f = open('result.txt', 'a')
for i in results:
	print(i)