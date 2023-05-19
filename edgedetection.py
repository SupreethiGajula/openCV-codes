import cv2 as cv
import numpy as np
img = cv.imread('sunflower.jpg')
cv.imshow('sunflower',img)

#grayscale

gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('gray',gray)

#apart from canny and contours,there are other two methods of edge detection
#laplacian and sobel

#laplacian

lap = cv.Laplacian(gray,cv.CV_64F)
lap = np.uint8(np.absolute(lap))#if we do this step it essentially appears as an pencil smudged image
cv.imshow('lap',lap)#if we don't use previous step and we directly go for this step then,it detects sharp edges

#sobel
sobelx = cv.Sobel(gray,cv.CV_64F,1,0)
sx = np.uint8(np.absolute(sobelx))
sobely = cv.Sobel(gray,cv.CV_64F,0,1)
sy = np.uint8(np.absolute(sobely))
cv.imshow('sobelx',sobelx)
cv.imshow('sobely',sobely)
cv.imshow('sx',sx)
cv.imshow('sy',sy)
#we can merge the both sobels
sobel_merged = cv.bitwise_or(sobelx,sobely)
cv.imshow('sobel_merged',sobel_merged)

cv.waitKey(0)