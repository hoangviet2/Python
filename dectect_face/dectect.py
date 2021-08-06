import matplotlib.pyplot as plt
import matplotlib.image as mpimg

import cv2
import glob
images=glob.glob("*.jpg")

for image in images:
    face_casadude = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

    image = cv2.imread(image)
    gray_image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

    faces_image = face_casadude.detectMultiScale(gray_image,scaleFactor=1.1,minNeighbors=5)

    for x,y,w,h in faces_image:
        image = cv2.rectangle(image,(x,y),(x+w,y+h),(0,255,0),3)

    resize = cv2.resize(image,(int(image.shape[1]/3),int(image.shape[0]/3)))

    if len(faces_image)>1:
        print(image)
        plt.imshow(resize)
        plt.show()