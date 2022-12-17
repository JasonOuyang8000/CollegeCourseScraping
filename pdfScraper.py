from pdfreader import PDFDocument, SimplePDFViewer
from io import BytesIO
import json
with open("assets/school_1.pdf", "rb") as f:
    fd = BytesIO(f.read())

viewer = SimplePDFViewer(fd)
viewer.navigate(3)
viewer.render()
data = viewer.canvas.strings

with open('app.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)