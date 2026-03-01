from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

def generate_report(file_path, name, email, skills, experience):
    doc = SimpleDocTemplate(file_path)
    elements = []

    styles = getSampleStyleSheet()

    elements.append(Paragraph(f"Name: {name}", styles["Normal"]))
    elements.append(Paragraph(f"Email: {email}", styles["Normal"]))
    elements.append(Spacer(1, 12))
    elements.append(Paragraph(f"Skills: {skills}", styles["Normal"]))
    elements.append(Spacer(1, 12))
    elements.append(Paragraph(f"Experience: {experience}", styles["Normal"]))

    doc.build(elements)