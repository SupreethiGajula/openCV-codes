import cv2 as cv
import matplotlib.pyplot as plt
img = cv.imread('coffee.jpeg')
#cv.imshow('cappuccino',img)

#resizing the image

resized = cv.resize(img,(500,600),interpolation = cv.INTER_CUBIC)
cv.imshow('resizedimage',resized)

#converting to grayscale

gray = cv.cvtColor(resized,cv.COLOR_BGR2GRAY)
cv.imshow('grayimage',gray)

#converting into HSV(hue saturation value)

hsv = cv.cvtColor(resized,cv.COLOR_BGR2HSV)
cv.imshow('hsvimage',hsv)

#converting into LAB sometimes L*a*b

lab = cv.cvtColor(resized,cv.COLOR_BGR2LAB)
cv.imshow('labimage',lab)

plt.imshow(resized)
plt.show()
#the result will be varied from the actual resized image because opencv accepts and reads ion BGR formal
#where as others read in RGB format

#converting into RGB

rgb = cv.cvtColor(resized,cv.COLOR_BGR2RGB)
cv.imshow('rgbimage',rgb)

cv.waitKey(0)