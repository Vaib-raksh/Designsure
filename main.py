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

# -----------------------------------
# SYMMETRY ANALYSIS
# -----------------------------------

height, width = gray.shape

left_half = gray[:, :width // 2]
right_half = gray[:, width // 2:]

# Flip right side
right_half_flipped = cv2.flip(right_half, 1)

# Resize for safety
min_width = min(
    left_half.shape[1],
    right_half_flipped.shape[1]
)

left_half = left_half[:, :min_width]
right_half_flipped = right_half_flipped[:, :min_width]

# Difference map
difference = cv2.absdiff(
    left_half,
    right_half_flipped
)

# Symmetry Score
symmetry_score = 100 - (
    np.sum(difference) /
    (
        difference.shape[0] *
        difference.shape[1] *
        255
    )
) * 100

symmetry_score = round(symmetry_score, 2)

# -----------------------------------
# STRUCTURAL DENSITY ANALYSIS
# -----------------------------------

blur = cv2.GaussianBlur(gray, (5, 5), 0)

edges = cv2.Canny(blur, 50, 150)

edge_pixels = np.sum(edges > 0)

total_pixels = edges.shape[0] * edges.shape[1]

density_score = (
    edge_pixels / total_pixels
) * 100

density_score = round(density_score, 2)

# -----------------------------------
# EFFECTIVENESS SCORE
# -----------------------------------

# Weighted scoring
effectiveness_score = (
    (symmetry_score * 0.7)
    +
    ((100 - density_score) * 0.3)
)

effectiveness_score = round(effectiveness_score, 2)

# -----------------------------------
# RISK CLASSIFICATION
# -----------------------------------

if effectiveness_score >= 85:
    risk = "Excellent Design"

elif effectiveness_score >= 70:
    risk = "Good Design"

elif effectiveness_score >= 55:
    risk = "Moderate Design"

else:
    risk = "High Risk / Inefficient Design"

# -----------------------------------
# PRINT RESULTS
# -----------------------------------

print(f"Symmetry Score: {symmetry_score}%")

print(f"Structural Density: {density_score}%")

print(
    f"Design Effectiveness Score: "
    f"{effectiveness_score}/100"
)

print(f"Assessment: {risk}")

# -----------------------------------
# HEATMAP
# -----------------------------------

heatmap = cv2.applyColorMap(
    edges,
    cv2.COLORMAP_JET
)

heatmap = cv2.cvtColor(
    heatmap,
    cv2.COLOR_BGR2RGB
)

# -----------------------------------
# DISPLAY RESULTS
# -----------------------------------

titles = [
    "Original",
    "Difference Map",
    "Structural Heatmap"
]

images = [
    image_rgb,
    difference,
    heatmap
]

plt.figure(figsize=(14, 6))

for i in range(len(images)):

    plt.subplot(1, 3, i + 1)

    plt.imshow(images[i], cmap='gray')

    plt.title(titles[i])

    plt.axis('off')

plt.suptitle(
    f"Effectiveness Score: "
    f"{effectiveness_score}/100\n"
    f"{risk}",
    fontsize=14
)

plt.tight_layout()

plt.show()
