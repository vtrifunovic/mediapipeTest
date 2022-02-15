import cv2
import time
import HandTrackingModule as htm
import math
import numpy as np
from datetime import datetime
cap = cv2.VideoCapture(0)

pTime = 0
detector = htm.handDetector(detectionCon = 0.75, maxHands = 1)
kernel = np.ones((5,5), dtype='uint8')

while True:
	success, img = cap.read()
	img = detector.findHands(img)
	lmList = detector.findPosition(img, draw=False)
	if len(lmList) != 0:
		logfile = open('cvlog.txt', 'a+')
		cTime = time.time()
		fps = 1/(cTime-pTime)
		pTime = cTime
		img_hsv  = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
		light_blue = (102, 90, 30)
		dark_blue = (129, 255, 255)
		mask = cv2.inRange(img_hsv, light_blue, dark_blue)
		mask = cv2.erode(mask, (5,5))
		mask = cv2.dilate(mask, (15,15))
		e_detect = cv2.subtract(cv2.dilate(cv2.cvtColor(img, cv2.COLOR_BGR2GRAY), kernel), cv2.erode(cv2.cvtColor(img,cv2.COLOR_BGR2GRAY), kernel))
		CANNY = cv2.Canny(cv2.cvtColor(img, cv2.COLOR_BGR2GRAY), 100, 200)		
		cnts, hier = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
		cnts2, hier2 = cv2.findContours(CANNY, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
		x1, y1 = 1000, 1000
		x2, y2 = 0, 0
		x3, y3 = 1000, 1000
		x4, y4 = 1000, 1000
		CANNY = cv2.cvtColor(CANNY, cv2.COLOR_GRAY2BGR)
		for c in cnts:
			x, y, w, h = cv2.boundingRect(c)
			approx = cv2.approxPolyDP(c,0.01*cv2.arcLength(c,True),True)
			if w < 25 or h < 25 or len(approx) < 12 or len(approx) > 20:
				pass
			else:
				if (x1, y1) == (0, 0):
					x1, y1 = (int(x+w/2), int(y+h/2))
					cv2.drawContours(img, c, -1, (0, 255, 0), thickness=2)
				else:
					if x+y < x1+y1:
						x3, y3 = x1, y1
						x1, y1 = (int(x+w/2), int(y+h/2))
						cv2.drawContours(img, c, -1, (0, 255, 0), thickness=3)
					elif (x3, y3) == (0, 0):
						x3, y3 = (int(x+w/2), int(y+h/2))
						cv2.drawContours(img, c, -1, (0, 255, 255), thickness=3)
					elif y < y3:
						x4, y4 = x3, y3
						x3, y3 = (int(x+w/2), int(y+h/2))
						cv2.drawContours(img, c, -1, (0, 255, 0), thickness=3)
					else:
						x4, y4 = (int(x+w/2), int(y+h/2))
						cv2.drawContours(img, c, -1, (0, 255, 255), thickness=3)
		#x2y2 is always our index finger
		#x1y1 is topleftmost X
		#x3y3 is 2nd  topleftmost X
		#x4y4 should be bottom rightmost X	
		x2, y2 = lmList[8][1], lmList[8][2]
		length = math.hypot(x2-((x1+x3)/2),y2-((y1+y3)/2))
		length2 = math.hypot(x4-x3,y4-y3)
		truelength = np.interp(length, [0, length2], [0,8.25])
		dist = str(f'Time: {datetime.now()}; Distance in inches: {round(truelength, 2)}')
		print(dist)
		cv2.line(img, (int((x1+x3)/2), int((y1+y3)/2)), (x2, y2), (255,15,150), 3)
		cv2.line(img, (x1, y1), (x3, y3), (255, 0, 0), 1)
		cv2.line(img, (x3, y3), (x4, y4), (255, 0, 255), 1)
		cv2.putText(img, f'FPS: {int(fps)}', (10, 30), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0), 3)
		logfile.write(dist+'\n')
		logfile.close()
	cv2.imshow('Image', img)
	if cv2.waitKey(1) == ord('q'):
		break	

'''
img = cv2.imread('test.jpg')
img = cv2.resize(img, (700,900))
img_hsv  = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
light_blue = (102, 75, 75)
dark_blue = (129, 255, 255)
mask = cv2.inRange(img_hsv, light_blue, dark_blue)
mask = cv2.erode(mask, (5,5))
mask = cv2.dilate(mask, (15,15))
cnts, hier = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
for c in cnts:
	x, y, w, h = cv2.boundingRect(c)
	if w < 25 or h < 25:
		pass
	else:
		cv2.drawContours(img, c, -1, (0, 255, 0), thickness=2)
cv2.imshow('img', img)
cv2.imshow('mask', mask)
cv2.waitKey(0)
'''
