import cv2 as cv
from cvzone import HandTrackingModule
import mediapipe as mp
cap = cv.VideoCapture(0)

detector = HandTrackingModule.HandDetector()
while True:
    ret,img = cap.read()
    hands,img = detector.findHands(img)

    cv.imshow("Hands Detected",img)
    if cv.waitKey(0)==ord('x'):
        break

cap.release()
cv.destroyAllWindows()
