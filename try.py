import cv2
import numpy as np
import os.path
import time

img=cv2.imread("ny-kg.jpeg");

#print(img[786,694])
l=[]
560,395
562,546

for s in range(0,798):
	for d in range(0,1196): 
		x,y,z=img[s,d]
				#print x,y,z
		if(x>=250 and y>=250 and z>=250):
			l.append([s,d])

print(l)			
			