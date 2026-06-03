def calculate_room_metrics(rooms):

    room_count = len(rooms)

    total_area = 0

    for room in rooms:
        total_area += room["area"]

    average_area = (
        total_area / room_count
        if room_count > 0
        else 0
    )

    return {
        "room_count": room_count,
        "average_area": round(average_area, 2)
    }