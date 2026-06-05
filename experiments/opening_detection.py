import cv2
import matplotlib.pyplot as plt

from modules.opening_detection import detect_openings

image = cv2.imread("images/floorplan.png")

image_rgb = cv2.cvtColor(
    image,
    cv2.COLOR_BGR2RGB
)

gray = cv2.cvtColor(
    image,
    cv2.COLOR_BGR2GRAY
)

_, thresh = cv2.threshold(
    gray,
    200,
    255,
    cv2.THRESH_BINARY_INV
)

openings = detect_openings(thresh)

output = image_rgb.copy()

for opening in openings:

    x = opening["x"]
    y = opening["y"]
    w = opening["w"]
    h = opening["h"]

    cv2.rectangle(
        output,
        (x, y),
        (x+w, y+h),
        (255, 0, 0),
        2
    )

print("Detected Openings:", len(openings))

plt.imshow(output)
plt.axis("off")
plt.show()