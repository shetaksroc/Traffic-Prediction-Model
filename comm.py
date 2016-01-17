import os
import time

while True:
	cmd = 'phantomjs github.js > out.txt'
	os.system(cmd)
	time.sleep(10)
	os.system('fin.py')
	time.sleep(10)
	