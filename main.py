import cv2
import numpy as np
import matplotlib.pyplot as plt
from reports.modules.report_generator import generate_report


# Load image
image = cv2.imread(
    r"C:\Users\vaibh\OneDrive\Desktop\DesignSure\images\floor plan image.png"
)

image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Blur
blur = cv2.GaussianBlur(gray, (5, 5), 0)

# Edge Detection
edges = cv2.Canny(blur, 50, 150)

# -------------------------------------------------
# QUADRANT SPLITTING
# -------------------------------------------------

height, width = edges.shape

mid_h = height // 2
mid_w = width // 2

quadrants = {
    "Top Left": edges[0:mid_h, 0:mid_w],
    "Top Right": edges[0:mid_h, mid_w:width],
    "Bottom Left": edges[mid_h:height, 0:mid_w],
    "Bottom Right": edges[mid_h:height, mid_w:width]
}

# -------------------------------------------------
# RISK ANALYSIS
# -------------------------------------------------

risk_scores = {}

for name, region in quadrants.items():

    edge_pixels = np.sum(region > 0)

    total_pixels = region.shape[0] * region.shape[1]

    density = (edge_pixels / total_pixels) * 100

    risk_scores[name] = round(density, 2)

# -------------------------------------------------
# RECOMMENDATIONS
# -------------------------------------------------

recommendations = []

for region, score in risk_scores.items():

    if score > 15:

        recommendations.append(
            f"{region}: High structural complexity detected. Consider reducing clutter."
        )

    elif score > 8:

        recommendations.append(
            f"{region}: Moderate complexity. Review spacing and organization."
        )

    else:

        recommendations.append(
            f"{region}: Structure appears balanced."
        )

# -------------------------------------------------
# HEATMAP GENERATION
# -------------------------------------------------

heatmap = np.zeros((height, width), dtype=np.uint8)

for region, score in risk_scores.items():

    intensity = min(int(score * 10), 255)

    if region == "Top Left":
        heatmap[0:mid_h, 0:mid_w] = intensity

    elif region == "Top Right":
        heatmap[0:mid_h, mid_w:width] = intensity

    elif region == "Bottom Left":
        heatmap[mid_h:height, 0:mid_w] = intensity

    elif region == "Bottom Right":
        heatmap[mid_h:height, mid_w:width] = intensity

heatmap_color = cv2.applyColorMap(
    heatmap,
    cv2.COLORMAP_JET
)

heatmap_color = cv2.cvtColor(
    heatmap_color,
    cv2.COLOR_BGR2RGB
)

# -------------------------------------------------
# OVERALL SCORE
# -------------------------------------------------

average_risk = np.mean(list(risk_scores.values()))

effectiveness_score = round(
    100 - average_risk * 3,
    2
)

if effectiveness_score > 85:
    assessment = "Excellent Design"

elif effectiveness_score > 70:
    assessment = "Good Design"

elif effectiveness_score > 55:
    assessment = "Moderate Design"

else:
    assessment = "High Risk Design"

# -------------------------------------------------
# REPORT
# -------------------------------------------------

print("\n========== DESIGNSURE REPORT ==========\n")

for region, score in risk_scores.items():
    print(f"{region}: {score}%")

print("\nEffectiveness Score:", effectiveness_score)
print("Assessment:", assessment)

print("\nRecommendations:\n")

for rec in recommendations:
    print("-", rec)

# -------------------------------------------------
# DISPLAY
# -------------------------------------------------

titles = [
    "Original Design",
    "Edge Detection",
    "Risk Heatmap"
]

images = [
    image_rgb,
    edges,
    heatmap_color
]

plt.figure(figsize=(15, 5))

for i in range(len(images)):

    plt.subplot(1, 3, i + 1)

    plt.imshow(images[i], cmap='gray')

    plt.title(titles[i])

    plt.axis("off")

plt.suptitle(
    f"DesignSure Analysis\nScore: {effectiveness_score} | {assessment}",
    fontsize=14
)
generate_report(
    image_name="3d-bedroom-designs",
    effectiveness_score=effectiveness_score,
    assessment=assessment,
    recommendations=recommendations,
    risk_scores=risk_scores
)

plt.tight_layout()

plt.show()