# Task: Video in person should not reveal his identity so blur his face

import cv2 as cv

# Read video
capture = cv.VideoCapture(0)

# Define the haar-cascade object
haar_cascade = cv.CascadeClassifier("haarcascade_frontalface_default.xml")

color = (255, 255, 0)
opacity = 0.4

def rescaleFrame(frame, res=0.3):
    width = int(frame.shape[1]*res)
    height = int(frame.shape[0]*res)

    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

# Display the video with blur faces
while True:
    rec, image = capture.read()
    # Uncomment below line if video resolution is high/low
    image = rescaleFrame(image, res=1.5)
    overlay = image.copy()

    if image is None:
        break

    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

    # Detect faces in current frame of video
    faces = haar_cascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=15)

    # Blur the faces in current frame of video
    for (x,y,w,h) in faces:
        # print(x,y,w,h)
        blur = cv.blur(image[y:y+w, x:x+h], (21,21))
        overlay[y:y+w, x:x+h] = blur
     
        cv.rectangle(overlay, (x, y), (x+w, y+h), color, -1)

        image = cv.addWeighted(overlay, opacity, image, 1-opacity, 0)

        cv.rectangle(image, (x, y), (x+w, y+h), color, 1)

    cv.imshow("Frame", image)

    if cv.waitKey(2) & 0xFF == ord("q"):
        break

capture.release()

cv.destroyAllWindows()

cv.waitKey(0)