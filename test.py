from keras.models import load_model
from time import sleep
from keras.preprocessing.image import img_to_array
from keras.preprocessing import image
import cv2
import numpy as np
import time
import youtube_stream

face_classifier = cv2.CascadeClassifier('src/haarcascade_frontalface_default.xml')
classifier =load_model('src/model.h5')

class_labels = ['Angry','Happy','Neutral','Sad','Surprise']
label_dict = {'Angry':0, 'Happy':0, 'Neutral':0, 'Sad':0, 'Surprise':0}

cap = cv2.VideoCapture(0)
end = time.time() + 15
while True:
    # Grab a single frame of video
    ret, frame = cap.read()
    labels = []
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces = face_classifier.detectMultiScale(gray,1.3,5)

    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h,x:x+w]
        roi_gray = cv2.resize(roi_gray,(48,48),interpolation=cv2.INTER_AREA)
    # rect,face,image = face_detector(frame)


        if np.sum([roi_gray])!=0:
            roi = roi_gray.astype('float')/255.0
            roi = img_to_array(roi)
            roi = np.expand_dims(roi,axis=0)

        # make a prediction on the ROI, then lookup the class

            preds = classifier.predict(roi)[0]
            label=class_labels[preds.argmax()]
            # print(label)
            label_dict[label] += 1
            label_position = (x,y)
            cv2.putText(frame,label,label_position,cv2.FONT_HERSHEY_SIMPLEX,2,(0,255,0),3)
        else:
            cv2.putText(frame,'No Face Found',(20,60),cv2.FONT_HERSHEY_SIMPLEX,2,(0,255,0),3)
    cv2.imshow('Emotion Detector',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        label = max(label_dict, key=label_dict.get)
        print(label)
        break
    if time.time() > end:
        label = max(label_dict, key=label_dict.get)
        print(label)
        break

label += " songs"

youtube_stream.play_video(label)

cap.release()
cv2.destroyAllWindows()