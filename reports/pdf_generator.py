from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)

from reportlab.lib.styles import getSampleStyleSheet


def generate_pdf(
    filename,
    analysis_id,
    risk_score,
    threat_level,
    explanation,
    recommendations
):

    doc = SimpleDocTemplate(filename)

    styles = getSampleStyleSheet()

    content = []

    content.append(
        Paragraph(
            "PhishShield AI Analysis Report",
            styles["Title"]
        )
    )

    content.append(Spacer(1, 20))

    content.append(
        Paragraph(
            f"<b>Analysis ID:</b> {analysis_id}",
            styles["BodyText"]
        )
    )

    content.append(
        Paragraph(
            f"<b>Risk Score:</b> {risk_score}",
            styles["BodyText"]
        )
    )

    content.append(
        Paragraph(
            f"<b>Threat Level:</b> {threat_level}",
            styles["BodyText"]
        )
    )

    content.append(Spacer(1, 12))

    content.append(
        Paragraph(
            "<b>Explanation</b>",
            styles["Heading2"]
        )
    )

    content.append(
        Paragraph(
            explanation,
            styles["BodyText"]
        )
    )

    content.append(Spacer(1, 12))

    content.append(
        Paragraph(
            "<b>Recommendations</b>",
            styles["Heading2"]
        )
    )

    content.append(
        Paragraph(
            recommendations,
            styles["BodyText"]
        )
    )

    doc.build(content)