import cv2 as cv
img = cv.imread('coffee.jpeg')
resized = cv.resize(img,(500,600),interpolation = cv.INTER_CUBIC)
cv.imshow('resizedimage',resized)
#cv.waitKey(0)

#average blur

avgblur = cv.blur(resized,(7,7))
cv.imshow('averageblur',avgblur)
#cv.waitKey(0)

#Gaussian blur

gblur = cv.GaussianBlur(resized,(7,7),1)
cv.imshow('Gaussianblur',gblur)

#median blur

mblur = cv.medianBlur(resized,7)
cv.imshow('medianblur',mblur)

#Bilateral blur

bblur = cv.bilateralFilter(resized,5,15,15)
cv.imshow('bilateralblur',bblur)
cv.waitKey(0)

 