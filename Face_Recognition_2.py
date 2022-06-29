import cv
import cv2 as cv
#loading the image
img = cv.imread("C:\\Users\\idoch\\PycharmProjects\\pythonforIntermediates\\pythonProject\\Independence_Declaration_USA.jpeg")
#loading haarcascade face file, helps recognise faces in an image.
haar_cascade = cv.CascadeClassifier("C:\\Users\\idoch\\OneDrive - Bar-Ilan University\\Documents\\GitHub\\opencv\\data\\haarcascades\\haarcascade_frontalface_alt2.xml")
#defining the scale of the faces rect
faces_rect = haar_cascade.detectMultiScale(img,scaleFactor=1.15,minNeighbors=1)
#show how many faces were detected
print(f'Number of faces found={len(faces_rect)}')

for (x,y,w,h) in faces_rect:
    cv.rectangle(img, (x,y),(x+w,y+h),(0,255,0),thickness=3)
cv.imshow('Detected Faces',img)

cv.waitKey(0)
