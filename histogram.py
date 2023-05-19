import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np
img = cv.imread('sunflower.jpg')
cv.imshow('sunflower',img)

blank = np.zeros(img.shape[:2],dtype = 'uint8')
cv.imshow('blank image',blank)

#we can plot a histogram for grayscale image and RGB image
#a histogram shows the distribution of pixels in an image
#histogram for grayscale image

gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('grayimage',gray)

#we want it for only one image-gray,there is only single color channel gray so [0],[256]=number of bins,as there is no mask = None
grayhist = cv.calcHist([gray],[0],None,[256],[0,256])
plt.plot(grayhist)

#we can try plotting the histogram after addition of a mask

crcle = cv.circle(blank.copy(),(img.shape[1]//2,img.shape[0]//2),100,255,-1)
cv.imshow('circle',crcle)

mask = cv.bitwise_and(gray,gray,mask = crcle)
cv.imshow('mask',mask)

grayhist1 = cv.calcHist([gray],[0],mask,[256],[0,256])


plt.figure()
plt.title('gray histogram')
plt.xlabel('number of bins')
plt.ylabel('number of pixels')
plt.xlim(256)
plt.plot(grayhist1)
plt.show()
cv.waitKey(0)