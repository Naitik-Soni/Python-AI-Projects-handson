# Task: Generate the image which is blur except the some rectangular portion of that image

import cv2 as cv

# Read the original image
image = cv.imread("Images\img3.jpg")

new_image = image.copy()

# Apply blur effect to the image
size = 51
blur = cv.blur(image, (size, size))

cv.imshow("Original", image)

# Apply blur to specific portion of image
blur[50:450, 50:450] = new_image[50:450, 50:450]

cv.imshow("Blured", blur)

cv.waitKey(0)
cv.destroyAllWindows()