import cv2 as cv
import numpy as np
img = cv.imread('sunflower.jpg')
cv.imshow('sunflower',img)
#cv.waitKey(0)

#translation

def translate(img,x,y):
    #we need a matrix to translate
    transmatrix = np.float32([[1,0,x],[0,1,y]])
    dimensions = (img.shape[1],img.shape[0])
    print(dimensions)
    return cv.warpAffine(img,transmatrix,dimensions)
#+x -->shift right
#+y -->shift up
#-x -->shift left
#-y -->shift down
translated = translate(img,100,100)
cv.imshow('translatedimage',translated)
#cv.waitKey(0)

#rotation

def rotate(img,angle,rotPoint=None):
    height,width = img.shape[:2]
    #if rotPoint is not given, it will be the center of the image
    if rotPoint == None:
        rotPoint = (width//2,height//2)
    #we need a matrix to rotate
    rotmatrix = cv.getRotationMatrix2D(rotPoint,angle,1.0)
    dimensions = (width,height)
    return cv.warpAffine(img,rotmatrix,dimensions)
rotated = rotate(img,45)
cv.imshow('rotatedimage',rotated)
#cv.waitKey(0)
# we can rotate the already rotated image too

#resizing

resized  = cv.resize(img,(500,500),interpolation = cv.INTER_CUBIC)
cv.imshow('resizedimage',resized)
#cv.waitKey(0)

#flipping

flipped = cv.flip(img,-1)
cv.imshow('flippedimage',flipped)
#cv.waitKey(0)

#cropping

cropped = resized[200:300,300:400]
cv.imshow('croppedimage',cropped)
cv.waitKey(0)
