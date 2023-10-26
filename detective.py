import cv2
import numpy as np

# Load the image
img = cv2.imread('image/basketball.png')

# Convert the image to HSV color space
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# Define the range of blue color in HSV
lower_blue = np.array([110,50,50])
upper_blue = np.array([130,255,255])

# Threshold the image to get only blue colors
mask = cv2.inRange(hsv, lower_blue, upper_blue)

# Show the original image and the mask
cv2.imshow('Original Image', img)
cv2.imshow('Mask', mask)

# Wait for a key press and then close all windows
cv2.waitKey(0)
cv2.destroyAllWindows()