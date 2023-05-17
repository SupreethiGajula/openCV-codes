import cv2 as cv
imge = cv.imread("C:/Users/gajul/OneDrive/Desktop/MLCOURSE/sunflower.jpg")
img = cv.cvtColor(imge, cv.COLOR_BGR2GRAY)
cv.imshow("sunflower", imge)
cv.waitKey(0) 