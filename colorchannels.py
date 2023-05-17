import cv2 as cv
import numpy as np
img = cv.imread('coffee.jpeg')
#cv.imshow('cappuccino',img)

resized = cv.resize(img,(500,600),interpolation = cv.INTER_CUBIC)
cv.imshow('resizedimage',resized)

#splitting the individual colors from the image

b,g,r = cv.split(resized)
cv.imshow('blue',b)
cv.imshow('green',g)
cv.imshow('red',r)

#merging the colors back

merged = cv.merge([b,g,r])
cv.imshow('merged',merged)

#if you want the view with actual colors

blank = np.zeros(resized.shape[:2],dtype = 'uint8')

blue = cv.merge([b,blank,blank])
green = cv.merge([blank,g,blank])
red = cv.merge([blank,blank,r])
cv.imshow('blues',blue)
cv.imshow('greens',green)
cv.imshow('reds',red)

cv.waitKey(0)