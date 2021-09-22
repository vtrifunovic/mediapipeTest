import cv2
import time
import HandTrackingModule as htm
import keyboard

cap = cv2.VideoCapture(0)

detector = htm.handDetector(detectionCon=0.75)
tipIDS = [4,8,12,16,20]

#W,S,A,D
#R, esc, space
#1,2,3,4
while True:
    success, img = cap.read()
    img = detector.findHands(img)
    lmList = detector.findPosition(img, draw=True)
    if len(lmList) != 0:
        for id in range(1,5):
            if (lmList[tipIDS[id]][1] > 50 and lmList[tipIDS[id]][1] < 100) and (lmList[tipIDS[id]][2] > 50 and lmList[tipIDS[id]][2] < 100):
                print("W")
                keyboard.send('k')
                #time.sleep(0.5)
            elif (lmList[tipIDS[id]][1] > 100 and lmList[tipIDS[id]][1] < 150) and (lmList[tipIDS[id]][2] > 50 and lmList[tipIDS[id]][2] < 100):
                print("S")
                keyboard.send('i')
                #time.sleep(0.5)
            elif (lmList[tipIDS[id]][1] > 150 and lmList[tipIDS[id]][1] < 200) and (lmList[tipIDS[id]][2] > 50 and lmList[tipIDS[id]][2] < 100):
                print("A")
                keyboard.send('l')
                #time.sleep(0.5)
            elif (lmList[tipIDS[id]][1] > 200 and lmList[tipIDS[id]][1] < 250) and (lmList[tipIDS[id]][2] > 50 and lmList[tipIDS[id]][2] < 100):
                print("D")
                keyboard.send('m')
                #time.sleep(0.5)
            elif (lmList[tipIDS[id]][1] > 250 and lmList[tipIDS[id]][1] < 300) and (lmList[tipIDS[id]][2] > 50 and lmList[tipIDS[id]][2] < 100):
                print("R")
                keyboard.send('e')
                #time.sleep(0.5)

    cv2.rectangle(img, (50,50),  (100,100), (255,255,255), 2)
    cv2.rectangle(img, (100,50), (150,100), (255,255,255), 2)
    cv2.rectangle(img, (150,50), (200,100), (255,255,255), 2)
    cv2.rectangle(img, (200,50), (250,100), (255,255,255), 2)

    cv2.imshow('Image',img)
    if cv2.waitKey(1) == ord('q'):
            break
