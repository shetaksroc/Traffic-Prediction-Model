import cv2
import numpy as np
import os.path
import time
img=cv2.imread("demo.jpeg");

for i in range(0,1200):
	for j in range(0,1000):
		
		img[j,i]=[255,255,255]


cv2.imwrite("out.jpeg",img);