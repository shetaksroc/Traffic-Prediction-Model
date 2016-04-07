import csv
import datetime
with open('output/data3_chunk10.csv','w') as csv1:
	with open('data3_chunk10.csv', 'rb') as csvfile:
		c=0
	
		spamreader = csv.reader(csvfile, delimiter=';', quotechar='|')
		spamwriter = csv.writer(csv1, delimiter=';', quotechar='|')
		for row in spamreader:
			l=row[0].strip("''").split(',')
			#print(l)
			#dt=row[9].strip('""')
			
			

			for i in range(len(l)):
				l[i]=float(l[i])
	
			x=l[9]	
			if(x>0 and x<=30):
				x=0
			if(x>30 and x<=60):
				x=30
			spamwriter.writerow([l[0],l[1],l[2],l[3],l[4],l[5],l[6],l[7],l[8],x,l[10]])	

