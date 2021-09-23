import cv2
import numpy as np
import HandTrackingModule as htm
import time
import autopy

cap = cv2.VideoCapture(0)
wCam = 1280
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
hCam = 720
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
smoothening = 7
pTime = 0
plocX, plocY = 0, 0
clocX, clocY = 0, 0
detector = htm.handDetector(maxHands=1)
wScr, hScr = autopy.screen.size()
frameR = 200
while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)
    img = detector.findHands(img)
    lmList = detector.findPosition(img)

    if len(lmList) != 0:
        x1, y1 = lmList[8][1:3]
        x2, y2 = lmList[12][1:3]

        fingers = detector.fingersUp()
        # print(fingers)
        cv2.rectangle(img, (frameR, frameR), (wCam - frameR, hCam - frameR), (255, 0, 255), 2)
        if fingers[1] == 1 and fingers[2] == 0:
            x3 = np.interp(x1, (frameR, wCam-frameR), (0, wScr))
            y3 = np.interp(y1, (frameR, hCam-frameR), (0, hScr))
            clocX = plocX + (x3-plocX)/smoothening
            clocY = plocY + (y3-plocY)/smoothening

            autopy.mouse.move(clocX, clocY)
            cv2.circle(img, (x1, y1), 15, (255, 0, 255), cv2.FILLED)
            plocX, plocY = clocX, clocY
        elif fingers[1] == 1 and fingers[2] == 1:
            length, img, lineInfo = detector.findDistance(8, 12, img)
            if length < 40:
                x3 = np.interp(x1, (frameR, wCam - frameR), (0, wScr))
                y3 = np.interp(y1, (frameR, hCam - frameR), (0, hScr))
                clocX = plocX + (x3 - plocX) / smoothening
                clocY = plocY + (y3 - plocY) / smoothening

                autopy.mouse.move(clocX, clocY)
                cv2.circle(img, (x1, y1), 15, (255, 0, 255), cv2.FILLED)
                plocX, plocY = clocX, clocY
                cv2.circle(img, (lineInfo[4], lineInfo[5]), 15, (0, 255, 0), cv2.FILLED)
                autopy.mouse.click()

    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime
    cv2.putText(img, str(int(fps)), (20,50), cv2.FONT_HERSHEY_COMPLEX, 2, (255, 0, 0), 3)
    cv2.imshow("Image", img)
    if cv2.waitKey(1) == ord('q'):
            break
