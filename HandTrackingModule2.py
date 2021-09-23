import math
import cv2
import mediapipe as mp
import time


class handDetector():
    def __init__(self, mode=False,maxHands=2,detectionCon=0.5,trackCon = 0.5):
        self.mode = mode
        self.maxHands = maxHands
        self.detectionCon = detectionCon
        self.trackCon = trackCon

        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(self.mode,self.maxHands,self.detectionCon,self.trackCon)
        self.mpDraw = mp.solutions.drawing_utils
        self.tipIDS = [4, 8, 12, 16, 20]

    def findHands(self, img, draw=True):
            imgRGB = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
            self.results = self.hands.process(imgRGB)
            #print(results.multi_hand_landmarks)
            if self.results.multi_hand_landmarks:
                for handLms in self.results.multi_hand_landmarks:
                    if draw:
                        self.mpDraw.draw_landmarks(img, handLms, self.mpHands.HAND_CONNECTIONS)
            return img

    def findPosition(self, img, handNo=0,draw=True):
        self.lmList = []
        # if self.results.multi_handedness:
        # label = self.results.multi_handedness[handNo].classification[0].label  # label gives if hand is left or right
        #    #account for inversion in webcams
        #    if label == "Left":
        #        label = "Right"
        #    elif label == "Right":
        #        label = "Left"
                
        if self.results.multi_hand_landmarks:
            myHand = self.results.multi_hand_landmarks[handNo]
            for id, lm in enumerate(myHand.landmark):
                #print(id,lm)
                h, w, c = img.shape
                cx, cy = int(lm.x*w), int(lm.y*h)
                self.lmList.append([id, cx, cy])
                if draw:
                    cv2.circle(img, (cx,cy), 7, (236,252,3))
        return self.lmList
    
    def amountHands(self, img):
        amount = 0
        if self.results.multi_hand_landmarks:
            for hand in enumerate(self.results.multi_hand_landmarks):
                #print("Hand")
                amount += 1
        return amount

    def fingersUp(self):
        fingers = []
        rightHand = False
        if self.lmList[5][1] > self.lmList[17][1]:
            rightHand = True
        if rightHand:
            if self.lmList[self.tipIDS[0]][1] > self.lmList[self.tipIDS[0] - 1][1]:
                fingers.append(1)
            else:
                fingers.append(0)
        else:
            if self.lmList[self.tipIDS[0]][1] < self.lmList[self.tipIDS[0] - 1][1]:
                fingers.append(1)
            else:
                fingers.append(0)

        for id in range(1,5):
            if self.lmList[self.tipIDS[id]][2] < self.lmList[self.tipIDS[id]-2][2]:
                fingers.append(1)
            else:
                fingers.append(0)
        return fingers

    def findDistance(self, p1, p2, img, draw=True, r=15, t=3):
        x1, y1 = self.lmList[p1][1:]
        x2, y2 = self.lmList[p2][1:]
        cx, cy = (x1+x2)//2, (y1+y2)//2
        if draw:
            cv2.line(img, (x1, y1), (x2, y2), (255, 0, 255), t)
            cv2.circle(img, (x1, y1), r, (255, 0, 255), cv2.FILLED)
            cv2.circle(img, (x2, y2), r, (255, 0, 255), cv2.FILLED)
            cv2.circle(img, (cx, cy), r, (255, 0, 255), cv2.FILLED)
        length = math.hypot(x2-x1, y2-y1)
        return length, img, [x1, y1, x2, y2, cx, cy]



def main():
    
    pTime = 0
    cTime = 0
    
    cap = cv2.VideoCapture(0)

    detector = handDetector()

    while True:
        success, img = cap.read()
        img = detector.findHands(img)
        lmList = detector.findPosition(img)
        if len(lmList) != 0:
            print(lmList[4])
        #imgRGB = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        #results = hands.process(imgRGB)
        print(detector.amountHands(img))
        cTime = time.time()
        fps = 1/(cTime-pTime)
        pTime = cTime

        cv2.putText(img,str(int(fps)), (10,70), cv2.FONT_HERSHEY_PLAIN, 3, (255,0,255),3)

        cv2.imshow("Image",img)
        if cv2.waitKey(1) == ord('q'):
            break

if __name__ == '__main__':
    main()
