import cv2

#importing cascade calssifier
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

#importing image
image = cv2.imread('images.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#detecting faecs
face = face_cascade.detectMultiScale(gray,
                                     scaleFactor=1.2,
                                     minNeighbors=5,
                                     minSize=(30, 30),
                                     flags =cv2.CASCADE_SCALE_IMAGE
                                     )

# Draw a rectangle around the faces
for (x, y, w, h) in face:
    cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
    
    cv2.imshow("Faces found", image)
    copy = cv2.imshow("Faces found", image)
cv2.waitKey(0)
cv2.destroyAllWindows()