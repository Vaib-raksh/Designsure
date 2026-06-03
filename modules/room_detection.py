import cv2

def detect_rooms(thresh):

    contours, _ = cv2.findContours(
        thresh,
        cv2.RETR_TREE,
        cv2.CHAIN_APPROX_SIMPLE
    )

    rooms = []

    for contour in contours:

        area = cv2.contourArea(contour)

        if 5000 < area < 150000:

            x, y, w, h = cv2.boundingRect(contour)

            rooms.append({
                "x": x,
                "y": y,
                "w": w,
                "h": h,
                "area": area
            })

    return rooms