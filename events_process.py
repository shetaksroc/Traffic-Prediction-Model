import csv
import datetime
with open('events/townhall_out.csv','w') as csv1:
	with open('events/townhall.csv', 'rb') as csvfile:
		spamreader = csv.reader(csvfile, delimiter=';', quotechar='|')
		spamwriter = csv.writer(csv1, delimiter=',', quotechar='|')
		spamwriter.writerow(["event_id","lat","long","y","x","year","month","day","weekno","weekday","hr","min","pixel"])
		for row in spamreader:
			l=row[0].strip("''").split(',')
			#print(l)
			#dt=row[9].strip('""')
			for i in range(len(l)):
				l[i]=l[i].strip('""')
			date_split=l[6].split(' ')
			final_split=[]
			for i in date_split:
				date_time=i.split('-')
				for j in date_time:
					j.strip('"')

					final_split.append(j)
			#for i in range(len(l)):
			#	l[i]=float(l[i])   
			#print l
			#print final_split
			data=l[1:6]
			for i in range(0,len(data)-2):
				data[i]=float(data[i])
			data[2]=int(data[2])
			data[3]=int(data[3])
			data[4]=int(data[4])	
			#print data

			for i in range(0,len(final_split)):
				final_split[i]=int(final_split[i])
			pixel=data[4]	
			year=final_split[0]
			month=final_split[1]
			day=final_split[2]
			hour=final_split[3]
			minutes=final_split[4]
			# for processing events see anothor file events.py
			#x=l[9]	

			week_day=datetime.datetime(year,month,day).weekday()
			week_number = (day - 1) // 7 + 1
			if(minutes>0 and minutes<=30):
				minutes=0
			if(minutes>30 and minutes<=60):
				minutes=30
			spamwriter.writerow([5,data[0],data[1],data[2],data[3],year,month,day,week_number,week_day,hour,minutes,pixel])	

