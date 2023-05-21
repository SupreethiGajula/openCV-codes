import cv2 as cv
import numpy as np

haar_cascade = cv.CascadeClassifier('haarcascade.xml')

celebs = ['dualipa','weeknd','mileycyrus','madonna','tomholland']

#features = np.load('features.npy',allow_pickle=True)
#labels = np.load('labels.npy')

#we hace created an LBPHface recognizer
face_recognizer = face_recognizer = cv.face.LBPHFaceRecognizer.create()
face_recognizer.read('faces_trained.yml')#we are training it with the file with the yml file from the 'trainingfaces.py' program

person = cv.imread(r'C:\Users\gajul\OneDrive\Desktop\MLprojects\opencv\celebs\tomholland\4.jpeg')
#grayscale
gray = cv.cvtColor(person,cv.COLOR_BGR2GRAY)
cv.imshow('duagray',gray)

faces_rect = haar_cascade.detectMultiScale(gray,1.1,8)

for(x,y,w,h) in faces_rect:
    faces_roi = gray[y:y+h,x:x+w]

    label,confidence = face_recognizer.predict(faces_roi)
    print(f'celebrity name  is {celebs[label]} and the confidence is {confidence}')
    cv.putText(person,str(celebs[label]),(50,50),cv.FONT_HERSHEY_COMPLEX,1.0,(255,0,0),thickness = 2,)
    cv.rectangle(person,(x,y),(x+w,y+h),(0,255,0),2)
cv.imshow('detectedface',person)
cv.waitKey(0)