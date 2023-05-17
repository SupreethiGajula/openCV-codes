import cv2 as cv
import numpy as np
img = cv.imread('sunflower.jpg')
cv.imshow('sunflower', img)

#converting into grayscale

gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)

#detecting the edges in the image

canny = cv.Canny(img,125,175)
cv.imshow('canny', canny)   

#detecting contours

contours,hierarchies = cv.findContours(canny,cv.RETR_LIST,cv.CHAIN_APPROX_SIMPLE)
#number of contours is a list
#so we can find the number of contours using the len()
print(len(contours))

#Thresholding
#i.e.,if any pixels are below the threshold value,in our case it is 125,then it will set those pixels
#to the minimum threshold value

ret,thresh = cv.threshold(gray,125,225,cv.THRESH_BINARY)
cv.imshow('thresholded', thresh)

#blur the image
blur = cv.blur(img,(5,5),cv.BORDER_DEFAULT)
cv.imshow('blurred',blur)

#if we detect the edges again

canny = cv.Canny(blur,125,175)
cv.imshow('canny1', canny)

#if we call in the contours again
contours,hierarchies = cv.findContours(canny,cv.RETR_LIST,cv.CHAIN_APPROX_SIMPLE)
print(len(contours))
#we observe the number of contours will be reduced a lot

#we shall draw the contours on an blank image with dimensions = our img dimensions
#we shall color the contours red
blank = np.zeros(img.shape,dtype = 'uint8')
cv.imshow('blankimage',blank)

cv.drawContours(blank,contours,-1,(0,0,255),2)
cv.imshow('contoursonblankimage',blank)

cv.waitKey(0)