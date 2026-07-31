from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet


def generate_report(filepath, analysis):
    doc = SimpleDocTemplate(filepath)
    styles = getSampleStyleSheet()
    story = []

    story.append(Paragraph("<b>AI Resume Analysis Report</b>", styles["Title"]))
    story.append(Paragraph("<br/>", styles["Normal"]))

    story.append(Paragraph(f"<b>ATS Score:</b> {analysis['ats_score']}/100", styles["Heading2"]))
    story.append(Paragraph("<br/>", styles["Normal"]))

    story.append(Paragraph("<b>AI Summary</b>", styles["Heading2"]))
    story.append(Paragraph(analysis["summary"], styles["BodyText"]))
    story.append(Paragraph("<br/>", styles["Normal"]))

    story.append(Paragraph("<b>Technical Skills</b>", styles["Heading2"]))
    for skill in analysis["technical_skills"]:
        story.append(Paragraph("• " + skill, styles["BodyText"]))

    story.append(Paragraph("<br/>", styles["Normal"]))

    story.append(Paragraph("<b>Soft Skills</b>", styles["Heading2"]))
    for skill in analysis["soft_skills"]:
        story.append(Paragraph("• " + skill, styles["BodyText"]))

    story.append(Paragraph("<br/>", styles["Normal"]))

    story.append(Paragraph("<b>Missing Skills</b>", styles["Heading2"]))
    for skill in analysis["missing_skills"]:
        story.append(Paragraph("• " + skill, styles["BodyText"]))

    story.append(Paragraph("<br/>", styles["Normal"]))

    story.append(Paragraph("<b>AI Suggestions</b>", styles["Heading2"]))
    for suggestion in analysis["suggestions"]:
        story.append(Paragraph("• " + suggestion, styles["BodyText"]))

    doc.build(story)