from PyPDF2 import PdfFileWriter, PdfFileReader

from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4

def generate(output):
    c = canvas.Canvas(output)
    c.drawString(100, 100, "hello")
    c.save()
