def blueprint_score(
    room_count,
    average_area
):

    score = 100

    if room_count < 3:
        score -= 20

    elif room_count > 12:
        score -= 10

    if average_area < 10000:
        score -= 15

    elif average_area > 50000:
        score += 5

    score = max(0, min(score, 100))

    return score