import cv2
import numpy as np
import matplotlib.pyplot as plt
import os

image = cv2.imread("images/Minimalist Headphone Stand.jpg")
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

#convert to grayscale 
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#Edge detection 
edges = cv2.Canny(gray, 50 ,150)

#thresholding
ret, thresh = cv2.threshold(gray,127,255,cv2.THRESH_BINARY)

#Find contours
contours, hierarchy = cv2.findContours(
    thresh,
    cv2.RETR_EXTERNAL, 
    cv2.CHAIN_APPROX_SIMPLE)

#Copy image for drawing 
contour_image = image_rgb.copy()

#loop through contours
for contour in contours:
    area = cv2.contourArea(contour)

    #ignore tiny areas - area filtering concept
    if area > 500:
        x,y,w,h = cv2.boundingRect(contour)
        #bounding box
        cv2.rectangle(
            contour_image,
            (x,y),
            (x+w,y+h),
            (0,255,0),
            2
        )

# Display images
titles = [
    "Original",
    "Threshold",
    "Room Detection"
]

images = [
    image_rgb,
    thresh,
    contour_image
]

plt.figure(figsize=(12, 6))

for i in range(3):
    plt.subplot(1, 3, i + 1)
    plt.imshow(images[i], cmap='gray')
    plt.title(titles[i])
    plt.axis('off')

plt.tight_layout()
plt.show()
