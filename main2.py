import cv2
from skimage import io

file_path = 'images/photo.jpg';

#img = io.imread(file_path)

face_cascade = cv2.CascadeClassifier(
    './cascades/haarcascade_frontalface_default.xml')
img = cv2.imread(file_path)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray, 1.08, 5)
for (x, y, w, h) in faces:
    img = cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
cv2.namedWindow('Faces Detected!')
cv2.imshow('Faces Detected!', img)
cv2.imwrite('./faces_detected.jpg', img)
cv2.waitKey(0)
