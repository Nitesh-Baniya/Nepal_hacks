from fpdf import FPDF
import io
import os

# Function to create PDF from text
def create_pdf_from_text(text, filename):
    pdf = FPDF()
    pdf.add_page()

    # Set auto page break and margin
    pdf.set_auto_page_break(auto=True, margin=15)

    # Add font (ensure the correct path to the font is specified)
    font_path = "fonts/DejaVuSans.ttf"  # Replace with your actual path to the .ttf file
    if not os.path.exists(font_path):
        raise RuntimeError(f"Font file not found: {font_path}")

    pdf.add_font("DejaVu", "", font_path, uni=True)
    pdf.set_font("DejaVu", size=12)

    # Split text into lines for proper line spacing in the PDF
    lines = text.split("\n")
    for line in lines:
        pdf.multi_cell(0, 10, line)

    # Create a BytesIO buffer to hold the PDF data in memory
    pdf_output = io.BytesIO()

    # Write PDF data to the buffer (use "output" to a BytesIO object)
    pdf.output(pdf_output)

    # Move the buffer’s cursor back to the start
    pdf_output.seek(0)

    return pdf_output