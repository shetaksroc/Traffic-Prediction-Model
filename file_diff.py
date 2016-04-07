with open('todays_out.txt','rb') as f1:
	with open('todays_cmp.txt','rb') as f2:
		l1=f1.readlines()
		
		l1=[line.rstrip('\n') for line in l1]
		#print l1
		l2=f2.readlines()
		
		l2=[line.rstrip('\n') for line in l2]
		c=0

		for i,j in zip(l1,l2):
			if(i!=j):
					c=c+1

		print (c*1.0/len(l1))*100