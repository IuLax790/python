import cv
import cv2 as cv
#loading the image
img = cv.imread("C:\\Users\\idoch\\OneDrive - Bar-Ilan University\\Pictures\\Screenshots\\images.jpg")
img2 = cv.imread("C:\\Users\\idoch\\OneDrive - Bar-Ilan University\\Pictures\\Screenshots\\images (1).jpg")
img3 = cv.imread("C:\\Users\\idoch\\OneDrive - Bar-Ilan University\\Pictures\\Screenshots\\hqdefault.jpg")
img4 = cv.imread("C:\\Users\\idoch\\OneDrive - Bar-Ilan University\\Pictures\\Screenshots\\White_Cats.jpg")
img5 = cv.imread("C:\\Users\\idoch\\OneDrive - Bar-Ilan University\\Pictures\\Screenshots\\puppies-kittens-group-different-breeds-cat-dog-30615033.jpg")
img6 = cv.imread("C:\\Users\\idoch\\OneDrive - Bar-Ilan University\\Pictures\\Screenshots\\_115537288_hi000618024.jpg")
img7 = cv.imread("C:\\Users\\idoch\\OneDrive - Bar-Ilan University\\Pictures\\Screenshots\\_115537288_hi000618024.jpg")
img8 = cv.imread("C:\\Users\\idoch\\OneDrive - Bar-Ilan University\\Pictures\\Screenshots\\_115537288_hi000618024.jpg")
img9 = cv.imread("C:\\Users\\idoch\\OneDrive - Bar-Ilan University\\Pictures\\Screenshots\\_115537288_hi000618024.jpg")
img10 = cv.imread("C:\\Users\\idoch\\OneDrive - Bar-Ilan University\\Pictures\\Screenshots\\_115537288_hi000618024.jpg")


#loading haarcascade face file, helps recognise faces in an image.
haar_cascade = cv.CascadeClassifier("C:\\Users\\idoch\\OneDrive - Bar-Ilan University\\Documents\\GitHub\\opencv\\data\\haarcascades\\haarcascade_frontalcatface.xml")
#defining the scale of the faces rect
faces_rect = haar_cascade.detectMultiScale(img,scaleFactor=1.1,minNeighbors=3)
#show how many faces were detected
print(f'Number of faces found={len(faces_rect)}')

for (x,y,w,h) in faces_rect:
    cv.rectangle(img, (x,y),(x+w,y+h),(0,255,0),thickness=3)
cv.imshow('Detected Faces',img)

cv.waitKey(0)

faces_rect = haar_cascade.detectMultiScale(img2,scaleFactor=1.17,minNeighbors=0)
#show how many faces were detected
print(f'Number of faces found={len(faces_rect)}')

for (x,y,w,h) in faces_rect:
    cv.rectangle(img2, (x,y),(x+w,y+h),(0,255,0),thickness=3)
cv.imshow('Detected Faces',img2)

cv.waitKey(0)

faces_rect = haar_cascade.detectMultiScale(img3,scaleFactor=1.17,minNeighbors=0)
#show how many faces were detected
print(f'Number of faces found={len(faces_rect)}')

for (x,y,w,h) in faces_rect:
    cv.rectangle(img3, (x,y),(x+w,y+h),(0,255,0),thickness=3)
cv.imshow('Detected Faces',img3)

cv.waitKey(0)

faces_rect = haar_cascade.detectMultiScale(img4,scaleFactor=1.17,minNeighbors=0)
#show how many faces were detected
print(f'Number of faces found={len(faces_rect)}')

for (x,y,w,h) in faces_rect:
    cv.rectangle(img4, (x,y),(x+w,y+h),(0,255,0),thickness=3)
cv.imshow('Detected Faces',img4)

cv.waitKey(0)

faces_rect = haar_cascade.detectMultiScale(img5,scaleFactor=1.17,minNeighbors=0)
#show how many faces were detected
print(f'Number of faces found={len(faces_rect)}')

for (x,y,w,h) in faces_rect:
    cv.rectangle(img5, (x,y),(x+w,y+h),(0,255,0),thickness=3)
cv.imshow('Detected Faces',img5)

cv.waitKey(0)

faces_rect = haar_cascade.detectMultiScale(img6,scaleFactor=1.17,minNeighbors=0)
#show how many faces were detected
print(f'Number of faces found={len(faces_rect)}')

for (x,y,w,h) in faces_rect:
    cv.rectangle(img6, (x,y),(x+w,y+h),(0,255,0),thickness=3)
cv.imshow('Detected Faces',img6)

cv.waitKey(0)

faces_rect = haar_cascade.detectMultiScale(img7,scaleFactor=1.17,minNeighbors=0)
#show how many faces were detected
print(f'Number of faces found={len(faces_rect)}')

for (x,y,w,h) in faces_rect:
    cv.rectangle(img7, (x,y),(x+w,y+h),(0,255,0),thickness=3)
cv.imshow('Detected Faces',img7)

cv.waitKey(0)

faces_rect = haar_cascade.detectMultiScale(img8,scaleFactor=1.17,minNeighbors=0)
#show how many faces were detected
print(f'Number of faces found={len(faces_rect)}')

for (x,y,w,h) in faces_rect:
    cv.rectangle(img8, (x,y),(x+w,y+h),(0,255,0),thickness=3)
cv.imshow('Detected Faces',img8)

cv.waitKey(0)

faces_rect = haar_cascade.detectMultiScale(img9,scaleFactor=1.17,minNeighbors=0)
#show how many faces were detected
print(f'Number of faces found={len(faces_rect)}')

for (x,y,w,h) in faces_rect:
    cv.rectangle(img9, (x,y),(x+w,y+h),(0,255,0),thickness=3)
cv.imshow('Detected Faces',img9)

cv.waitKey(0)

faces_rect = haar_cascade.detectMultiScale(img10,scaleFactor=1.17,minNeighbors=0)
#show how many faces were detected
print(f'Number of faces found={len(faces_rect)}')

for (x,y,w,h) in faces_rect:
    cv.rectangle(img10, (x,y),(x+w,y+h),(0,255,0),thickness=3)
cv.imshow('Detected Faces',img10)

cv.waitKey(0)