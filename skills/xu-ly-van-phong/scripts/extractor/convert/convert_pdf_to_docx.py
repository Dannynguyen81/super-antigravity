import os
import sys

def convert_pdf_to_docx(pdf_file, output_file):
    """Convert PDF file to DOCX using pdf2docx."""
    try:
        from pdf2docx import Converter
    except ImportError:
        print("pdf2docx is not installed. Installing...")
        import subprocess
        subprocess.check_call([sys.executable, "-m", "pip", "install", "pdf2docx"])
        from pdf2docx import Converter

    print(f"Converting {pdf_file} to {output_file}...")
    cv = Converter(pdf_file)
    cv.convert(output_file, start=0, end=None)
    cv.close()
    print(f"Created: {output_file}")

if __name__ == '__main__':
    if len(sys.argv) > 2:
        convert_pdf_to_docx(sys.argv[1], sys.argv[2])
    else:
        print("Usage: python convert_pdf_to_docx.py <input.pdf> <output.docx>")
