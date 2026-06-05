import cv2

def detect_openings(thresh):

    contours, _ = cv2.findContours(
        thresh,
        cv2.RETR_TREE,
        cv2.CHAIN_APPROX_SIMPLE
    )

    openings = []

    for contour in contours:

        area = cv2.contourArea(contour)

        if 500 < area < 5000:

            x, y, w, h = cv2.boundingRect(contour)

            aspect_ratio = w / h

            openings.append({
                "x": x,
                "y": y,
                "w": w,
                "h": h,
                "aspect_ratio": round(aspect_ratio, 2)
            })

    return openings