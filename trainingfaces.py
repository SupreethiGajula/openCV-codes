import os
import cv2 as cv
import cv2
import numpy as np
#from cv2 import cv2.face
celebs = ['dualipa','weeknd','mileycyrus','madonna','tomholland']
DIR = r'C:\Users\gajul\OneDrive\Desktop\MLprojects\opencv\celebs'

#this will list all the files present in the specified path shown
#not so important for now
p = []
for i in os.listdir(r'C:\Users\gajul\OneDrive\Desktop\MLprojects\opencv\celebs'):
    p.append(i)
print(p)
#end for that

haar_cascade = cv.CascadeClassifier('haarcascade.xml')
features = []
labels = []

def create_train():
    for person in celebs:
        #DIR and person are variables representing two parts of a file path. 
        #By using os.path.join(DIR, person), the code concatenates these two parts and returns the complete path as a string, 
        # which is then assigned to the variable path
        path = os.path.join(DIR,person)
        label = celebs.index(person)

        for img in os.listdir(path):                 #we are trying to iterate through all the images one by one
            img_path = os.path.join(path,img)
            img_array = cv.imread(img_path)           #we are reading all the images one by one with specified path
            gray = cv.cvtColor(img_array,cv.COLOR_BGR2GRAY)
            #The detectMultiScale() function returns a list of rectangles, where
#  each rectangle represents a detected object or region of interest (ROI) in the image. 
# Each rectangle contains the coordinates of the top-left corner, width, and height of the detected object.
            faces_rect = haar_cascade.detectMultiScale(gray,scaleFactor = 1.1,minNeighbors = 4)

            for (x,y,w,h) in faces_rect:
                faces_roi = gray[y:y+h,x:x+h]
                features.append(faces_roi)
                labels.append(label)
create_train()
print('-------------------------training done----------------------------\n')

print('length of the features = ',len(features))
print('length of the labels = ',len(labels))

#we are converting the features and labels into numpy arrays
features = np.array(features,dtype = 'object')
labels = np.array(labels)

#now we shall build a face recognizer and train it with our features and labels

face_recognizer = cv.face.LBPHFaceRecognizer.create()#we created a face recognizer

face_recognizer.train(features,labels)#we are training it with features and labels
face_recognizer.save('faces_trained.yml')

np.save('features.npy',features)
np.save('labels.npy',labels)

