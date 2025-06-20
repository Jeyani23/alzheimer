from fpdf import FPDF
import os
from datetime import datetime

def generate_pdf_report(name, age, result, confidence):
    filename = f"{name.replace(' ', '_')}_Alzheimer_Report.pdf"
    filepath = os.path.join("generated_reports", filename)
    os.makedirs("generated_reports", exist_ok=True)

    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", 'B', 16)
    pdf.cell(200, 10, "Alzheimer Diagnostic Report", ln=True, align='C')

    pdf.set_font("Arial", '', 12)
    pdf.cell(200, 10, f"Name: {name}", ln=True)
    pdf.cell(200, 10, f"Age: {age}", ln=True)
    pdf.cell(200, 10, f"Date: {datetime.today().strftime('%Y-%m-%d')}", ln=True)
    pdf.cell(200, 10, f"\nMRI Diagnosis: {result}", ln=True)
    pdf.cell(200, 10, f"Confidence: {confidence}%", ln=True)

    pdf.multi_cell(0, 10, "\nDiagnosis Summary:")
    if result != "NonDemented":
        pdf.multi_cell(0, 10, "Signs of Alzheimer's disease detected. Immediate clinical consultation recommended.")
    else:
        pdf.multi_cell(0, 10, "No signs of Alzheimer's disease were detected in the scan.")

    pdf.multi_cell(0, 10, "\nRecommendations:\n- Follow up with a neurologist.\n- Maintain a healthy lifestyle.")
    pdf.output(filepath)
    return filepath
