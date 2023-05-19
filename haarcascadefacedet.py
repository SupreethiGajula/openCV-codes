import cv2 as cv
man = cv.imread('4people.jpeg')
cv.imshow('9 persons',man)
#grayscale
gray = cv.cvtColor(man,cv.COLOR_BGR2GRAY)
cv.imshow('gray',gray)

haar_cascade = cv.CascadeClassifier('haarcascade.xml')
#detect faces
#here faces is a list
#so when we detect multiple faces in a single image, we sometimes get an output as more faces than expected or less faces than expected
#so this haarcascades is very sensitive to noise . one way to manage this is to try altering the scale factor and min neighbors
faces = haar_cascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=8)
print('number of faces found:',len(faces))

#we shall now draw a rectangle around the found faces

for (x,y,w,h) in faces:
    cv.rectangle(man,(x,y),(x+h,y+w),(0,255,0),thickness=2)
cv.imshow('detectedfaces',man)
cv.waitKey(0)