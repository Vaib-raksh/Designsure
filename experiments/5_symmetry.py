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

# Get image dimensions
height, width = gray.shape

# Split image vertically
left_half = gray[:, :width // 2]
right_half = gray[:, width // 2:]

# Flip right half horizontally
right_half_flipped = cv2.flip(right_half, 1)

# Resize if dimensions mismatch
min_width = min(left_half.shape[1], right_half_flipped.shape[1])

left_half = left_half[:, :min_width]
right_half_flipped = right_half_flipped[:, :min_width]

# Calculate absolute difference
difference = cv2.absdiff(
    left_half,
    right_half_flipped
)

# Symmetry score
score = 100 - (
    np.sum(difference) /
    (difference.shape[0] * difference.shape[1] * 255)
) * 100

score = round(score, 2)

print(f"Symmetry Score: {score}%")

# Display images
titles = [
    "Original Image",
    "Left Half",
    "Flipped Right Half",
    f"Difference Map\nSymmetry Score: {score}%"
]

images = [
    image_rgb,
    left_half,
    right_half_flipped,
    difference
]

plt.figure(figsize=(14, 10))

for i in range(len(images)):

    plt.subplot(2, 2, i + 1)

    plt.imshow(images[i], cmap='gray')

    plt.title(titles[i])

    plt.axis('off')

plt.tight_layout()

plt.show()