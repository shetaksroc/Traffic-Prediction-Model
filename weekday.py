import csv
import datetime
with open('today/data(3)_chunk1_o.csv','w') as csv1:
	with open('today/data(3)_chunk1.csv', 'rb') as csvfile:
		c=0
	
		spamreader = csv.reader(csvfile, delimiter=';', quotechar='|')
		spamwriter = csv.writer(csv1, delimiter=',', quotechar='|')
		spamwriter.writerow(["st","lat","long","y","x","year","month","day","weekno","weekday","hr","min","pixel"])
		for row in spamreader:
			l=row[0].strip("''").split(',')
			#print(l)
			for i in range(len(l)):
				l[i]=l[i].strip('""')
			
			#6 and 7 remove 0 also split 8 into dt and time and split dt into yr,mn,dy time into hr,mn,sec

			dt,time=l[8].split(' ')
			yr,mn,dy=map(int,dt.split('-'))
			hr,mns,sec=map(int,time.split('-'))

			for i in range(1,6):
				l[i]=float(l[i])

			
			l[9]=int(l[9])
			x=mns	
			if(x>0 and x<=30):
				x=0
			if(x>30 and x<=60):
				x=30
			
			#print row
			week_dy=datetime.datetime(yr,mn,dy).weekday()
			week_number = (dy - 1) // 7 + 1
			spamwriter.writerow([l[1],l[2],l[3],l[4],l[5],yr,mn,dy,week_number,week_dy,hr,x,l[9]])	

