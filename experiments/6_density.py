import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load image
image = cv2.imread(
    r"C:\Users\vaibh\OneDrive\Desktop\DesignSure\images\3d-bedroom-designs.jpg"
)

# Convert BGR to RGB
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Blur image
blur = cv2.GaussianBlur(gray, (5, 5), 0)

# Edge Detection
edges = cv2.Canny(blur, 50, 150)

# Count edge pixels
edge_pixels = np.sum(edges > 0)

# Total pixels
total_pixels = edges.shape[0] * edges.shape[1]

# Density percentage
density = (edge_pixels / total_pixels) * 100

density = round(density, 2)

# Risk classification
if density < 5:
    risk = "Low Risk / Very Simple Design"

elif density < 12:
    risk = "Moderate Risk / Balanced Design"

elif density < 20:
    risk = "High Complexity / Congested Design"

else:
    risk = "Very High Risk / Overcrowded Structure"

print(f"Structural Density: {density}%")
print(f"Risk Assessment: {risk}")

# Heatmap visualization
heatmap = cv2.applyColorMap(
    edges,
    cv2.COLORMAP_JET
)

heatmap = cv2.cvtColor(
    heatmap,
    cv2.COLOR_BGR2RGB
)

# Display images
titles = [
    "Original Image",
    "Edges",
    "Structural Heatmap"
]

images = [
    image_rgb,
    edges,
    heatmap
]

plt.figure(figsize=(14, 6))

for i in range(len(images)):

    plt.subplot(1, 3, i + 1)

    plt.imshow(images[i], cmap='gray')

    plt.title(titles[i])

    plt.axis('off')

plt.suptitle(
    f"Density: {density}% | {risk}",
    fontsize=14
)

plt.tight_layout()

plt.show()