# reportlab-action
[![Build Container Image](https://github.com/sksat/reportlab-action/actions/workflows/build-image.yml/badge.svg)](https://github.com/sksat/reportlab-action/actions/workflows/build-image.yml)
[![test Action](https://github.com/sksat/reportlab-action/actions/workflows/test-action.yml/badge.svg)](https://github.com/sksat/reportlab-action/actions/workflows/test-action.yml)

Edit PDF on GitHub Actions by ReporLab

## example

```yaml
- uses: ./
  with:
    script: hello.py
    output: hello.pdf
```

hello.py
```python
from PyPDF2 import PdfFileWriter, PdfFileReader

from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4

def generate(output):
    print("hello")
    c = canvas.Canvas(output)
    c.drawString(100, 100, "hello")
    c.save()
```
