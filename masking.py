import cv2 as cv
import numpy as np
img = cv.imread('sunflower.jpg')
cv.imshow('sunflower',img)

blank = np.zeros(img.shape[:2],dtype = 'uint8')
cv.imshow('blank image',blank)

mask = cv.circle(blank.copy(),(img.shape[1]//2,img.shape[0]//2),100,255,-1)
cv.imshow('mask',mask)

mask1 = cv.rectangle(blank.copy(),(40,40),(250,250),255,-1)
cv.imshow('mask1',mask1)

masked = cv.bitwise_and(img,img,mask = mask)
cv.imshow('masked image',masked)

masked1 = cv.bitwise_and(img,img,mask = mask1)
cv.imshow('masked image1',masked1)
cv.waitKey(0)

#try it without using blank.copy() 