import cv2
import numpy as np

# Load the image
img = cv2.imread('image/basketball.png')

# Convert the image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Threshold the image to get a binary image
ret, thresh = cv2.threshold(gray, 127, 255, 0)

# Find contours in the binary image
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# Draw all contours on the original image
cv2.drawContours(img, contours, -1, (0, 255, 0), 3)

# Show the original image with the contours
cv2.imshow('Image with Contours', img)

# Wait for a key press and then close all windows
cv2.waitKey(0)
cv2.destroyAllWindows()