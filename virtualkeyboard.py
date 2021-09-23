import cv2
import time
import HandTrackingModule as htm
import keyboard

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
detector = htm.handDetector(detectionCon=0.75)
tipIDS = [4, 8, 12, 16, 20]
wBox = (50, 100), (50, 100)
# W,S,A,D
# R, esc, space
# 1,2,3,4
wLow = 200
wHigh = 300
aLow = 50
aHigh = 150
dLow = 350
dHigh = 450
while True:
    success, img = cap.read()
    img = cv2.flip(img,1)
    img = img[0:720,0:640]
    img = detector.findHands(img)
    lmList = detector.findPosition(img, draw=True)
    if len(lmList) != 0:
        for id in range(0, 5):
            if (lmList[tipIDS[id]][1] > wLow and lmList[tipIDS[id]][1] < wHigh) and (lmList[tipIDS[id]][2] > 50 and lmList[tipIDS[id]][2] < 150):
                print("W")
                keyboard.press('w')
                time.sleep(0.1)
            elif (lmList[tipIDS[id]][1] > aLow-25 and lmList[tipIDS[id]][1] < aHigh-25) and (lmList[tipIDS[id]][2] > 450 and lmList[tipIDS[id]][2] < 550):
                print("S")
                keyboard.press('s')
                time.sleep(0.1)
            elif (lmList[tipIDS[id]][1] > aLow and lmList[tipIDS[id]][1] < aHigh) and (lmList[tipIDS[id]][2] > 250 and lmList[tipIDS[id]][2] < 350):
                print("A")
                keyboard.press('a')
                time.sleep(0.1)
            elif (lmList[tipIDS[id]][1] > dLow and lmList[tipIDS[id]][1] < dHigh) and (lmList[tipIDS[id]][2] > 250 and lmList[tipIDS[id]][2] < 350):
                print("D")
                keyboard.press('d')
                time.sleep(0.1)
            elif (lmList[tipIDS[id]][1] > 375 and lmList[tipIDS[id]][1] < 475) and (lmList[tipIDS[id]][2] > 50 and lmList[tipIDS[id]][2] < 150):
                print("R")
                keyboard.press('r')
                time.sleep(0.1)
            elif (lmList[tipIDS[id]][1] > dLow+50 and lmList[tipIDS[id]][1] < dHigh+50) and (lmList[tipIDS[id]][2] > 350 and lmList[tipIDS[id]][2] < 450):
                print("1")
                keyboard.press('1')
                time.sleep(0.1)
            elif (lmList[tipIDS[id]][1] > dLow+50 and lmList[tipIDS[id]][1] < dHigh+50) and (lmList[tipIDS[id]][2] > 450 and lmList[tipIDS[id]][2] < 550):
                print("2")
                keyboard.press('2')
                time.sleep(0.1)
            elif (lmList[tipIDS[id]][1] > dLow+50 and lmList[tipIDS[id]][1] < dHigh+50) and (lmList[tipIDS[id]][2] > 550 and lmList[tipIDS[id]][2] < 650):
                print("3")
                keyboard.press('3')
                time.sleep(0.1)
            else:
                keyboard.release('w')
                keyboard.release('s')
                keyboard.release('a')
                keyboard.release('d')
                keyboard.release('r')
                keyboard.release('1')
                keyboard.release('2')
                keyboard.release('3')
            
    # w key
    cv2.rectangle(img, (wLow,50),  (wHigh,150), (255,255,255), 2)
    cv2.putText(img, 'W', (wLow+25, 120), cv2.FONT_HERSHEY_COMPLEX, 2, (255, 255, 255), 3)
    # s key
    cv2.rectangle(img, (aLow-25,450), (aHigh-25,550), (255,255,255), 2)
    cv2.putText(img, 'S', (aLow, 520), cv2.FONT_HERSHEY_COMPLEX, 2, (255, 255, 255), 3)
    # a key
    cv2.rectangle(img, (aLow,250), (aHigh,350), (255,255,255), 2)
    cv2.putText(img, 'A', (aLow+25, 320), cv2.FONT_HERSHEY_COMPLEX, 2, (255, 255, 255), 3)
    # d key
    cv2.rectangle(img, (dLow,250), (dHigh,350), (255,255,255), 2)
    cv2.putText(img, 'D', (dLow+25, 320), cv2.FONT_HERSHEY_COMPLEX, 2, (255, 255, 255), 3)
    # r key
    cv2.rectangle(img, (375,50), (475,150), (255,255,255), 2)
    cv2.putText(img, 'R', (395, 120), cv2.FONT_HERSHEY_COMPLEX, 2, (255, 255, 255), 3)
    # 1 key
    cv2.rectangle(img, (dLow+50, 350), (dHigh+50, 450), (255, 255, 255), 2)
    cv2.putText(img, '1', (dLow + 75, 420), cv2.FONT_HERSHEY_COMPLEX, 2, (255, 255, 255), 3)
    # 2 key
    cv2.rectangle(img, (dLow+50, 450), (dHigh+50, 550), (255, 255, 255), 2)
    cv2.putText(img, '2', (dLow + 75, 520), cv2.FONT_HERSHEY_COMPLEX, 2, (255, 255, 255), 3)
    # 2 key
    cv2.rectangle(img, (dLow+50, 550), (dHigh+50, 650), (255, 255, 255), 2)
    cv2.putText(img, '3', (dLow + 75, 620), cv2.FONT_HERSHEY_COMPLEX, 2, (255, 255, 255), 3)

    cv2.imshow('Image', img)
    if cv2.waitKey(1) == ord('q'):
            break
