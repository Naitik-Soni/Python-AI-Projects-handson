# Task: Identified edges within specified region of image

import cv2 as cv
import numpy as np

# Read the original image
image = cv.imread("Images\img3.jpg")

# Detect edges with canny edge detection algorithm
edges = cv.Canny(image[50:450, 50:450], 100, 255)

# Change ROI in image with edges
image[50:450, 50:450, 0] = edges
image[50:450, 50:450, 1] = edges
image[50:450, 50:450, 2] = edges

cv.imshow("Image", image)

cv.waitKey(0)
cv.destroyAllWindows()