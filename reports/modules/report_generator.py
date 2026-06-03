import os
from datetime import datetime

def generate_report(
    image_name,
    effectiveness_score,
    assessment,
    recommendations,
    risk_scores
):

    os.makedirs("reports", exist_ok=True)

    filename = f"reports/{image_name}_report.txt"

    with open(filename, "w") as file:

        file.write("DESIGNSURE ANALYSIS REPORT\n")
        file.write("=" * 40 + "\n\n")

        file.write(f"Image: {image_name}\n")
        file.write(f"Generated: {datetime.now()}\n\n")

        file.write(
            f"Effectiveness Score: {effectiveness_score}/100\n"
        )

        file.write(
            f"Assessment: {assessment}\n\n"
        )

        file.write("Risk Zones:\n")

        for region, score in risk_scores.items():
            file.write(
                f"{region}: {score}%\n"
            )

        file.write("\nRecommendations:\n")

        for rec in recommendations:
            file.write(f"- {rec}\n")

    print(f"\nReport saved to {filename}")