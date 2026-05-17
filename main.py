import cv2
import numpy as np
import matplotlib.pyplot as plt
import os

image = cv2.imread("images/Minimalist Headphone Stand.jpg")

#convert to grayscale 
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#Edge detection 
edges = cv2.Canny(gray, 50 ,150)

#thresholding
ret, thresh = cv2.threshold(gray,127,255,cv2.THRESH_BINARY)

#display the images 
images = [ image, gray, edges, thresh]
titles = ['Original', 'Grayscale', 'Edges', 'Threshold']
for i in range(4):
    plt.subplot(2,2,i+1)
    plt.imshow(images[i], cmap ='gray')
    plt.title(titles[i])
    plt.axis('off')
plt.tight_layout()
plt.show()    