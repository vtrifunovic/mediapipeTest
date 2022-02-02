import cv2
import time
import HandTrackingModule as htm
import PoseModule as pm
import math
import numpy as np

cap = cv2.VideoCapture(0)

pTime = 0
detector = htm.handDetector(detectionCon = 0.75, maxHands = 1)
bdetector = pm.poseDetector()

while True:
	success, img = cap.read()
	img = detector.findHands(img)
	lmList = detector.findPosition(img, draw=False)
	if len(lmList) != 0:
		cTime = time.time()
		fps = 1/(cTime-pTime)
		pTime = cTime
		img_hsv  = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
		light_blue = (102, 70, 70)
		dark_blue = (129, 255, 255)
		mask = cv2.inRange(img_hsv, light_blue, dark_blue)
		mask = cv2.erode(mask, (5,5))
		mask = cv2.dilate(mask, (15,15))
		cnts, hier = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
		x1, y1 = 0, 0
		x2, y2 = 0, 0
		x3, y3 = 0, 0
		
		for c in cnts:
			x, y, w, h = cv2.boundingRect(c)
			if w < 25 or h < 25:
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
					else:
						x3, y3 = (int(x+w/2), int(y+h/2))
						cv2.drawContours(img, c, -1, (0, 255, 255), thickness=3)
	
		x2, y2 = lmList[8][1], lmList[8][2]
		length = math.hypot(x2-x1,y2-y1)
		length2 = math.hypot(x3-x1,y3-y1)
		truelength = np.interp(length, [0, length2], [0,10])
		print(f'Distance in px: {int(length)}; Distance in inches: {round(truelength, 2)}')
		cv2.line(img, (x1, y1), (x2, y2), (255,15,150), 3)
		cv2.putText(img, f'FPS: {int(fps)}', (10, 30), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0), 3)
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
