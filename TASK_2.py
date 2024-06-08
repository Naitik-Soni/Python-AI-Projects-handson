# Task: Generate the image which is blur except the some Circular portion of that image

import cv2 as cv
import numpy as np

# Read the original image
image = cv.imread("Images\img3.jpg")
new_image = image.copy()

black = np.zeros(image.shape[:3], dtype="uint8")

center = (250, 250)
radius = 200

cv.circle(black, center, radius, (255,255,255), -1)

# Apply blur effect to the image
size = 51
blurred = cv.blur(image, (size, size))


# Apply blur to specific portion of image using bitwise operators
middle_blur = cv.bitwise_and(blurred, cv.bitwise_not(black))
toast = cv.bitwise_and(black, new_image)

generated = cv.bitwise_or(toast, middle_blur)


cv.imshow("Black", blurred)
cv.imshow("Generated", generated)

cv.waitKey(0)
cv.destroyAllWindows()