import cv2
import HandTrackingModule as htm
import HandTrackingModule2 as htm2
import keyboard
import numpy as np
import time
import autopy
import threading


def keyboard_run(wLow, wHigh, aLow, aHigh, dLow, dHigh):
    while(True):
        success, img = cap.read()
        img = cv2.flip(img, 1)
        img = img[0:720, 0:640]
        img = detector.findHands(img)
        lmList = detector.findPosition(img, draw=True)
        if len(lmList) != 0:
            for id in range(0, 5):
                if (lmList[tipIDS[id]][1] > wLow and lmList[tipIDS[id]][1] < wHigh) and (
                        lmList[tipIDS[id]][2] > 50 and lmList[tipIDS[id]][2] < 150):
                    print("W")
                    keyboard.press('w')
                    time.sleep(0.1)
                elif (lmList[tipIDS[id]][1] > aLow - 25 and lmList[tipIDS[id]][1] < aHigh - 25) and (
                        lmList[tipIDS[id]][2] > 450 and lmList[tipIDS[id]][2] < 550):
                    print("S")
                    keyboard.press('s')
                    time.sleep(0.1)
                elif (lmList[tipIDS[id]][1] > aLow and lmList[tipIDS[id]][1] < aHigh) and (
                        lmList[tipIDS[id]][2] > 250 and lmList[tipIDS[id]][2] < 350):
                    print("A")
                    keyboard.press('a')
                    time.sleep(0.1)
                elif (lmList[tipIDS[id]][1] > dLow and lmList[tipIDS[id]][1] < dHigh) and (
                        lmList[tipIDS[id]][2] > 250 and lmList[tipIDS[id]][2] < 350):
                    print("D")
                    keyboard.press('d')
                    time.sleep(0.1)
                elif (lmList[tipIDS[id]][1] > 375 and lmList[tipIDS[id]][1] < 475) and (
                        lmList[tipIDS[id]][2] > 50 and lmList[tipIDS[id]][2] < 150):
                    print("R")
                    keyboard.press('r')
                    time.sleep(0.1)
                elif (lmList[tipIDS[id]][1] > dLow + 50 and lmList[tipIDS[id]][1] < dHigh + 50) and (
                        lmList[tipIDS[id]][2] > 350 and lmList[tipIDS[id]][2] < 450):
                    print("1")
                    keyboard.press('1')
                    time.sleep(0.1)
                elif (lmList[tipIDS[id]][1] > dLow + 50 and lmList[tipIDS[id]][1] < dHigh + 50) and (
                        lmList[tipIDS[id]][2] > 450 and lmList[tipIDS[id]][2] < 550):
                    print("2")
                    keyboard.press('2')
                    time.sleep(0.1)
                elif (lmList[tipIDS[id]][1] > dLow + 50 and lmList[tipIDS[id]][1] < dHigh + 50) and (
                        lmList[tipIDS[id]][2] > 550 and lmList[tipIDS[id]][2] < 650):
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
        cv2.rectangle(img, (wLow, 50), (wHigh, 150), (255, 255, 255), 2)
        cv2.putText(img, 'W', (wLow + 25, 120), cv2.FONT_HERSHEY_COMPLEX, 2, (255, 255, 255), 3)
        # s key
        cv2.rectangle(img, (aLow - 25, 450), (aHigh - 25, 550), (255, 255, 255), 2)
        cv2.putText(img, 'S', (aLow, 520), cv2.FONT_HERSHEY_COMPLEX, 2, (255, 255, 255), 3)
        # a key
        cv2.rectangle(img, (aLow, 250), (aHigh, 350), (255, 255, 255), 2)
        cv2.putText(img, 'A', (aLow + 25, 320), cv2.FONT_HERSHEY_COMPLEX, 2, (255, 255, 255), 3)
        # d key
        cv2.rectangle(img, (dLow, 250), (dHigh, 350), (255, 255, 255), 2)
        cv2.putText(img, 'D', (dLow + 25, 320), cv2.FONT_HERSHEY_COMPLEX, 2, (255, 255, 255), 3)
        # r key
        cv2.rectangle(img, (375, 50), (475, 150), (255, 255, 255), 2)
        cv2.putText(img, 'R', (395, 120), cv2.FONT_HERSHEY_COMPLEX, 2, (255, 255, 255), 3)
        # 1 key
        cv2.rectangle(img, (dLow + 50, 350), (dHigh + 50, 450), (255, 255, 255), 2)
        cv2.putText(img, '1', (dLow + 75, 420), cv2.FONT_HERSHEY_COMPLEX, 2, (255, 255, 255), 3)
        # 2 key
        cv2.rectangle(img, (dLow + 50, 450), (dHigh + 50, 550), (255, 255, 255), 2)
        cv2.putText(img, '2', (dLow + 75, 520), cv2.FONT_HERSHEY_COMPLEX, 2, (255, 255, 255), 3)
        # 2 key
        cv2.rectangle(img, (dLow + 50, 550), (dHigh + 50, 650), (255, 255, 255), 2)
        cv2.putText(img, '3', (dLow + 75, 620), cv2.FONT_HERSHEY_COMPLEX, 2, (255, 255, 255), 3)

        cv2.imshow('Image', img)
        if cv2.waitKey(1) == ord('q'):
            return


def mouse_run(wCam, hCam, smoothening, plocX, plocY, clocX, clocY, wScr, hScr, frameR, pTime):
    while(True):
        success, img2 = cap.read()
        img2 = cv2.flip(img2, 1)
        img2 = img2[0:720, 640:1280]
        img2 = detector2.findHands(img2)
        lmList2 = detector2.findPosition(img2)

        if len(lmList2) != 0:
            x1, y1 = lmList2[8][1:3]
            x2, y2 = lmList2[12][1:3]

            fingers = detector2.fingersUp()
            # print(fingers)
            cv2.rectangle(img2, (frameR, frameR), (wCam - frameR, hCam - frameR), (255, 0, 255), 2)
            if fingers[1] == 1 and fingers[2] == 0:
                x3 = np.interp(x1, (frameR, wCam - frameR), (0, wScr))
                y3 = np.interp(y1, (frameR, hCam - frameR), (0, hScr))
                clocX = plocX + (x3 - plocX) / smoothening
                clocY = plocY + (y3 - plocY) / smoothening
                # error check so that input is 1 pixel less than in-game resolution
                csgoW, csgoH = 1279, 959
                if clocX > csgoW:
                    clocX = csgoW
                clocY = plocY + (y3 - plocY) / smoothening
                if clocY > csgoH:
                    clocY = csgoH
                print(clocX, clocY)
                autopy.mouse.move(clocX, clocY)
                cv2.circle(img2, (x1, y1), 15, (255, 0, 255), cv2.FILLED)
                plocX, plocY = clocX, clocY
            elif fingers[1] == 1 and fingers[2] == 1:
                length, img2, lineInfo = detector2.findDistance(8, 12, img2)
                if length < 40:
                    x3 = np.interp(x1, (frameR, wCam - frameR), (0, wScr))
                    y3 = np.interp(y1, (frameR, hCam - frameR), (0, hScr))
                    clocX = plocX + (x3 - plocX) / smoothening
                    if clocX > 1279:
                        clocX = 1279
                    clocY = plocY + (y3 - plocY) / smoothening
                    if clocY > 959:
                        clocY = 959

                    autopy.mouse.move(clocX, clocY)
                    cv2.circle(img2, (x1, y1), 15, (255, 0, 255), cv2.FILLED)
                    plocX, plocY = clocX, clocY
                    cv2.circle(img2, (lineInfo[4], lineInfo[5]), 15, (0, 255, 0), cv2.FILLED)
                    autopy.mouse.click()

        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime
        cv2.putText(img2, str(int(fps)), (20, 50), cv2.FONT_HERSHEY_COMPLEX, 2, (255, 0, 0), 3)
        cv2.imshow("Image2", img2)
        if cv2.waitKey(1) == ord('q'):
            return


if __name__ == '__main__':
    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
    detector = htm.handDetector(detectionCon=0.75)
    detector2 = htm2.handDetector(detectionCon=0.75, maxHands=1)
    tipIDS = [4, 8, 12, 16, 20]
    wLow, wHigh = 200, 300
    aLow, aHigh = 50, 150
    dLow, dHigh = 350, 450
    wCam, hCam = 640, 720
    smoothening = 1
    pTime = 0
    plocX, plocY = 0, 0
    clocX, clocY = 0, 0
    wScr, hScr = autopy.screen.size()
    frameR = 200
    t1 = threading.Thread(target=keyboard_run, args=(wLow, wHigh, aLow, aHigh, dLow, dHigh))
    t2 = threading.Thread(target=mouse_run, args=(wCam, hCam, smoothening, plocX, plocY, clocX, clocY, wScr, hScr, frameR, pTime))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
