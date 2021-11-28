import cv2

file_path = 'images/photo.jpg';

face_cascade = cv2.CascadeClassifier(
    './cascades/haarcascade_frontalface_default.xml')
eyeCascade = cv2.CascadeClassifier('Cascades/haarcascade_eye.xml')
smileCascade = cv2.CascadeClassifier('Cascades/haarcascade_smile.xml')
img = cv2.imread(file_path)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray, 1.08, 5)
for (x, y, w, h) in faces:
    img = cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)

    roi_gray = gray[y:y + h, x:x + w]
    roi_color = img[y:y + h, x:x + w]

    eyes = eyeCascade.detectMultiScale(
        roi_gray,
        scaleFactor=1.5,
        minNeighbors=5,
        minSize=(5, 5),
    )

    for (ex, ey, ew, eh) in eyes:
        cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 0, 255), 2)

    smile = smileCascade.detectMultiScale(
        roi_gray,
        scaleFactor=1.5,
        minNeighbors=15,
        minSize=(25, 25),
    )

    for (xx, yy, ww, hh) in smile:
        cv2.rectangle(roi_color, (xx, yy), (xx + ww, yy + hh), (255, 0, 0), 2)

cv2.namedWindow('Faces Detected!')
cv2.imshow('Faces Detected!', img)
cv2.imwrite('./faces_detected.jpg', img)
cv2.waitKey(0)
