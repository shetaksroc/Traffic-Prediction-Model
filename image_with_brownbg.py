import cv2
img=cv2.imread("demo.jpeg")
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
cv2.imwrite("out3.jpeg",img);					