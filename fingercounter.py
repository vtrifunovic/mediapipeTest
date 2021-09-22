import cv2
import time
import os
import HandTrackingModule as htm

cap = cv2.VideoCapture(0)

pTime = 0
detector = htm.handDetector(detectionCon=0.75)

tipIDS = [4,8,12,16,20]

while True:
    success, img = cap.read()
    img = detector.findHands(img)
    fingers = []
    rightHand = False
    lmList = detector.findPosition(img, draw=True)
    #print(lmList)
    #print(detector.findPosition.landmark)
    if len(lmList) != 0:
        #thumb
        if lmList[5][1] > lmList[17][1]:
            rightHand = True
        if rightHand:
            if lmList[tipIDS[0]][1] > lmList[tipIDS[0]-1][1]:
                fingers.append(1)
            else:
                fingers.append(0)
        else:
            if lmList[tipIDS[0]][1] < lmList[tipIDS[0]-1][1]:
                fingers.append(1)
            else:
                fingers.append(0)
        #rest of fingers
        for id in range(1,5):
            if lmList[tipIDS[id]][2] < lmList[tipIDS[id]-2][2]:
                fingers.append(1)
            else:
                fingers.append(0)
        print(fingers)

    totalFingers = fingers.count(1)
    #print(totalFingers)
    cv2.putText(img, f'Fingers: {totalFingers}', (10,70), cv2.FONT_HERSHEY_COMPLEX, 1, (255,255,255), 3)
    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime
    
    cv2.putText(img, f'FPS: {int(fps)}', (10,30), cv2.FONT_HERSHEY_COMPLEX, 1, (255,0,0), 3)
    cv2.imshow('Image',img)
    if cv2.waitKey(1) == ord('q'):
            break
