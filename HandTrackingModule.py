import cv2
import mediapipe as mp
import time


class HandDetector():
    def __init__(self, static_img_mode=False, maxHands=2, detectionCon=0.5,modelComplexity=1,trackCon=0.5):
        self.static_img_mode = static_img_mode
        self.maxHands = maxHands
        self.detectionCon = detectionCon
        self.modelComplex = modelComplexity
        self.trackCon = trackCon
        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(self.mode, self.maxHands,self.modelComplex,
                                        self.detectionCon, self.trackCon)
        self.mpDraw = mp.solutions.drawing_utils

    
    def findHands(self,img,draw = True):
       imageRGB = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
       self.results = self.hands.process(imageRGB)
       
       if self.results.multi_hand_landmarks:
           for handLms in self.results.multi_hand_landmarks:
               
               if draw:
                   self.mpDraw.draw_landmarks(img, handLms, self.mpHands.HAND_CONNECTIONS)
       return img
   
    def positionFinder(self,image, handNo=0, draw=True):
        lmlist = []
        if self.results.multi_hand_landmarks:
            Hand = self.results.multi_hand_landmarks[handNo]
            for id, lm in enumerate(Hand.landmark):
                h,w,c = image.shape
                cx,cy = int(lm.x*w), int(lm.y*h)
                lmlist.append([id,cx,cy])
            if draw:
                cv2.circle(image,(cx,cy), 15 , (255,0,255), cv2.FILLED)

        return lmlist


def main():
    pTime = 0
    cTime = 0
    cap = cv2.VideoCapture(0)
    
    detector = HandDetector()
    
    while(cap.isOpened()):
        success, img = cap.read()
        img = detector.findHands(img)

        lmList = detector.positionFinder(img)
        if len(lmList) != 0:
            print(lmList[4])

        cTime = time.time()
        fps = 1/(cTime - pTime)
        pTime = cTime
        
        cv2.putText(img,str(int(fps)),(10,70),cv2.FONT_HERSHEY_PLAIN,3,
                (255,0,255),3)
    
        cv2.imshow('Image',img)
        cv2.waitKey(1)

if __name__ == "__main__":
    main()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    # for id, lm in enumerate(handLms.landmark):
    #             # print(id,lm)
    #             h, w, c = img.shape
    #             cx, cy = int(lm.x*w), int(lm.y*h)
    #             print(id,cx,cy)
    #             #    if id == 4:
    #             cv2.circle(img, (cx,cy), 15, (255,0,255), cv2.FILLED)