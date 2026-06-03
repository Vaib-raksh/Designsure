def compare_designs(
    design1_name,
    design1_score,
    design2_name,
    design2_score
):

    print("\n========== COMPARISON ==========\n")

    print(
        f"{design1_name}: "
        f"{design1_score}"
    )

    print(
        f"{design2_name}: "
        f"{design2_score}"
    )

    if design1_score > design2_score:

        winner = design1_name

    elif design2_score > design1_score:

        winner = design2_name

    else:

        winner = "Tie"

    print(f"\nWinner: {winner}")

    return winner
