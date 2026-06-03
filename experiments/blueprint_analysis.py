import cv2
import matplotlib.pyplot as plt

from modules.room_detection import detect_rooms
from modules.room_metrics import calculate_room_metrics
from modules.blueprint_scoring import blueprint_score

# Load floorplan image

image = cv2.imread(
    "images/floorplan.png"
)

image_rgb = cv2.cvtColor(
    image,
    cv2.COLOR_BGR2RGB
)

gray = cv2.cvtColor(
    image,
    cv2.COLOR_BGR2GRAY
)

# Threshold

_, thresh = cv2.threshold(
    gray,
    200,
    255,
    cv2.THRESH_BINARY_INV
)

# Detect rooms

rooms = detect_rooms(thresh)

# Calculate metrics

metrics = calculate_room_metrics(rooms)

room_count = metrics["room_count"]

average_area = metrics["average_area"]

# Blueprint score

score = blueprint_score(
    room_count,
    average_area
)

# Draw rooms

output = image_rgb.copy()

for room in rooms:

    x = room["x"]
    y = room["y"]
    w = room["w"]
    h = room["h"]

    cv2.rectangle(
        output,
        (x, y),
        (x + w, y + h),
        (0, 255, 0),
        3
    )

# Report

print("\n===== BLUEPRINT REPORT =====\n")

print(
    f"Rooms Detected: {room_count}"
)

print(
    f"Average Room Area: {average_area}"
)

print(
    f"Blueprint Score: {score}/100"
)

# Display

titles = [
    "Original Blueprint",
    "Threshold",
    "Detected Rooms"
]

images = [
    image_rgb,
    thresh,
    output
]

plt.figure(figsize=(15, 5))

for i in range(len(images)):

    plt.subplot(
        1,
        3,
        i + 1
    )

    plt.imshow(
        images[i],
        cmap="gray"
    )

    plt.title(
        titles[i]
    )

    plt.axis("off")

plt.tight_layout()

plt.show()