import cv2 as cv
import numpy as np
#we can use an existing image or a blank image
#creating a blank image
#(500,500,3) specifies the dimensions of the image and 3 specifies the number of color channels
#uint8 is the datatype for an image
blank = np.zeros((500,500,3),dtype = 'uint8')
cv.imshow('blankimage',blank)
#colouring the blank image
#for all the pixels
blank[:] = 255,0,0#specifies red colour
cv.imshow('blankblueimage',blank)
#if you want to colour only some of the pixels
blank[200:300,400:500] = 0,255,255
cv.imshow('somepixelscolored',blank)
#draw a rectangle
#the rectangle is specified by the top left corner and bottom right corner
cv.rectangle(blank,(0,0),(250,250),(0,255,0),thickness = 5)
#if you want the rectangle to be filled,use thickness = -1
#you can do something like blank.shape[1]//2 and blank.shape[0]//2 so that you will get the width and height exactly halved i.e.,you get a square
cv.imshow('rectangle',blank)
#draw a circle
cv.circle(blank,(250,250),100,(255,255,255),thickness = 6)
cv.imshow('circle',blank)
#very similarly we can draw a line
cv.line(blank,(0,0),(250,250),(0,255,0),thickness = 6)
cv.imshow('line',blank)
#write a text
cv.putText(blank,'Hello',(400,400),cv.FONT_ITALIC,1,(255,255,255),thickness = 3,lineType = cv.INTER_CUBIC)
cv.imshow('text',blank)
cv.waitKey(0)

