import cv2
import time
import HandTrackingModule as htm
import keyboard

cap = cv2.VideoCapture(0)

detector = htm.handDetector(detectionCon=0.75)
tipIDS = [4, 8, 12, 16, 20]
wBox = (50, 100), (50, 100)
#W,S,A,D
#R, esc, space
#1,2,3,4
while True:
    success, img = cap.read()
    img = detector.findHands(img)
    lmList = detector.findPosition(img, draw=True)
    if len(lmList) != 0:
        for id in range(1, 5):
            if (lmList[tipIDS[id]][1] > 50 and lmList[tipIDS[id]][1] < 150) and (lmList[tipIDS[id]][2] > 50 and lmList[tipIDS[id]][2] < 150):
                print("W")
                keyboard.press('w')
                time.sleep(0.1)
            elif (lmList[tipIDS[id]][1] > 150 and lmList[tipIDS[id]][1] < 250) and (lmList[tipIDS[id]][2] > 50 and lmList[tipIDS[id]][2] < 150):
                print("S")
                keyboard.press('s')
                time.sleep(0.1)
            elif (lmList[tipIDS[id]][1] > 250 and lmList[tipIDS[id]][1] < 350) and (lmList[tipIDS[id]][2] > 50 and lmList[tipIDS[id]][2] < 150):
                print("A")
                keyboard.press('a')
                time.sleep(0.1)
            elif (lmList[tipIDS[id]][1] > 350 and lmList[tipIDS[id]][1] < 450) and (lmList[tipIDS[id]][2] > 50 and lmList[tipIDS[id]][2] < 150):
                print("D")
                keyboard.press('d')
                time.sleep(0.1)
            elif (lmList[tipIDS[id]][1] > 450 and lmList[tipIDS[id]][1] < 550) and (lmList[tipIDS[id]][2] > 50 and lmList[tipIDS[id]][2] < 150):
                print("R")
                keyboard.press('r')
                time.sleep(0.1)
            else:
                keyboard.release('w')
                keyboard.release('s')
                keyboard.release('a')
                keyboard.release('d')
                keyboard.release('r')

    cv2.rectangle(img, (50,50),  (150,150), (255,255,255), 2)
    cv2.rectangle(img, (150,50), (250,150), (255,255,255), 2)
    cv2.rectangle(img, (250,50), (350,150), (255,255,255), 2)
    cv2.rectangle(img, (350,50), (450,150), (255,255,255), 2)
    cv2.rectangle(img, (450,50), (550,150), (255,255,255), 2)

    cv2.imshow('Image', img)
    if cv2.waitKey(1) == ord('q'):
            break
