# Task: Blur the faces of individuals in an image while keeping the rest of the scene unaffected.

import cv2 as cv
import numpy as np

# Read image
image = cv.imread("Images\Img8.jpg")

gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    
# Create haar-cascade object
haar_cascade = cv.CascadeClassifier("haarcascade_frontalface_default.xml")

# Detect faces using haar-cascade
faces = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

print(len(faces))

# Blur faces in haar-cascade
for (x,y,w,h) in faces:
    blur = cv.blur(image[y:y+w, x:x+h], (15,15))
    image[y:y+w, x:x+h] = blur


cv.imshow("Image", image)

cv.waitKey(0)
cv.destroyAllWindows()
