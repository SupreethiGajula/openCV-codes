import cv2 as cv
img = cv.imread('4people.jpeg')
cv.imshow('9 persons',img)
#grayscale
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('gray',gray)

haar_cascade = cv.CascadeClassifier('haarcascade.xml')
#detect faces
#here faces is a list
#so when we detect multiple faces in a single image, we sometimes get an output as more faces than expected or less faces than expected
#so this haarcascades is very sensitive to noise . one way to manage this is to try altering the scale factor and min neighbors
#The detectMultiScale() function returns a list of rectangles, where
#  each rectangle represents a detected object or region of interest (ROI) in the image. 
# Each rectangle contains the coordinates of the top-left corner, width, and height of the detected object.
faces = haar_cascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=8)
print('number of faces found:',len(faces))

#we shall now draw a rectangle around the found faces

for (x,y,w,h) in faces:
    cv.rectangle(img,(x,y),(x+h,y+w),(0,255,0),thickness=2)
cv.imshow('detectedfaces',img)
cv.waitKey(0)